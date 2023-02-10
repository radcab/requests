import radcabToolz
import requests
import time
import os
import string
import random
import threading
import queue
from radcabToolz import coolTitle, typeStr, readFile


def count_lines(filename):

    with open(filename) as file:
        lines = file.readlines()
        total_lines = len(lines)
        return total_lines 



check = 1
radcabToolz.coolTitle('giftchecker.py / github.com/radcab')
class checkGift:
    def __init__(self, code_queue):
        self.code_queue = code_queue

    def checkCode(self):
        global check
        while not self.code_queue.empty():
            code = self.code_queue.get()
            req = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if req.status_code == 200:
                print(f"HIT | http://discord.gift/{code}")
                check = 2
                file = open('HIT.txt', 'w')
                file.write(f'http://discord.gift/{code}' + '\n')
                input("<<< Press Enter to Exit. >>>")
                exit()
            else:
                print(f"INVALID | http://discord.gift/{code}")
                if check == 2:
                    exit()
def clear():
    os.system('cls')
    
def home():
    clear()
    print('''
=============================================================

            giftchecker.py / github.com/radcab
            
=============================================================
''')

    radcabToolz.typeStr('''
1 - Start Checking
2 - Generate Codes
3 - Exit
''', delay=0.02)
    print("\n")
    var = input("> ")
    if var == "1":
        clear()
        radcabToolz.typeStr("\n<<< Enter the name of the txt file >>> : ", delay=0.02)
        file = input("")
        radcabToolz.typeStr("\n<<< How many threads would you like to use? >>> : ", delay=0.02)
        thread_amount = input("")
        amount_of_t = int(thread_amount)
        if amount_of_t < 0:
            radcabToolz.typeStr("\n<<< You must use atleast 1 thread! >>>", delay=0.01)
            radcabToolz.typeStr("\n<<< Returning to home screen. >>>", delay=0.02)
        try:
            count = count_lines(file)
            radcabToolz.coolTitle(f'giftchecker.py / {count} codes / LOADED')
            code_queue = queue.Queue()
            with open(file, 'r') as f:
                for line in f:
                    code_queue.put(line.strip())
        
            for i in range(amount_of_t):
                check_gifts = checkGift(code_queue)
                thread = threading.Thread(target=check_gifts.checkCode)
                thread.start()
            for i in range(amount_of_t):
                thread.join()
            time.sleep(1)
            radcabToolz.typeStr("\n<<< Finished checking, returning to home screen. >>>", delay=0.02)
            time.sleep(3)
            home()
        
        except:
            radcabToolz.typeStr("\n<<< Unknown Error, going back to home screen. >>>", delay=0.01)
            time.sleep(3)
            home()
        
    elif var == "2":
        clear()
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
            clear()
            home()
        radcabToolz.typeStr("\n<<< Finished generating and saved to codes.txt, returning to home screen. >>>", delay=0.02)
        time.sleep(2)
        clear()
        home()

    elif var == "3":
        clear()
        radcabToolz.typeStr("\n<<< Exiting in 3 seconds >>>", delay=0.02)
        time.sleep(3)
        exit()
    else:
        radcabToolz.typeStr("\n<<< Invalid choice, returning to home screen. >>>", delay=0.02)
        time.sleep(1)
        clear()
        home()
home()
