#!/usr/bin/env python3
import subprocess
import time
import sys


message = input("Spam Message: ")
msgint = int(input("How often?: "))

print("SPAM BEGINS IN 10 SECS!!!")
time.sleep(10)

for i in range(msgint):
    subprocess.call(["xdotool", "type", message])
    subprocess.call(["xdotool", "key", "Return"])
    sleep 0.1
