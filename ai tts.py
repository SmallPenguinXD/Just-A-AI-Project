# -*- coding: utf-8 -*-
from TTS.api import TTS
import tkinter as tk
import pyautogui
def tts_f():
    ai_vc_cl_file = r"voice_clone_wav\input.wav"
    text = input_word.get()
    if(text is None or text == ""):
        text = "Bro thing I know what you want"
    tts = TTS("tts_models/en/vctk/vits",vocoder_name="vocoder_models/en/librispeech100/wavlm-hifigan_prematched")
    tts.tts_to_file(f"{text}",file_path="vc_op_wav.wav",split_sentences=True,speaker="p225")
    tts2 = TTS("voice_conversion_models/multilingual/multi-dataset/openvoice_v2")
    tts2.voice_conversion_to_file(source_wav ="vc_op_wav.wav" , target_wav=ai_vc_cl_file,file_path="finally.wav")
if __name__ == "__main__":
    ttsgui = tk.Tk()
    weight_w1 ,height_w1 = pyautogui.size()
    weight_w2 ,height_w2 = weight_w1//2 ,height_w1//2 
    print(weight_w2,height_w2)
    ttsgui.geometry(f'{weight_w2}x{height_w2}')
    tk.Label(ttsgui,text="請輸入文本來輸入聊天內容").pack()
    input_word = tk.Entry(ttsgui)
    input_word.pack()
    s_btn_getin = tk.Button(ttsgui,text="開始TTS",command=tts_f())
    s_btn_getin.pack()
    ttsgui.mainloop()