import interfaceCustomer as ic
import interfaceAdmin as ia
import getpass
import sys,os

while True:
    print("Type 1 to enter Admin Mode")
    print("Type 2 to enter Customer Mode")
    print("Type 3 to exit")
    choice = input('Enter a choice: ')

    if choice == '1':
        passwd = getpass.getpass()
        if(passwd != 'admin'):
            print('Wrong Password')
        else:
            ia.start()
    if choice == '2':
        ic.start()
    if choice == '3':
        sys.exit(0)

    os.system('pause')
    