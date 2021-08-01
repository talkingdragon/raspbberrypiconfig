#Script execute True or False
UpdateUpgrade = False
Argon         = False
SSH           = False
VNC           = False
Moonlight     = False
Firefox       = False
MariaDB       = False
PySimpleGui   = False
Hostname      = False #Reboot forced
hostname      = "raspberry2
Overclock     = False
overclock     = 1750
GPU           = False #GPU memory split
gpu           = 256 #256, 512, 1024
Country       = False #Wifi country
country       = "ES"
Keyboard      = False
keyboard      = "ES"
Wifi          = False #Adding
ssid          = "ssid_name" #wifi name
ssid_pass     = "******" #wifi password


import subprocess
import os
from time import sleep
def Ex(cmd):
  print(cmd)
  result = subprocess.call(cmd,shell=True)
  print("End of: " + cmd)
  
  #apt update & upgrade
  if UpdateUpgrade = True:
    Ex("sudo apt-get update")
    Ex("sudo apt-get -y upgrade")
