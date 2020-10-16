from gtts import gTTS
import os


myText="Abdullah Mujahid"

language="en"


output = gTTS(text=myText,lang=langauge,slow=False)


output.save("output.mp3")

os.system("start output.mp3")