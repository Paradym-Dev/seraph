import os
import sys
import time
import requests
import random
import ctypes
from pystyle import Colorate, Colors, Write, Add, Center
import urllib.request

class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.warn()
        time.sleep(2)
        self.cls()
        self.banner()
        self.options()
        while self.gg == True:
            print()
            choose = input(str('             Choose Number:  '))
            if (choose == '1'):
                self.cls()
                self.banner()
                self.rs()
            elif (choose == '2'):
                self.cls()
                self.banner()
                self.zp()
            



    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
        
    def warn(self):
        Banner1= """
           _   _   _   _   _   _     _   _   _   _   _     _   _   _   _   _   _   _  
          / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
         ( S | e | r | a | p | h ) ( G | r | o | u | p ) ( T | o | o | l | b | o | x )
          \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
                                                                    By Paradym 
              ==================================================================
              + Please use this tool on a debian based system for best results +
              ==================================================================                
        """
        Banner2 = """
              """
        print(Center.XCenter(Colorate.Vertical(Colors.red_to_yellow, Add.Add(Banner1,Banner2, center=True), 2)))
 
    def banner(self):
        Banner1= """
           _   _   _   _   _   _     _   _   _   _   _     _   _   _   _   _   _   _  
          / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
         ( S | e | r | a | p | h ) ( G | r | o | u | p ) ( T | o | o | l | b | o | x )
          \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
                                                                    By Paradym 
                              
        """
        Banner2 = """
              """
        print(Center.XCenter(Colorate.Vertical(Colors.red_to_blue, Add.Add(Banner1,Banner2, center=True), 2)))
    
    
    def options(self):
        Banner1 ="""            [1]  RouterSploit (WIFI Exploitation)
            [2]  ZPhisher (Phishing Tool)
            [3]  MetaSploit (Hacking Framework)
            [4]  MITM(MITM Attack)
            [5]  (WebSite Attack)
            [6]  (Android Exploitation)
            [7]  (Payload Creation)
            [8]  (SQL Injection)
            [9]  (Remote Administration Tool)
            [10]  (Anon Web Surfing)
            [11]  (WebSite Attack)
            [12]  (WebSite Attack)"""
        Banner2 = """
              """
        print(Colorate.Vertical(Colors.red_to_blue, Add.Add(Banner1,Banner2, center=True), 2))
               
    
    def irtb(self):
        Banner1 = """            [1] Install
            [2] Run
            [3] Tool Page
            [99] Back"""
        Banner2 = """
              """
        print(Colorate.Vertical(Colors.red_to_blue, Add.Add(Banner1,Banner2, center=True), 2))
        
        
    def rs(self):
        self.irtb()
        while self.gg == True:
            print('')
            choose = input(str('            Choose Number:  '))
            if (choose == '1'):
               self.clear()
               self.banner() 
               os.system('sudo git clone https://github.com/threat9/routersploit.git:/home/seraph/Tools .')           
               os.system('cd routersploit && sudo python3 -m pip install -r requirements.txt')
               self.rs()
            elif (choose == '2'):
               os.system('cd Tools && cd routersploit && sudo python3 rsf.py')
            elif (choose == '3'):
               urllib.request.urlopen('https://github.com/threat9/routersploit')
            elif (choose == '99'):
               self.cls()
               self.banner()
               self.options()
       
    def zp(self):
        self.irtb()
        while self.gg == True:
            print('')
            choose = input(str('            Choose Number:  '))
            if (choose == '1'):
               self.clear()
               self.start_logo() 
               os.system('sudo git clone https://github.com/threat9/routersploit.git://Tools')           
               os.system('cd routersploit && sudo python3 -m pip install -r requirements.txt')
               self.rs()
            elif (choose == '2'):
               os.system('cd Tools && cd routersploit && sudo python3 rsf.py')
            elif (choose == '3'):
               os.system('cd Tools && cd routersploit && sudo python3 rsf.py')
            elif (choose == '99'):
               self.cls()
               self.banner()
               self.options()

Main()
