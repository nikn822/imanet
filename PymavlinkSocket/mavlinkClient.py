from __future__ import print_function

import time

from pymavlink import mavutil
import tkinter

from tkinter import *

import matplotlib

import matplotlib.pyplot as plt

import matplotlib.animation as animation
from matplotlib import style

ct = 0
lolWhile = 9
datNum = 0



def GuiStartCMD():

	global Tk

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

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	xs = []
	ys = []
	for line in lines:
		if len(line) > 1:
			x, y = line.split(',')
			xs.append(float(x))
			ys.append(float(y))


	if (lolWhile >0):
		global data,ct
		dat =  (newdevice.recv())
		ct += 1

		try:
			data = int(dat)
			xs.append(float(ct))
			ys.append(float(data))
		except ValueError:
			xs.append(float(ct))
			ys.append(float(0))


	ax1.clear()
	ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
	



