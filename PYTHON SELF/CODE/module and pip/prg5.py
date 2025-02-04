# install any extrnal module and use as per intrest 
# install pyttx3 and now it will say what i type
import pyttsx3
engine = pyttsx3.init()
engine.say("hello this is speaking bot")
engine.runAndWait()