import math
from bokeh.plotting import ColumnDataSource
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show
import numpy as np

from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider
from bokeh.plotting import ColumnDataSource, figure, show
e=[]
u=[]
HIGH=[]

max=500   #20 #wartosc maksymalna
min=5 #wartosc minimalna
ho=0    #poziom poczatkowy substancji
h0=4 # poziom poczatkowy substancji

t=[0]

FIELD_A=5   #50
Hz=300   #5 #float(input( "podaj wysokosc zadaną:"))
Tp=   0.1  #float(input("podaj okres probkowania:"))  tp=0.5
b=0.1 #wspólczynnik wyplywu b=0.35    # 0.025
kp=3    #1.15 # kp=10
ti=4     #0.25   # ti=50   czas zdwojenia    n_i*Tp
td=0.01

Ts= 100 #float(input( "podaj czas symulacji:"))
qd=0.05 # natezenie dopływu

HIGH.append(float(ho))
N=range(int(Ts/Tp))
for n in N:
    e.append(Hz-HIGH[n]) #uchyb regulacji
    u.append(kp * (e[n] + (Tp / ti) * sum(e) + (td / ti) * (e[n] - e[n - 1])))      #napięcie  #ti(HIGH[n]*tp)
    if(u[n]<0 or u[n]>10):
        u[n]>10.0
    else:
         u[n]>0.0
    qd=u[n]*b   #natęzenie dopływu
    qo=b*math.sqrt(HIGH[n])  #nateżenie odpływu
    HIGH.append((1 / FIELD_A) * (qd-qo) * Tp + HIGH[n])

x = N
y = HIGH
source = ColumnDataSource(data=dict(x=x, y=y))
plot = figure(y_range=(0, 10), plot_width=600, plot_height=600)

output_file("automatyka.html")
curdoc().theme = 'dark_minimal'
p = figure(title='Automatyka', plot_width=800, plot_height=800)
p.line(x, HIGH)
show(p)
