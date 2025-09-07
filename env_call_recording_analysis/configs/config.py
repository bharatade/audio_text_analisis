import os

# -------- Paths --------
INPUT_FOLDER = "Bharat"
TEMP_WAV_PATH = "/tmp/temp_fixed.wav"

# -------- Models --------
#LLM_MODEL = "xxxxx"
GROQ_API_KEY = "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"
LLM_MODEL = "openai/gpt-oss-120b"
NEMO_CHECKPOINT = "models/indicconformer_stt_hi_hybrid_rnnt_large.nemo"

# -------- Language --------
TARGET_LANG = "hi"
LANG_CODE_MAP = {
    "mar": "mr", "hi": "hi", "tam": "ta", "tel": "te",
    "guj": "gu", "kan": "kn", "mal": "ml", "ben": "bn", "eng": "en"
}
LANG_ID = LANG_CODE_MAP.get(TARGET_LANG)

# -------- Database Config --------
DB_CONFIG = {
    "server": "xxxx",
    "database": "xxxx",
    "username": "xxxx",
    "password": "xxx"
}

# -------- Logging --------
LOG_FILE = "logs/call_recording_analysis.log"
