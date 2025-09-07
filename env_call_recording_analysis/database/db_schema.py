from .db_connection import get_connection

def ensure_table_exists():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='speech_analysiss3' AND xtype='U')
    CREATE TABLE speech_analysiss3 (
        ID INT IDENTITY(1,1) PRIMARY KEY,
        Language NVARCHAR(10),
        RecordingFileName NVARCHAR(255),
        TranscriptEnglish NVARCHAR(MAX),
        TranscriptLocal NVARCHAR(MAX),
        DSO_ID NVARCHAR(50),
        DMI_ID NVARCHAR(50),
        IsValidCall BIT,
        Status NVARCHAR(50),
        Summary NVARCHAR(MAX),
        InsertedOn DATETIME DEFAULT GETDATE()
    )
    """)
    conn.commit()
    conn.close()
