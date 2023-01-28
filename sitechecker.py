import requests
import time
from os import system

#Make it look cooler by giving it a terminal title :)
system("title " + "sitechecker.py")

def checkWebsite(website):
    try:
        #Ctrl + C triggers keyboard interrupt so we will use that to exit our code easily
        print("Press CTRL + C to exit the site checker.")
        while True:
            #Get the status of the website
            status = requests.get(website)
            code = status.status_code
            time.sleep(3)
            #Print it out
            print(f"Returned code {code}")
            
            #Self explanatory basically
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
#Put this just to make it look a little neater
print("Preparing!")

checkWebsite(web)
            

        


            
