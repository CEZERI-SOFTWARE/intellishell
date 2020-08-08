import os
import getpass
import socket
import psutil
import sys
import sysconfig
import random
import platform
import subprocess
import cmd
import ssl
import datetime
import time

def fetch():
    print(bcolors.OKGREEN + username + bcolors.ENDC + "'s computer")
    print("Name: " + bcolors.OKGREEN  + hostname + bcolors.ENDC) 
def fetch_os():
      if platform.system() == "Darwin":
        print("""
                        .888"
                      .8888'"
                    .8888'"
                    888'"
                    8'"
        .88888888888. .88888888888."
    .8888888888888888888888888888888." 
  .8888888888888888888888888888888888." 
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:"
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:"
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:"
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%."
  00000000000000000000000000000000000"
    000000000000000000000000000000000"
    0000000000000000000000000000000"
      ###########################"
      #######################"
          #################"
        
  """)
     print("Kernel Name: Darwin")
     print("OS name: MacOS")
    elif platform.system() == "Windows":
      print("""
             _.-;;-._
      '-..-'|   ||   |
      '-..-'|_.-;;-._|
      '-..-'|   ||   |
      '-..-'|_.-''-._|
""")
      print("Kernel Name: ")
      print("NT")
      print("OS Name: ")
      print("Windows")
      print("Release:")
      print(platform.release())
    elif platform.system() == "Linux":
      print("""
        dGGGGMMb
       @p~qp~~qMb  
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL   
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' 

""")
      print("Kernel: " + bcolors.OKGREEN)
      print("Linux" + bcolors.ENDC)
      print("Kernel Release: ")
      print(bcolors.OKGREEN + platform.release() + bcolors.ENDC)
      print("Distribution: " + bcolors.OKGREEN)
      os.system(distribution)

      
def fetch_etc():
  print(bcolors.ENDC + "Platform:")
  print(bcolors.OKGREEN + sysconfig.get_platform() + bcolors.ENDC)