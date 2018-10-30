from __future__ import print_function

import time

from pymavlink import mavutil

newdevice = mavutil.mavlink_connection('tcp:localhost:7850', planner_format=True, notimestamps=False, robust_parsing=True) 

lolWhile = 9

while (lolWhile >0):
	  data = newdevice.recv()
	  print(data)


