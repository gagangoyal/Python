#!/usr/bin/python2

import socket as s
import thread as th
import time as t

v=s.socket(s.AF_INET, s.SOCK_DGRAM)
ip='127.0.0.1'
#ip=raw_input("Enter IP")
port_no=8000

#Binding of ip and port no.
v.bind((ip,port_no))

#Sender function
def snd():
	msg=raw_input("enter a messege")
	#send a messege
	v.sendto(msg,(ip,9000))


#reciever function
def rec():
	data=v.recvfrom(1000)
	print data[0]
	
th.start_new_thread(rec,())
th.start_new_thread(snd,())

while True:
	pass
