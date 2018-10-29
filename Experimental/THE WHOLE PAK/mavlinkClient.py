from __future__ import print_function

import time

from pymavlink import mavutil


newdevice = mavutil.mavlink_connection('tcp:localhost:8080', planner_format=False, notimestamps=True, robust_parsing=True) 

lolWhile = 9

while (lolWhile >0):
	  data = newdevice.recv()
	  print(data)
