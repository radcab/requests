import radcabToolz
import requests
import time
import os
import string
import random
import threading

check = 1
radcabToolz.coolTitle('giftchecker.py / github.com/radcab')

class checkGift:
    def __init__(self):
        t = threading.Thread(target=self.checkCode)
        t.start

    def clear(self):
        os.system('cls')

    def checkCode(self, file):
        file = radcabToolz.readFile(file)
        for files in file:
            req = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{files}?with_application=false&with_subscription_plan=true")
            global check
            if req.status_code == 200:
                print(f"HIT | http://discord.gift/{files}")
                check = 1
                input("<<< Press Enter to Exit. >>>")
                exit()
        
            else:
                print(f"INVALID | http://discord.gift/{files}")
                if check == 2:
                    exit()

    def home(self):
        self.clear()
        radcabToolz.typeStr('''
=============================================================

            giftchecker.py / github.com/radcab
            
=============================================================
                        ''', delay=0.01)

        radcabToolz.typeStr('''
1 - Start Checking
2 - Generate Codes
3 - Exit

''', delay=0.02)
        var = input("")
        if var == "1":
            self.clear()
            radcabToolz.typeStr("\n<<< Enter the name of the txt file >>> : ", delay=0.02)
            file = input("")
            print("\n")
            for i in range(900):
                self.checkCode(file)
                break
            radcabToolz.typeStr("\n<<< Finished checking, returning to home screen. >>>", delay=0.02)
            time.sleep(3)
            self.home()
            
        elif var == "2":
            self.clear()
            radcabToolz.typeStr("\n<<< How many codes would you like to generate? >>> : ", delay=0.02)
            var2 = input("")
            try:
                file = open('codes.txt', 'w')
                for i in range(int(var2)):
                    code1 = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                    file.write(f'{code1}' + '\n')   
                    print(f'http://discord.gift/{code1}')
                file.close()
            except ValueError:
                radcabToolz.typeStr("\n<<< Invalid choice, returning to home screen. >>> ", delay=0.02)
                time.sleep(2)
                self.clear()
                self.home()
            radcabToolz.typeStr("\n<<< Finished generating and saved to codes.txt, returning to home screen. >>>", delay=0.02)
            time.sleep(2)
            self.clear()
            self.home()

        elif var == "3":
            self.clear()
            radcabToolz.typeStr("\n<<< Exiting in 3 seconds >>>", delay=0.02)
            time.sleep(3)
            exit()
        else:
            radcabToolz.typeStr("\n<<< Invalid choice, returning to home screen. >>>", delay=0.02)
            time.sleep(2)
            self.clear()
            self.home()
    
        
        
checkGift().home()
