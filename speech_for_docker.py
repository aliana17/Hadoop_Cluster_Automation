def sv():
	import pyttsx3
	import socket
	s = socket.socket()
	engine=pyttsx3.init()
	print("welcome to dockers setup tool...please enter the ip of master")
	engine.say("welcome to dockers setup tool...please enter the ip of master")
	engine.runAndWait()
	ipm = input()
	s.connect((ipm,4000))
	print("do you want to setup dockers?")
	engine.say("do you want to setup dockers?")
	engine.runAndWait()
	print(" please enter ur response in yes or no")
	engine.say("please enter ur response in yes or no")
	engine.runAndWait()
	text=input()
	print(text)
	if "yes" in text:
            cmd = "python36 /root/Full/dockers.py"
            cmd1 = cmd.encode()
            s.send(cmd1)
            print(s.recv(1024))
            e = pyttsx3.init()
            e.say(s.recv(1024))
            e.runAndWait()
	else:
		engine.say("you have entered no ....exiting from dockers setup tool")
		engine.runAndWait()
		exit()

