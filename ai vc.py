# -*- coding: utf-8 -*-
from TTS.api import TTS
if __name__ == "__main__":
    ai_vc_cl_file = r"voice_clone_wav\input.wav"
    tts2 = TTS("voice_conversion_models/multilingual/multi-dataset/openvoice_v2")
    tts2.voice_conversion_to_file(source_wav ="record.wav" , target_wav=ai_vc_cl_file,file_path="vc_finally.wav")
