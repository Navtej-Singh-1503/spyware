

'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

17/02/2026

Version - 0.2.1

mail - navtejsingh15032011@gmail.com

'''


target_ip = input("Enter target's IP address ..>>  ")


line2 = f"target = '{target_ip}'"


with open("FILES/IP.py", "w") as f:
    f.write(line2)


print("Setup Completed !!")
print('Now you can run "main.py"')
print("whitehorse is the RAT")


