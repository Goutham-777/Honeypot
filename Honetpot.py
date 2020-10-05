#!bin/python

import socket
import os
import time
import optparse
import sys
from termcolor import *

parser = optparse.OptionParser()
parser.add_option('--ipaddr', '--ip_adrress', dest='ip', help='Used to mention ip address to Start Honeypot')
(option, argu) = parser.parse_args()

ip = option.ip
time.sleep(1)
os.system("clear")
print (colored("[•]Honeypot Started.....", 'yellow'))

def pot():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, 80))
        s.listen(80)
        while True:
            client_con,client_addr = s.accept()
            print ("Visiter Found ![{}]".format(client_addr[0]))
            client_con.send(b"<h1>$You Has Been Hacked!!</h1>")
            data = client_con.recv(1024)
            print (data.decode('utf-8'))
    except KeyboardInterrupt as g:
        print (colored("\nHoneypot Stopped!!", 'blue'))
        sys.exit()
        s.close()
    except PermissionError as P:
        print (colored('Run as root', 'red'))
        sys.exit()
    except ConnectionResetError as E:
        print (colored(f'[{client_addr[0]}]  This ip Scanned with Nmap', 'red'))
        pot()
    except OSError as Os:
        time.sleep(1)
        s.close()
    finally:
        s.close()

if __name__ == "__main__":
    while True:
        pot()
