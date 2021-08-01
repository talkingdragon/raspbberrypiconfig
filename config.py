#Script execute True or False

#Software Update
UpdateUpgrade = False

#Raspberry configs
SSH           = False
VNC           = False
Camera        = False
Overscan      = False #Enable if you see black edges
Hostname      = False #Reboot forced
hostname      = "raspberry2"
Overclock     = False
overclock     = None #None|Modest|Medium|High|Turbo Currently only for Pi4
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

#Change HostName
if Hostname = True:
  Ex("raspi-config nonint do_hostname " + hostname)

#SSH
if SSH = True:
  Ex("sudo raspi-config nonint do_ssh 1") #need verify is 1 is on

#VNC
if VNC = True:
  Ex("sudo raspi-config nonint do_vnc 1") #need verify is 1 is on

#Camera
if Camera = True:
  Ex("sudo raspi-config nonint do_camera 1") #need verify is 1 is on

#Moonlight
if Moonlight = True:
  Ex("curl -1sLf 'https://dl.cloudsmith.io/public/moonlight-game-streaming/moonlight-qt/setup.deb.sh' | sudo -E bash")
  Ex("sudo apt install moonlight-qt")

#Argon
if Argon = True:
  Ex("curl https://download.argon40.com/argon1.sh | bash")

#Firefox
if Firefox = True:
  Ex("sudo apt-get install firefox-esr")

#Overclock
if Overclock = True:
  if overclock = Modest
  Ex("set_config_var arm_freq" + 800)
  Ex("set_config_var core_freq" + 250)
  Ex("set_config_var sdram_freq" + 400)
  Ex("set_config_var over_voltage" + 0)
  
  elif overclock = Medium
  Ex("set_config_var arm_freq" + 900)
  Ex("set_config_var core_freq" + 250)
  Ex("set_config_var sdram_freq" + 450)
  Ex("set_config_var over_voltage" + 2)
  
  elif overclock = High
  Ex("set_config_var arm_freq" + 950)
  Ex("set_config_var core_freq" + 250)
  Ex("set_config_var sdram_freq" + 450)
  Ex("set_config_var over_voltage" + 6)
  
  elif overclock = Turbo
  Ex("set_config_var arm_freq" + 1000)
  Ex("set_config_var core_freq" + 500)
  Ex("set_config_var sdram_freq" + 600)
  Ex("set_config_var over_voltage" + 6)
