#Script execute True or False

#Software Update
UpdateUpgrade = False

#Raspberry configs
SSH           = False
VNC           = False
Camera        = False
Overscan      = False #Enable if you see black edges
Hostname      = False #Reboot forced
hostname      = "raspberry2
Overclock     = False
overclock     = 1750
GPU           = False #GPU memory split
gpu           = 256 #256, 512, 1024
Country       = False #Wifi country
country       = "ES"
TimeZone      = False
timezone      = "Europe/Spain" #run "timedatectl list-timezones" for a list
Keyboard      = False
keyboard      = "ES"
Wifi          = False #Adding
ssid          = "ssid_name" #wifi name
ssid_pass     = "******" #wifi password

#Software/Programs
Argon         = False
Moonlight     = False
Firefox       = False
MariaDB       = False #Includes initial setup. Removes test DB and sets new root password
mariadb_pass  = "****"

#Packages
PySimpleGui   = False



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
