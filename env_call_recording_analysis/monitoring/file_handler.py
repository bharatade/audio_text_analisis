import os
import logging
from datetime import datetime
from watchdog.events import FileSystemEventHandler
from models.asr_model import transcribe_audio
from models.llm_model import translate_to_english, classify_busy, generate_summary
from database.db_operations import insert_record
from configs.config import TARGET_LANG

class RecordingHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_name = os.path.basename(file_path)

            try:
                print(f"📝 Processing: {file_name}")
                transcript_local = transcribe_audio(file_path)
                transcript_english = (translate_to_english(transcript_local) 
                                      if TARGET_LANG != "en" else transcript_local)

                if transcript_local:
                    isBusy = classify_busy(transcript_local)
                    status = "Successful" if isBusy else "Unsuccessful"
                    summary = generate_summary(transcript_english)
                else:
                    isBusy, status, summary = 0, "Mute", "No conversation detected."

                insert_record(TARGET_LANG, file_name, transcript_english, transcript_local,
                              "DSO123", "DMI456", isBusy, status, summary)

                logging.info(f"Processed: {file_name} at {datetime.now()}")

            except Exception as e:
                logging.error(f"Error processing {file_name}: {e}")
