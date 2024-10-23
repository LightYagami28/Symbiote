#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

import random
import subprocess
import ctypes
import sys
import os
import urllib
from os import system, getuid, path
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output
from Checks import *

def banner():
    """
    Displays a custom banner based on random selection.
    """
    RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW, YELLOW2, GREEN2, BRED = (
        '\033[91m', '\033[46m', '\033[36m', '\033[1;91m', '\033[0m',
        '\033[1;32m', '\033[1;93m', '\033[1;92m', "\033[5;35m"
    )
    BLINK, MAGENTA = "\033[5m", "\033[1;34m"
    y = '\033[1;33m'

    # Clear terminal
    system('clear')
    
    # Display banner text
    print(f'''

                                  {YELLOW}...                             
                             {YELLOW}.ckXWMMMMWKx:                        {MAGENTA}|    
                           {YELLOW};0MMMWKOOOKWMMMWk'                     {MAGENTA}|     
                         {YELLOW}'KMMWd'       .oNMMMk.                   {MAGENTA}|     
                        {YELLOW}lMM0d.  {CYAN}.:cllc,.  {YELLOW}cKWMN.                  {MAGENTA}|     
                       {YELLOW}oMWc  {CYAN}'kWMMMMMMMMKl. {YELLOW}.XMW.                 {MAGENTA}|    
                      {YELLOW};MW, {CYAN}.OMMMMMMMMMMMMMWd. {YELLOW}KMN                 {MAGENTA}|              
                      {YELLOW}XM: {CYAN};NMMMMMMMMMMMMMMMMN;{YELLOW}.XMx                {MAGENTA}|              {GREEN}░░░░░░░ ░░    ░░ ░░░    ░░░ ░░░░░░  ░░  ░░░░░░  ░░░░░░░░ ░░░░░░░{CYAN}  
                      {YELLOW}XM: {CYAN}.OMMMMMMMMMMMMMMMMMWd. {YELLOW}KMN                 {MAGENTA}| 
                    {CYAN}'kMMWd'     .oNMMMk.                 {MAGENTA}|        
                  KMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMK                  {MAGENTA}| 
                  .MMMMMMMMMMMWWWWWWWWWWMMMMMMMMMMM.                  {MAGENTA}| 
                  {CYAN}======================{YELLOW}
                  ''')
    # More banner or further updates can go here as per your needs

def android_banner():
    """
    Displays a custom banner for Android.
    """
    # Define color codes
    RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW, YELLOW2, GREEN2, BRED = (
        '\033[91m', '\033[46m', '\033[36m', '\033[1;91m', '\033[0m',
        '\033[1;32m', '\033[1;93m', '\033[1;92m', "\033[5;35m"
    )
    BLINK, MAGENTA = "\033[5m", "\033[1;34m"
    y = '\033[1;33m'

    # Display banner text
    print(f'''
                                {YELLOW}...      
                           {YELLOW}.ckXWMMMMWKx:  
                         {YELLOW};0MMMWKOOOKWMMMWk'
                       {YELLOW}'KMMWd'       .oNMMMk.  
                      {YELLOW}lMM0d.  {CYAN}.:cllc,.  {YELLOW}cKWMN.  
                     {YELLOW}oMWc  {CYAN}'kWMMMMMMMMKl. {YELLOW}.XMW.  
                    {YELLOW};MW, {CYAN}.OMMMMMMMMMMMMMWd. {YELLOW}KMN   
                    {YELLOW}XM: {CYAN};NMMMMMMMMMMMMMMMMN;{YELLOW}.XMx 
                   {YELLOW};Mx {CYAN}lMMMMMMMMMMMMMMMMMMMM:{YELLOW}.WM.
                   {YELLOW}kN {CYAN}:MMMMMMMMMMMMMMMMMMMMMW'{YELLOW}lMo  
                   {YELLOW}kN {CYAN}:MMMMMMMMMMMMMMMMMMMMMW'{YELLOW}lMo  

                   {CYAN}GitHub Profile: {DEFAULT}https://github.com/LightYagami28                   
                   "Yes, I made this banner when I was 21"
                  ''')

def end():
    """
    Displays an end message.
    """
    RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW, YELLOW2, GREEN2 = (
        '\033[1;91m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m',
        '\033[1;33m', '\033[1;93m', '\033[1;92m'
    )
    blink = '\033[5m'

    # Print end message
    print(f'''
                                                                                           
                                       {CYAN}'cdxOOkdl,{DEFAULT}                                             {YELLOW}|                                            {WHITE}<Symbiote> BY: {CYAN}HASAN FIRNAS I
                                    {CYAN}.lKMMMMMMMMMMXd.{DEFAULT}                                          {YELLOW}|                                       
                                   {CYAN}lNMMMMMMMMMMNXXNNo{DEFAULT}                                         {YELLOW}|                      
                                 {CYAN}'0MMMMMMMNkl,..   .'.{DEFAULT}                                        {YELLOW}|                       
                                {CYAN}oWMMMMMMO;{DEFAULT}                                                    {YELLOW}|                      
                              {CYAN}.OMMMMMMK;{DEFAULT}                                                      {YELLOW}|                     
                             {CYAN}.0MMMMMWd{DEFAULT}                                                        {YELLOW}|                     
                  ''')
