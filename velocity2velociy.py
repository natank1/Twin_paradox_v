
from twin_util import velocity_y_frac ,abline,l,lo,r,hi
import matplotlib.pyplot as plt
import numpy as np
from pylab import *


def v2v(xun,yun,xp,yp,v2):
    gamma2 = 1 / sqrt((1 - v2 * v2))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    a_val, b_val = abline(1, 0, -9, 9)
    c_val, d_val = abline(-1, 0, -9, 9)

    plt.plot(a_val,b_val,'y-')
    plt.plot(c_val,d_val,'y-')


    plt.plot(3,3/velocity_y_frac   , 'b*')
    plt.plot(5., 5/velocity_y_frac, 'r*')
    plt.plot(0.41, 0.41/v2, 'k*')
    plt.plot(1.2 , 1.2 / v2, 'c*')
    plt.legend(['Light Speed', 'Light Speed', 'Big speed sees itself'
                   ,'Big speed is seen','Small speed sees itself',"Small speed is seen" ],loc='upper left',prop={'size':5})



    # arrow( l-1, 0, r-l+2, 0, length_includes_head = True, head_width = 0.1 )
    # arrow( 0, lo-1, 0, hi-lo+2, length_includes_head = True, head_width = 0.1 )
    ax.annotate('a', xytext=(0, 0), xy=(7,35/4 ), arrowprops=dict(arrowstyle='->'))
    ax.annotate('a', xytext=(0, 0), xy=(-7 , 7*0.8), arrowprops=dict(arrowstyle='->'))
    ax.annotate('', xytext=(0, 0), xy=(7, -7 * 0.8), arrowprops=dict(arrowstyle='->'))
    ax.annotate('b', xytext=(0, 0), xy=(3, 3/0.3 ), arrowprops=dict(arrowstyle='->'))
    ax.annotate('b', xytext=(0, 0), xy=(-7, 7 * 0.3), arrowprops=dict(arrowstyle='->'))
    ax.annotate('', xytext=(0, 0), xy=(7, -7 * 0.3), arrowprops=dict(arrowstyle='->'))
    plt.xlabel('X-space')
    plt.ylabel("CT")

    ax.set(xlim=(-8,11 ), ylim=(-8 , 12 ))

    plt.show()
    return
if __name__=='__main__':
    v2v(4,5,0,8,v2=0.3)
