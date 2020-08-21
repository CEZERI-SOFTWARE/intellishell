import os
import getpass
import socket
import psutil
import sys
import sysconfig
import random
import platform
import distro
import subprocess
import cmd
import ssl
import distro
import cpuid
import GPUtil
import csv
import datetime
import time

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

version = "1.0.0"
hostname = socket.gethostname()
username = getpass.getuser()
suankizaman = datetime.datetime.now()

def fetch():
    print(colors.BLUE + "Intellifetch " + version + colors.END)
    print()
def fetch_os():
    if platform.system() == "Darwin":
     print("""
                      .888
                    .8888'
                   .8888'
                   888'
                   8'
      .88888888888. .88888888888.
   .8888888888888888888888888888888.
 .8888888888888888888888888888888888.
.&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
 00000000000000000000000000000000000
  000000000000000000000000000000000
   0000000000000000000000000000000
     ###########################
     #######################
         #################
      
""")
     print("Kernel Name: Darwin")
     print("OS name: MacOS")
    elif platform.system() == "Windows":
      
     print("       _.-;;-._     " + colors.GREEN + username + colors.END + "'s " +colors.GREEN + hostname + colors.END)
     print("-..--'|   ||   |    " + "--------------")
     print("'-..-'|_.-;;-._|    " + "Kernel Name: ")
     print("'-..-'|   ||   |    " + colors.GREEN + "NT" + colors.END)   
     print("'-..-'|_.-''-._|    " + "OS Name: ")
     print("                    " + colors.GREEN + "Windows" + colors.END)
     print("                    " + "Release: ")
     print("                    " + colors.GREEN +  platform.release() + colors.END)

    elif platform.system() == "Linux":
      
      print("      dGGGGMMb")        
      print("      p~qp~~qMb      " + colors.GREEN + username + colors.END + "'s " +colors.GREEN + hostname + colors.END)
      print("      M|@||@)M|      " + " ------------")
      print("      @,----.JM|     |" + "Kernel: ")
      print("     JS^\__/  qKL    |" + colors.GREEN + "Linux " + colors.END +  platform.release())
      print("    dZP        qKRb  |" + "Distribution: ")
      print("   dZP          qKKb |" + colors.GREEN + distro.id() + colors.END)
      print(" fZP            SMMb |" + colors.END + "Platform:")
      print(" HZM            MMMM |" + colors.GREEN + sysconfig.get_platform() + colors.END)
      print(" FqM            MMMM |")
      print("  __|          \dSqML")
      print(" |    `.       | `' \Zq    ")
      print("_)      \.___.,|     .'     ")
      print("\____   )MMMMMP|   .'    ")
      print("     `-'       `--'      ")
