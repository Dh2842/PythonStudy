from gtts import gTTS
from playsound import playsound
import os

text = '아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ'
tts = gTTS(text = text, lang= "ko")
fileName ="tovoice1" 
fileExtension = "mp3"

fullpath:str = fr"{os.getcwd()}/{fileName}.{fileExtension}".replace("\\","/")
print(fullpath)

tts.save(fullpath)
playsound(fullpath)