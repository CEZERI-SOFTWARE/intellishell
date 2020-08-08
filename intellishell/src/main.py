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
from intellifetch import fetch
from intellifetch import fetch_os
hostname = socket.gethostname()
username = getpass.getuser()

suankizaman = datetime.datetime.now()
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



print("""                                                                                                                                                   
  ___     _       _ _ _    _        _ _ 
 |_ _|_ _| |_ ___| | (_)__| |_  ___| | |
  | || ' \  _/ -_) | | (_-< ' \/ -_) | |
 |___|_||_\__\___|_|_|_/__/_||_\___|_|_|                                           
""")
print(colors.GREEN + 'Welcome to Intellishell, ' + username + "!" + colors.END)
print(colors.WARNING + "Write 'help' to see commands." + colors.END)


print("Current date & time:")
print (suankizaman.strftime("%Y-%m-%d %H:%M:%S" " || " "%I:%M:%S %p"))
print (suankizaman.strftime("%a, %b %d, %Y"))



#Start
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
def main_function():
    while True:
        cmd = input(colors.BLUE + username + colors.END + colors.GREEN  + "@" + colors.BLUE + hostname + colors.END + ": ")
        
          
        if cmd == "exit":
            break
        elif cmd == "credits":
          print("Intellishell v1.0")
          print("Made by Emir Ensar Rahmanlar (github.com/rahmanlar)")
          print("Copyright (c) 2020 Cezeri Software, licensed with MIT.")
        elif cmd == "intellifetch":
          fetch()
          fetch_os()
        elif cmd == "termcmd":
          termcmd = input(colors.BLUE + username + colors.GREEN + "@" + colors.END + colors.BLUE + hostname + colors.END + "(terminal mode)" + ":")
          os.system(termcmd)
        elif cmd == "print":
          prinput = input("print ")
          print(prinput)
        elif cmd == "diskusage":
          print(psutil.disk_usage('/'))
        elif cmd == "help":
          print(colors.GREEN + "credits " + colors.END + "- See who's making this app.")
          print(colors.GREEN + "intellifetch " + colors.END + "- A simple screenfetch.")
          print(colors.GREEN + "termcmd " + colors.END + "- To type terminal or cmd commands only.")
          print(colors.GREEN + "print " + colors.END + "- A simple print function.")
        else:
            terminalcommand = os.system(cmd)
            


main_function()


      


