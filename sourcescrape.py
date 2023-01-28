import requests
import time
from os import system

#Give it a terminal title
system("title " + "sourcescrape.py / github.com/radcab")

#Make the cool type text function
def typeStr(str, delay):
    for i in str:
        print(i, end="", flush=True)
        time.sleep(delay)

title = '''
==============================================================
      
            sourcescrape.py --- github.com/radcab
      
==============================================================
'''
typeStr(title, 0.02)

typeStr('<<< Input the url of your webpage >>> :', delay=0.02)

print("\n")
webpage=input("")

hr1 = "--------------------------------------------------------------"

typeStr("\n"+hr1, 0.02)

#Steal da code!!1!!1
req = requests.get(webpage)

print("\n")
typeStr('<<< Would you like to save or print the output? S/P >>> :', delay=0.02)
print("\n")
var = input("")

#Make it so their input is always capitalized via the capitalize() function
if var.capitalize() == "P":
    print(f"\n"+req.text)
    input(f"\n<<< Press Enter to exit the program. >>>")
    
#Save it to a txt file if they selected S
elif var.capitalize() == "S":
    with open ('output.txt', 'w') as file:  
        file.write(req.text)
    typeStr("\n"+hr1, 0.02)
    input(f"\n<<< Press Enter to exit the program. >>>") 
    
#Exit the code if they typed something else
else:
    print(f"\nInvalid choice!, Qutting in 5s.")
    time.sleep(5)
