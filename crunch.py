#!usr/bin/evn python3
import subprocess
linux = input("what's your os , if you are using linux [sudo] and termux hit [enter] >>>")
subprocess.call(linux + " apt install crunch ", shell=True)
digit = input("digits >>> ")
values = input("input >>> ")
cd = input("directory >>> ")
subprocess.call(linux + " crunch " + digit + values + cd, shell=True)
subprocess.call(linux + " cd " + cd, shell=True)
a = "your text file has been saved here"
print(a)
