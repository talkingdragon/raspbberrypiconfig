#Script execute True or False

#Execute type
Make      = False
Remove    = False
#Type
User      = False
Database  = False
Table     = False

#Data
database  = ""
table     = ""

import subprocess
import os
from time import sleep

def Ex(cmd):
  print(cmd)
  result = subprocess.call(cmd,shell=True)
  print("End of: " + cmd)
  sleep(5)

#Make or Remove a Database
if Make == True and Database == True:
  Ex("sudo mysql -e 'CREATE DATABASE IF NOT EXISTS " + database + "'")
elif Remove == True and Database == True:
  Ex("sudo mysql -e 'DROP DATABASE IF EXISTS " + database + "'")

#Make or Remove a Table
if Make == True and Table == True:
  Ex("sudo mysql -e 'USE " + database +" ; CREATE TABLE IF NOT EXISTS " + table + "'")
elif Remove == True and Table == True:
  Ex("sudo mysql -e 'USE " + database +" ; DROP TABLE IF NOT EXISTS " + table + "'")
