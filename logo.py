#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

import random
import subprocess
import os
from time import sleep
from platform import architecture
from os import system
from Checks import *

def banner():
    """
    Displays a custom banner based on random selection.
    """
    # Color definitions
    colors = {
        'RED': '\033[91m',
        'WHITE': '\033[46m',
        'CYAN': '\033[36m',
        'GREEN': '\033[1;91m',
        'DEFAULT': '\033[0m',
        'YELLOW': '\033[1;32m',
        'YELLOW2': '\033[1;93m',
        'GREEN2': '\033[1;92m',
        'BRED': "\033[5;35m",
        'BLINK': "\033[5m",
        'MAGENTA': "\033[1;34m"
    }

    # Clear terminal
    system('clear')
    
    # Display banner text
    print(f'''
                                  {colors['YELLOW']}...
                             {colors['YELLOW']}.ckXWMMMMWKx:                        {colors['MAGENTA']}|    
                           {colors['YELLOW']};0MMMWKOOOKWMMMWk'                     {colors['MAGENTA']}|     
                         {colors['YELLOW']}'KMMWd'       .oNMMMk.                   {colors['MAGENTA']}|     
                        {colors['YELLOW']}lMM0d.  {colors['CYAN']}.:cllc,.  {colors['YELLOW']}cKWMN.                  {colors['MAGENTA']}|     
                       {colors['YELLOW']}oMWc  {colors['CYAN']}'kWMMMMMMMMKl. {colors['YELLOW']}.XMW.                 {colors['MAGENTA']}|    
                      {colors['YELLOW']};MW, {colors['CYAN']}.OMMMMMMMMMMMMMWd. {colors['YELLOW']}KMN                 {colors['MAGENTA']}|              
                      {colors['YELLOW']}XM: {colors['CYAN']};NMMMMMMMMMMMMMMMMN;{colors['YELLOW']}.XMx                {colors['MAGENTA']}|              {colors['GREEN']}░░░░░░░ ░░    ░░ ░░░    ░░░ ░░░░░░  ░░  ░░░░░░  ░░░░░░░░ ░░░░░░░{colors['CYAN']}  
                      {colors['YELLOW']}XM: {colors['CYAN']}.OMMMMMMMMMMMMMMMMMWd. {colors['YELLOW']}KMN                 {colors['MAGENTA']}| 
                    {colors['CYAN']}'kMMWd'     .oNMMMk.                 {colors['MAGENTA']}|        
                  KMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMK                  {colors['MAGENTA']}| 
                  .MMMMMMMMMMMWWWWWWWWWWMMMMMMMMMMM.                  {colors['MAGENTA']}| 
                  {colors['CYAN']}======================{colors['YELLOW']}
                  ''')

def android_banner():
    """
    Displays a custom banner for Android.
    """
    colors = {
        'RED': '\033[91m',
        'WHITE': '\033[46m',
        'CYAN': '\033[36m',
        'GREEN': '\033[1;91m',
        'DEFAULT': '\033[0m',
        'YELLOW': '\033[1;32m',
        'YELLOW2': '\033[1;93m',
        'GREEN2': '\033[1;92m',
        'BRED': "\033[5;35m",
        'BLINK': "\033[5m",
        'MAGENTA': "\033[1;34m"
    }

    # Display banner text
    print(f'''
                                {colors['YELLOW']}...
                           {colors['YELLOW']}.ckXWMMMMWKx:  
                         {colors['YELLOW']};0MMMWKOOOKWMMMWk'
                       {colors['YELLOW']}'KMMWd'       .oNMMMk.  
                      {colors['YELLOW']}lMM0d.  {colors['CYAN']}.:cllc,.  {colors['YELLOW']}cKWMN.  
                     {colors['YELLOW']}oMWc  {colors['CYAN']}'kWMMMMMMMMKl. {colors['YELLOW']}.XMW.  
                    {colors['YELLOW']};MW, {colors['CYAN']}.OMMMMMMMMMMMMMWd. {colors['YELLOW']}KMN   
                    {colors['YELLOW']}XM: {colors['CYAN']};NMMMMMMMMMMMMMMMMN;{colors['YELLOW']}.XMx 
                   {colors['YELLOW']};Mx {colors['CYAN']}lMMMMMMMMMMMMMMMMMMMM:{colors['YELLOW']}.WM.
                   {colors['YELLOW']}kN {colors['CYAN']}:MMMMMMMMMMMMMMMMMMMMMW'{colors['YELLOW']}lMo  
                   {colors['YELLOW']}kN {colors['CYAN']}:MMMMMMMMMMMMMMMMMMMMMW'{colors['YELLOW']}lMo  

                   {colors['CYAN']}GitHub Profile: {colors['DEFAULT']}https://github.com/LightYagami28                   
                   "Yes, I made this banner when I was 21"
                  ''')

def end():
    """
    Displays an end message.
    """
    colors = {
        'RED': '\033[1;91m',
        'WHITE': '\033[46m',
        'CYAN': '\033[1;36m',
        'GREEN': '\033[1;32m',
        'DEFAULT': '\033[0m',
        'YELLOW': '\033[1;33m',
        'YELLOW2': '\033[1;93m',
        'GREEN2': '\033[1;92m'
    }
    blink = '\033[5m'

    # Print end message
    print(f'''
                                                                                           
                                       {colors['CYAN']}'cdxOOkdl,{colors['DEFAULT']}                                             {colors['YELLOW']}|                                            {colors['WHITE']}<Symbiote> BY: {colors['CYAN']}HASAN FIRNAS I
                                    {colors['CYAN']}.lKMMMMMMMMMMXd.{colors['DEFAULT']}                                          {colors['YELLOW']}|                                       
                                   {colors['CYAN']}lNMMMMMMMMMMNXXNNo{colors['DEFAULT']}                                         {colors['YELLOW']}|                      
                                 {colors['CYAN']}'0MMMMMMMNkl,..   .'.{colors['DEFAULT']}                                        {colors['YELLOW']}|                       
                                {colors['CYAN']}oWMMMMMMO;{colors['DEFAULT']}                                                    {colors['YELLOW']}|                      
                              {colors['CYAN']}.OMMMMMMK;{colors['DEFAULT']}                                                      {colors['YELLOW']}|                     
                             {colors['CYAN']}.0MMMMMWd{colors['DEFAULT']}                                                        {colors['YELLOW']}|                     
                  ''')
