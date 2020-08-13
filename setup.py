#!usr/bin/evn python3
import subprocess
linux = input("what's your os , if you are using linux [sudo] and termux hit [enter] >>>")
subprocess.call(linux + " apt install crunch ", shell=True)
