import subprocess as sp
b = False

a = input("t or f Are you using linux or termux >>>")
if (a == "t" or a == "T"):
	b = True
if (a == "f" or a == "F"):
	b = False
	
if b == True: 
	sp.run('sudo apt-get install -y crunch',shell=True)
elif b == False: 
	print("It was not completed") 
