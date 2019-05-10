def s():
	import pyttsx3
	import socket
	import speech_recognition as sr
	s=socket.socket()
	engine=pyttsx3.init()
	print("welcome to hadoop setup tool...please enter the ip of master")
	engine.say("welcome to hadoop setup tool...please enter the ip of master")
	engine.runAndWait()
	ipm=input()
	print(ipm)
	s.connect((ipm,4000))
	print("enter ur response in yes or no")
	text=input()
	print(text)
	if "yes" in text:
		cmd="python36 /root/Full/hcluster.py"
		cmd1=cmd.encode()
		s.send(cmd1)
	else:
		engine.say("you have entered no ....exiting from hadoop setup tool")
		engine.runAndWait()
		exit()



