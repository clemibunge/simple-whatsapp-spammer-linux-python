#!/usr/bin/env python3
import subprocess
import time
import sys
# open the textfile
text = open(sys.argv[1]).read().strip()
print("SPAM BEGINS IN 10 SECOUNDS!!!")
time.sleep(10)
for ch in text:
    # type out the text
    subprocess.call(["xdotool", "type", ch])
    # increase or decrease the time below to type slower or faster
    time.sleep(0.0001)
