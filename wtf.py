# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:13:02 2015

@author: rafael
"""

from pylab import*
t = 0.0
dt =0.01
x = 10.0 
v = 0.0 
k = 10.0 
m = 2.0 
tm=[]
vel =[]
dis = []
while t < 5:
    f = -k*x 
    v = v+(f/m)*dt
    x= x+v*dt
    t= t+dt
    tm.append(t)
    vel.append(v)
    dis.append(x)
    plot(tm,vel)
    plot(tm,dis)
    show()
    