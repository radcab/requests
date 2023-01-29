import radcabToolz
import requests
import time
import os


def clear():
    os.system('cls')

def checkCode(file):
    file = radcabToolz.readFile(file)
    for files in file:
        req = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{files}?with_application=false&with_subscription_plan=true")
        if req.status_code == 200:
            print(f"HIT | {files}")
            input("<<< Press Enter to Exit. >>>")
            exit()
        
        else:
            print(f"INVALID | {files}")

def home():
    os.system('cls')
    radcabToolz.typeStr('''
=============================================================

            giftchecker.py / github.com/radcab
            
=============================================================
                        ''', delay=0.01)

    radcabToolz.typeStr('''
1 - Start Checking
2 - Exit

''', delay=0.02)
    var = input("")
    if var == "1":
        radcabToolz.typeStr("\n<<< Enter the name of the txt file >>> : ", delay=0.02)
        print("\n")
        file = input("")
        print("\n")
        checkCode(file)
        radcabToolz.typeStr("\nFinished checking", delay=0.02)
        radcabToolz.typeStr("\n<<< Exiting in 3 seconds >>>", delay=0.02)
        time.sleep(3)
        exit()
    elif var == "2":
        radcabToolz.typeStr("\n<<< Exiting in 3 seconds >>>", delay=0.02)
        time.sleep(3)
        exit()
    else:
        radcabToolz.typeStr("\n<<< Invalid choice, returning to home screen. >>>", delay=0.02)
        time.sleep(2)
        clear()
        home()
        
home()