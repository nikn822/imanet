from __future__ import print_function

import time

from pymavlink import mavutil
from tkinter import *

master = Tk()
jeff = Label(master, text="First Name").grid(row=0)
riperino = Label(master, text="Last Name").grid(row=1)

e1 = Entry(master, textvariable=v)
e2 = Entry(master, textvariable=q)

s = v.get()
p = q.get()

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop( )

print(jeff)
print(riperino)



newdevice = mavutil.mavlink_connection('tcp:localhost:7850', planner_format=False, notimestamps=True, robust_parsing=True) 

lolWhile = 9

while (lolWhile >0):
	  data = newdevice.recv()
	  print(data)


