from __future__ import print_function

import time

from pymavlink import mavutil
from tkinter import *

def makeWin():
	root = Tk()
	lab = Label(root, text="this is too easy")
	root.mainloop()


#makeNewWindow = makeWin



newdevice = mavutil.mavlink_connection('tcp:10.0.2.15:7850', planner_format=False, notimestamps=True, robust_parsing=True) 

lolWhile = 9

while (lolWhile >0):
	  data = newdevice.recv()
	  print(data)

