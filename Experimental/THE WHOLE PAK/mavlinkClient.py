from __future__ import print_function

import time

from pymavlink import mavutil

from tkinter import *

master = Tk()

labl = Label(master, text = "Enter IP Address of server followed by port in the format: 000.000.000.000:0000 and then close window")
labl.pack()

e = Entry(master)
e.pack()

e.focus_set()

ipAddr = ''

def callback():
    print (e.get())
    ipAddr == e.get()
    master.quit()

b = Button(master, text="Change IP", width=10, command =callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()





newIP = (ipAddr)
print (newIP)

newdevice = mavutil.mavlink_connection(ipAddr, planner_format=True, notimestamps=False, robust_parsing=True) 

lolWhile = 9

while (lolWhile >0):
	  data = newdevice.recv()
	  print(data)


