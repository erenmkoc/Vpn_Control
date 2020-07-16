#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install ike-scan")
os.system("clear")
os.system("figlet Vpn Control")

print("************")
print ("Maker by ....")
print("************")

print( "Vpn Control" )

hedefip = raw_input("Enter the target ip : ")

os.system("ike-scan " + hedefip)
print("Transaction completed successfully...")



