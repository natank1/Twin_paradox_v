from my311 import abline,l,lo,r,hi,velocity_frac,gamma
# import matplotlib.pyplot as plt
# import numpy as np
from pylab import *

def prime_graph(xun,yun,xp,yp, velocity_frac,lor_gline=True):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    a_val, b_val = abline(1, 0, -9, 9)
    c_val, d_val = abline(-1, 0, -9, 9)

    plt.plot(a_val,b_val,'y-')
    plt.plot(c_val,d_val,'y-')
    xx= [i/1000 for i in range(4000)]
    yy= [1/velocity_frac *i for i in xx]

    plt.plot(xx,yy,'r*')
    # plt.hlines(y=5, xmin=0, xmax=4, colors='b', linestyles='dotted')
    plt.vlines(x=0, ymin=0, ymax=25/3, colors='m')
    x_values = [xun, xp ]
    y_values = [yun, yp]
    plt.plot(x_values, y_values, 'co', linestyle="--")
    plt.legend(['Light Speed', 'Light Speed', 'Travellers perspective', 'Prime time', 'Rest frame as seen from Trav'],loc='upper left',prop={'size':6})
    plt.plot(xp, yp, 'b*')

    plt.plot(xun  , yun, 'b*')

    arrow( l-1, 0, r-l+2, 0, length_includes_head = True, head_width = 0.1 )
    arrow( 0, lo-1, 0, hi-lo+2, length_includes_head = True, head_width = 0.1 )
    ax.annotate('', xytext=(0, 0), xy=(7,35/4 ), arrowprops=dict(arrowstyle='->'))
    ax.annotate('', xytext=(0, 0), xy=(-7 , 7*0.8), arrowprops=dict(arrowstyle='->'))
    ax.annotate('', xytext=(0, 0), xy=(7, -7 * 0.8), arrowprops=dict(arrowstyle='->'))
    plt.xlabel('X-space')
    plt.ylabel("CT")
    ax.set(xlim=(-8 ,8 ), ylim=(-8 , 9 ))

    plt.show()
    return

if __name__ =='__main__':
    velocity_frac = 0.5

    prime_graph(4,5,0,8,0.8)
