from twin_util import abline,lo,hi,r,l,velocity_y_frac,unprime_time,unprime_state
import matplotlib.pyplot as plt
import numpy as np
from math import ceil
def unprime_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    a_val, b_val = abline(1, 0, -8, 8)
    c_val, d_val = abline(-1, 0, -8, 8)
    plt.plot(a_val, b_val, 'y-')
    plt.plot(c_val, d_val, 'y-')
    plt.xlabel('X-space')
    plt.ylabel("CT")
    plt.vlines(x=0, ymin=0, ymax=unprime_time, colors='m')

    m000 =1000*int(ceil(unprime_state))
    xx = [i / 1000 for i in range(m000)]
    yy = [1/velocity_y_frac * i for i in xx]

    plt.plot(xx, yy, 'r-')
    plt.hlines(y=unprime_time, xmin=0, xmax=unprime_state, colors='b', linestyles='dotted')
    x_values = [4, 0 ]
    y_values = [5, 3]
    plt.plot(x_values, y_values, 'co', linestyle="--")
    plt.plot(0, 3, 'b*')
    plt.arrow(l - 1, 0, r - l + 2, 0, length_includes_head=True, head_width=0.2)
    plt.arrow(0, lo - 1, 0, hi - lo + 2, length_includes_head=True, head_width=0.2)

    plt.legend(['Light Cone', 'Light Cone', 'Unprime axis',"traveler seen from earth","time line","Lorentz tr"],loc="upper left" ,prop={'size':8})
    plt.show()
    return
if __name__=='__main__':
    # plot_light_cones(terimaite=True)
    unprime_plot()



