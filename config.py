#Script execute True or False

#Software Update
UpdateUpgrade = False
Reboot        = False #Recommended always be True

#Raspberry configs
SSH           = False
VNC           = False
Camera        = False
Overscan      = False #Enable if you see black edges
Hostname      = False #Reboot forced
hostname      = "argon"
Overclock     = False
overclock     = "Modest" #Modest|Medium|High|Turbo Currently only for Pi4
Timezone      = False
timezone      = "Europe/Madrid" #run "timedatectl list-timezones" for a list
Keyboard      = False #Change keyboard layout
keyboard      = "es" #es = Spanish | gb = British
Wifi          = False #Adding new wifi
ssid          = "ssid_name" #Wifi name
ssid_pass     = "******" #Wifi password
country       = "ES"

#Software/Programs
Argon         = False
Moonlight     = False
Firefox       = False
MariaDB       = False #Includes initial setup. Removes test DB and sets new root password
mariadb_pass  = "newpassword"

#Packages
PySimpleGui   = False



import subprocess
import os
from time import sleep
def Ex(cmd):
  print(cmd)
  result = subprocess.call(cmd,shell=True)
  print("End of: " + cmd)
  sleep(5)
  
#apt update & upgrade
if UpdateUpgrade == True:
  Ex("sudo apt-get update")
  Ex("sudo apt-get -y upgrade")

#Wifi
if Wifi == True:
  Ex("raspi-config nonint do_wifi_country " + country)
  Ex("raspi-config nonint do_wifi_ssid_passphrase " + ssid + " " + ssid_pass)

#Timezone
if Timezone == True:
  Ex("sudo timedatectl set-timezone " + timezone)

#Overscan
if Overscan == True:
  Ex("sudo raspi-config nonint do_overscan 0")

#SSH
if SSH == True:
  Ex("sudo raspi-config nonint do_ssh 0")

#VNC
if VNC == True:
  Ex("sudo raspi-config nonint do_vnc 0")

#Camera
if Camera == True:
  Ex("sudo raspi-config nonint do_camera 0")

#Keyboard
if Keyboard == True:
  Ex("sudo raspi-config nonint do_configure_keyboard " + keyboard)

#Moonlight
if Moonlight == True:
  Ex("curl -1sLf 'https://dl.cloudsmith.io/public/moonlight-game-streaming/moonlight-qt/setup.deb.sh' | sudo -E bash")
  Ex("sudo apt -y install moonlight-qt")

#Argon
if Argon == True:
  Ex("curl https://download.argon40.com/argon1.sh | bash")

#Firefox
if Firefox == True:
  Ex("sudo apt-get -y install firefox-esr")

#PySimpleGui
if PySimpleGui == True:
  Ex("yes | pip install pysimplegui")

#MariaDB
if MariaDB == True:
  Ex("sudo apt-get -y install mariadb-server")
  Ex("sudo mysql -e \"UPDATE mysql.user SET Password = PASSWORD(\'" + mariadb_pass + "\') WHERE User = \'root\'\"")
  Ex("sudo mysql -e \"DROP USER IF EXISTS ''@'localhost'\"")
  Ex("sudo mysql -e 'DROP DATABASE IF EXISTS test'")

#Overclock
if Overclock == True:
  if overclock == "Modest":
    Ex("set_config_var arm_freq" + 800)
    Ex("set_config_var core_freq" + 250)
    Ex("set_config_var sdram_freq" + 400)
    Ex("set_config_var over_voltage" + 0)
  
  elif overclock == "Medium":
    Ex("set_config_var arm_freq" + 900)
    Ex("set_config_var core_freq" + 250)
    Ex("set_config_var sdram_freq" + 450)
    Ex("set_config_var over_voltage" + 2)
  
  elif overclock == "High":
    Ex("set_config_var arm_freq" + 950)
    Ex("set_config_var core_freq" + 250)
    Ex("set_config_var sdram_freq" + 450)
    Ex("set_config_var over_voltage" + 6)
  
  elif overclock == "Turbo":
    Ex("set_config_var arm_freq" + 1000)
    Ex("set_config_var core_freq" + 500)
    Ex("set_config_var sdram_freq" + 600)
    Ex("set_config_var over_voltage" + 6)

#Change HostName
if Hostname == True:
  Ex("raspi-config nonint do_hostname " + hostname)

#Reboot
if Reboot == True or Hostname == True:
  Ex("sudo reboot")
