import torch
import nemo.collections.asr as nemo_asr
from configs.config import NEMO_CHECKPOINT, LANG_ID, TEMP_WAV_PATH
from services.audio_utils import convert_to_wav

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print("🔄 Loading NeMo ASR model...")
asr_model = nemo_asr.models.EncDecHybridRNNTCTCBPEModel.restore_from(restore_path=NEMO_CHECKPOINT)
asr_model.freeze()
asr_model = asr_model.to(device)
asr_model.cur_decoder = "ctc"

def transcribe_audio(file_path):
    convert_to_wav(file_path, TEMP_WAV_PATH)
    with torch.no_grad():
        transcripts = asr_model.transcribe([TEMP_WAV_PATH], batch_size=1, language_id=LANG_ID)
    text = transcripts[0][0] if isinstance(transcripts[0], list) else transcripts[0]
    return text.strip()
