from __future__ import print_function

import time

from pymavlink import mavutil
from tkinter import *

root = Tk()
lab = Label(root, text="this is too easy")
lab.pack()
root.mainloop()



newdevice = mavutil.mavlink_connection('tcp:10.105.39.111:7850', planner_format=False, notimestamps=True, robust_parsing=True) 

lolWhile = 9

while (lolWhile >0):
	  data = newdevice.recv()
	  print(data)


