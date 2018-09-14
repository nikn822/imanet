from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import Figure

import csv
import pandas as pd

#with open('data.csv', 'r') as csvfile:
#     csv_reader = csv.reader(csvfile)

#     for line in csv_reader:
#	print(line)

import numpy as np
import socket 
import ast 

with open('imu.csv', 'w') as fp:
	hello = csv.writer(fp, delimiter=',')

s = socket.socket()
port = 8080 
s.connect(('127.0.0.1', port))   

df = pd.read_csv('data.csv')

source = ColumnDataSource(dict(s=[], y=[], x=[], z=[]))

#Choose Modes Carefully
#source = ColumnDataSource(dict(s=[], y=[], x=[]))
#source = ColumnDataSource(dict(s=[], y=[]))
#source = ColumnDataSource(dict(s=[], x=[]))
#source = ColumnDataSource(dict(s=[], z=[]))

x = Figure(width=1000, height=300, title='x')
x.line(source=source, x='s', y='x', line_width=2, alpha= .85, color= 'purple')


y = Figure(width=1000, height=300, title='y')
y.line(source=source, x='s', y='y', line_width=2, alpha= .85, color= 'green')


z = Figure(width=1000, height=300, title='z')
z.line(source=source, x='s', y='z', line_width=2, alpha= .85, color= 'blue')


sine_sum = 0
ct = 0

def update_data():
        global ct,sine_sum
        ct += 1
        sine=np.sin((ct*3.1415*100)/180)

	jiff = ast.literal_eval(s.recv(1024))

	dog = dict(jiff)
	nom = dog['x']
	print(nom)
	mol = dog['y']
	print(mol)
	pop = dog['z']
	print(pop)
	data = [nom, mol, pop]
	hello.writerows(data)
	hello.next()



	#Choose Modes Carefully
	new_data = dict(s=[ct],y=[nom], x=[mol],z=[pop])
	#new_data = dict(s=[ct],y=[nom], x=[mol])
	#new_data = dict(s=[ct],x=[mol])
	#new_data = dict(s=[ct],y=[nom])
	#new_data = dict(s=[ct],z=[pop])
        source.stream(new_data,100)

curdoc().add_root(y)
curdoc().add_root(x)
curdoc().add_root(z)
curdoc().add_periodic_callback(update_data, 100)


 
