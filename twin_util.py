import math
import matplotlib.pyplot as plt
import numpy as np
unprime_time = 5
unprime_state =3.999
velocity_y_frac=0.8
# printing factors
l=-12
r=12
lo=-12
hi=12

arrow_style = {
    "head_width": 0.1,
    "head_length": 0.2,
    "color":"k"
}

def abline(slope, intercept,xst,xend):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    # mm=axes.get_xlim()
    x_vals = np.array((xst,xend ))

    # x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    return x_vals,y_vals


class parad_util:
    def __init__(self,velocity_frac):
        self.veloc= velocity_frac
        self.gamma_factor= 1/math.sqrt(1-self.veloc*self.veloc)
        self.get_slopes()
        self.x_pos =int(math.ceil(unprime_state))
    def get_slopes(self):
        self.slope= 1/self.veloc
        self.perp_slope = -1/self.slope

    def calc_b(self,time_elpase):
       return time_elpase*(self.slope-self.perp_slope)

    def lor_trans(self,x, t):
        tprime = self.gamma_factor  * (t * (1 - self.veloc  * self.veloc))
        return tprime
    def lor_xtrans(self,x, t):
        xprime = self.gamma_factor  * (x  + self.veloc * t)
        return xprime


def create_annotiation(ax,x_coor,fast_ob):
    ax.annotate('a', xytext=(0, 0), xy=(x_coor, x_coor*fast_ob.slope), arrowprops=dict(arrowstyle='->'))
    ax.annotate('a', xytext=(0, 0), xy=(-x_coor, -x_coor * fast_ob.perp_slope), arrowprops=dict(arrowstyle='->'))
    ax.annotate('', xytext=(0, 0), xy=(x_coor, x_coor*fast_ob.perp_slope), arrowprops=dict(arrowstyle='->'))
    return ax

    ax.set(xlim=(-8, 11), ylim=(-8, 12))
    # return ax