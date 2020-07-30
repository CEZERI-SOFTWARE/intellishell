# /* MIT License
#
# Copyright (c) 2020 Emir Ensar All Rights Reserved.
# Distributed under the terms of the MIT License.
#
# */
#   eeeeeeeeeeee    nnnn  nnnnnnnn        ssssssssss     aaaaaaaaaaaaa  rrrrr   rrrrrrrrr   
#  ee::::::::::::ee  n:::nn::::::::nn    ss::::::::::s    a::::::::::::a r::::rrr:::::::::r  
# e::::::eeeee:::::een::::::::::::::nn ss:::::::::::::s   aaaaaaaaa:::::ar:::::::::::::::::r 
#e::::::e     e:::::enn:::::::::::::::n s::::::ssss:::::s           a::::arr::::::rrrrr::::::r
#e:::::::eeeee::::::e  n:::::nnnn:::::n s:::::s  ssssss     aaaaaaa:::::a r:::::r     r:::::r
#e:::::::::::::::::e   n::::n    n::::n   s::::::s        aa::::::::::::a r:::::r     rrrrrrr
#e::::::eeeeeeeeeee    n::::n    n::::n      s::::::s    a::::aaaa::::::a r:::::r            
#e:::::::e             n::::n    n::::n ssssss   s:::::s a::::a    a:::::a r:::::r            
#e::::::::e            n::::n    n::::n s:::::ssss::::::sa::::a    a:::::a r:::::r            
 #e::::::::eeeeeeee    n::::n    n::::n s::::::::::::::s a:::::aaaa::::::a r:::::r            
  #ee:::::::::::::e    n::::n    n::::n s:::::::::::ss   a::::::::::aa:::ar:::::r            
#    eeeeeeeeeeeeee    nnnnnn    nnnnnn  sssssssssss      aaaaaaaaaa  aaaarrrrrrr            



import os
import getpass
import socket
import psutil
import sys
import sysconfig
import random
import platform
import cmd
import ssl
import datetime
import time
hostname = socket.gethostname()
username = getpass.getuser()
suankizaman = datetime.datetime.now()
distribution = "lsb_release -ds"
context = ssl.create_default_context()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



print("""                                                                                                                                                   
  ___     _       _ _ _    _        _ _ 
 |_ _|_ _| |_ ___| | (_)__| |_  ___| | |
  | || ' \  _/ -_) | | (_-< ' \/ -_) | |
 |___|_||_\__\___|_|_|_/__/_||_\___|_|_|                                           
""")
print(bcolors.OKGREEN + 'Welcome to Intellishell, ' + username + "!" + bcolors.ENDC)
print(bcolors.WARNING + "Write 'help' to see commands." + bcolors.ENDC)


print("Current date & time:")
print (suankizaman.strftime("%Y-%m-%d %H:%M:%S" " || " "%I:%M:%S %p"))
print (suankizaman.strftime("%a, %b %d, %Y"))



#Start
def fetch():
    print(bcolors.OKGREEN + username + bcolors.ENDC + "'s computer")
    print("Name: " + bcolors.OKGREEN  + hostname + bcolors.ENDC) 
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
def main_function():
    while True:
        cmd = input(bcolors.OKBLUE + username + bcolors.ENDC + bcolors.OKGREEN  + "@" + bcolors.OKBLUE + hostname + bcolors.ENDC + ": ")
        
          
        if cmd == "exit":
            break
        elif cmd == "credits":
          print("Intellishell v1.0")
          print("Made by Emir Ensar Rahmanlar (github.com/rahmanlar)")
          print("Copyright (c) 2020 Cezeri Software, licensed with MIT.")
        elif cmd == "intellifetch":
          fetch()
          fetch_os()
          fetch_etc()
        elif cmd == "termcmd":
          termcmd = input(bcolors.OKBLUE + username + bcolors.OKGREEN + "@" + bcolors.ENDC + bcolors.OKBLUE + hostname + bcolors.ENDC + "(terminal mode)" + ":")
          os.system(termcmd)
        elif cmd == "print":
          prinput = input("print ")
          print(prinput)
        elif cmd == "diskusage":
          print(psutil.disk_usage('/'))
        elif cmd == "help":
          print("""
credits - See who's making this app.
intellifetch - A simple screenfetch.
termcmd - To type terminal or cmd commands only.
print - A simple print function.
          """)
        else:
            terminalcommand = os.system(cmd)
            


main_function()


      


