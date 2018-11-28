from pymavlink import mavutil
import time

from tkinter import *


def GuiStartCMD():


	master = Tk()

	labl = Label(master, text = "Enter IP Address of server followed by port in the format: 000.000.000.000:0000 and then close window")
	labl.pack()

	e = Entry(master)
	e.pack()

	e.focus_set()

	ipAddr = ''

	def callback():
	    master.quit()

	b = Button(master, text="Change IP", width=10, command =callback)
	b.pack()

	mainloop()

	text = e.get()
	newIP = str(text)
	print ("ipaddr: ",newIP)
	return text

startGui = GuiStartCMD()
newdevice = mavutil.mavlink_connection(('tcp:'+startGui), planner_format=True, notimestamps=False, robust_parsing=True) 

lolWhile = 9

while (lolWhile >0):
	  time.sleep(0.0100)
	  data = str (newdevice.recv())
	  print(data)




