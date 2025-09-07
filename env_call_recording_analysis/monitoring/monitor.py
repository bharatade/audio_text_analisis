import time
import logging
from watchdog.observers import Observer
from .file_handler import RecordingHandler
from configs.config import INPUT_FOLDER, LOG_FILE
import os

def start_monitoring():
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    os.makedirs(INPUT_FOLDER, exist_ok=True)
    event_handler = RecordingHandler()
    observer = Observer()
    observer.schedule(event_handler, INPUT_FOLDER, recursive=False)
    observer.start()
    print(f"✅ Monitoring started on folder: {INPUT_FOLDER}")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
