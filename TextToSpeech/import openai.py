import openai
import sounddevice as sd
import soundfile as sf
from gtts import gTTS


openai.api_key = "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"


while True:

  prompt = input("\nWhat can I help with? \n")
  
 
  fjala = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)

  text = fjala["choices"][0]["text"]

 
  tts = gTTS(text)


  tts.save("speech.mp3")

  data, fs = sf.read("speech.mp3", dtype='int16')
  sd.play(data, fs)
  status = sd.wait()  

  print(text)
  