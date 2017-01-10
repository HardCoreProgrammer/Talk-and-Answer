#!/usr/bin/env python2.7

import pyttsx
import speech_recognition as sr

engine = pyttsx.init()
engine.setProperty('rate', 100)


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    audiOut = r.recognize_google(audio)
    mystring = str(audiOut) 
    stan = "hello"
	


try:
    
	
    print("You said " + audiOut)
	
except sr.UnknownValueError:
    print("I could not understand audio")
except sr.RequestError as e:
    print("Could not undestand what you said; {0}".format(e))


	
if mystring == stan:
    print("Hello Andres Silva you are the best")
    engine.say("Hello Andres Silva you are the best")
	
else:
    print("you didn't greet the master")	
	
engine.runAndWait
