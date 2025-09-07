from .db_connection import get_connection

def insert_record(Language, RecordingFileName, TranscriptEnglish, TranscriptLocal,
                  DSO_ID, DMI_ID, IsValidCall, Status, Summary):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO speech_analysiss3 
        (Language, RecordingFileName, TranscriptEnglish,
         TranscriptLocal, DSO_ID, DMI_ID, IsValidCall, Status, Summary)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (Language, RecordingFileName, TranscriptEnglish,
                           TranscriptLocal, DSO_ID, DMI_ID, IsValidCall, Status, Summary))
    conn.close()
