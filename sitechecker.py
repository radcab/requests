import requests
import time
from os import system

system("title " + "sitechecker.py")

def checkWebsite(website):
    try:
        print("Press CTRL + C to exit the site checker.")
        while True:
            status = requests.get(website)
            code = status.status_code
            time.sleep(3)
            print(f"Returned code {code}")
        
            if code == 200:
                print("Site is up!")
        
            elif code == 404:
                print("Site is down!")
        
            else:
                print("Site may be down.")
            
    except KeyboardInterrupt:
        pass
            
            
print('''
--------------------------------------------------------------
      
          sitechecker.py --- github.com/radcab
      
--------------------------------------------------------------
      ''')
web = input("Input the website you want to check: ")
print("Preparing!")

checkWebsite(web)
            

        


            
