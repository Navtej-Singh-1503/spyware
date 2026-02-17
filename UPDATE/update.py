

'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

17/02/2026


mail - navtejsingh15032011@gmail.com

'''



import os
from FILES.color import *


result = os.system("git pull")
    if result == 0:
        print(GREEN+"["+RED+"+"+GREEN+"]"+RESET+ " Tool Updated Successfully!")
    else:
        print(GREEN+"["+RED+"!"+GREEN+"]"+RESET+" Update Failed!")
