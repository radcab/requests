import requests
from os import system

#Give it a terminal title
system("title " + "sllchecker.py")

print('''
==============================================================
      
            sslchecker.py --- github.com/radcab
      
==============================================================
      ''')

site = input("<<< Input your site >>> : ")

try:
    #Request has verify enabled by default so we will not
    #specify it.
    resp = requests.get(site)
    print("")
    print("The inputted site has a SSL Certificate.")
    print("")
    input("<<< Press Enter to exit the program. >>>")
    
except requests.exceptions.SSLError:
    print("")
    print("The inputted site does not have a SSL Certificate.")
    print("")
    input("<<< Press Enter to exit the program. >>>")