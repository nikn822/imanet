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
    ipAddr = e.get()
    master.quit()

b = Button(master, text="Change IP", width=10, command =callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()





newIP = chr ipAddr
print (ipAddr)

-----
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
    #ipAddr = str (e.get())
    ipAddr = '127.0.0.1:7850'
    master.quit()

b = Button(master, text="Change IP", width=10, command =callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()

-----
from tkinter import *

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





newIP = (ipAddr)
print (newIP)