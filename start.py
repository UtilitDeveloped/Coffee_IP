import socket
from threading import Thread
from colorama import init 
from colorama import Fore,Back,Style
import os
import time

def banner():
    print('_________________¶¶¶1___¶¶¶____¶¶¶1_______________')
    print('__________________¶¶¶____¶¶¶____1¶¶1______________')
    print('___________________¶¶¶____¶¶¶____¶¶¶______________')
    print('___________________¶¶¶____¶¶¶____¶¶¶______________')
    print('__________________¶¶¶____1¶¶1___1¶¶1______________')
    print('________________1¶¶¶____¶¶¶____¶¶¶1_______________')
    print('______________1¶¶¶____¶¶¶1___¶¶¶1_________________')
    print('_____________¶¶¶1___1¶¶1___1¶¶1___________________')
    print('____________1¶¶1___1¶¶1___1¶¶1____________________')
    print('____________1¶¶1___1¶¶1___1¶¶¶____________________')
    print('_____________¶¶¶____¶¶¶1___¶¶¶1___________________')
    print('______________¶¶¶¶___1¶¶¶___1¶¶¶__________________')
    print('_______________1¶¶¶1___¶¶¶1___¶¶¶¶________________')
    print('_________________1¶¶1____¶¶¶____¶¶¶_______________')
    print('___________________¶¶1____¶¶1____¶¶1______________')
    print('___________________¶¶¶____¶¶¶____¶¶¶______________')
    print('__________________1¶¶1___1¶¶1____¶¶1______________')
    print('_________________¶¶¶____¶¶¶1___1¶¶1_______________')
    print('________________11_____111_____11_________________')
    print('__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('1¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('1¶¶¶¶¶¶¶¶¶¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('1¶¶_______¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________')
    print('__________¶¶___1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1________')
    print('____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11__________')
    print('11_____________________________________________111')
    print('1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1')
    print('__¶¶111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111¶__')

    print('Coffee IP is started')
    init()
    print(Fore.RED + 'WARNING!\nInstall the host to be checked and a set of ports starting from the 1st port to be checked and ending with the last one. When you specify the site domain, start specifying it with "www."',Style.RESET_ALL)

banner()


try:
    time.sleep(2)
    global host
    global port
    global port2
    host = input('Host: ')
    port = int(input('Set the port from: '))
    port2 = int(input('Set the port to: '))
    print(Fore.GREEN + 'Coffee IP starting check ' + host + ' at the port ' + str(port) + '-' + str(port2),Style.RESET_ALL)
except:
    print('Error! You send invalid Port or Host')



while port < port2:
    try:
        port += 1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,int(port)))
        init()
        print(Fore.GREEN + 'Port ' + str(port) + ' Is open')
        s.close()
    except:
        init()
        print(Fore.RED + 'Port ' + str(port) + ' Is close')
