from my311 import abline,l,lo,r,hi,velocity_frac,gamma_f
import matplotlib.pyplot as plt
import numpy as np
from twin_util import parad_util,create_annotiation,unprime_time,unprime_state
from pylab import *
velocity_frac=0.8



def get_lines_of_one_system(paras_obj,col0 ):
    tprime= paras_obj.lor_trans(unprime_state,unprime_time)
    lt  =unprime_time/tprime
    ll =paras_obj.x_pos
    x_point =[ paras_obj.lor_xtrans(0,i)  for i in range(1,ll)]
    print (x_point)
    # x_point =[i for i in x_point if i<=ll]
    print (x_point)
    b_list =[paras_obj.calc_b(i) for i in x_point]
    mm=[]
    for b in b_list:
       x1,y1= abline(paras_obj.perp_slope,b,-2 ,6 )
       plt.plot(x1,y1,col0)
       mm.append((x1,y1,col0))
    return mm
def prime_2graph(fast_obj,slow_obj,lor_gline=True):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    a_val, b_val = abline(1, 0, -9, 9)
    c_val, d_val = abline(-1, 0, -9, 9)

    plt.plot(a_val,b_val,'y-')
    plt.plot(c_val,d_val,'y-')
    # xx= [i/1000 for i in range(4000)]
    # yy= [1/velocity_frac *i for i in xx]
    #
    plt.xlabel('X-space')
    plt.ylabel("CT")
    for i in range(1,int(ceil(unprime_time))):
      plt.hlines(y=i, xmin=-6 , xmax=6, colors='g'   )
    arrow( l-1, 0, r-l+2, 0, length_includes_head = True, head_width = 0.1 )
    arrow( 0, lo-1, 0, hi-lo+2, length_includes_head = True, head_width = 0.1 )

    m_fast =get_lines_of_one_system(fast_obj,'r-' )
    m_slow =get_lines_of_one_system(slow_obj,'m-' )
    # ax = create_annotiation(ax, 7, fast_obj)
    ax = create_annotiation(ax, 7, slow_obj)
    ax = create_annotiation(ax, 7, fast_obj)

    ax.set(xlim=(-8, 8), ylim=(-8, 12))

    plt.show()
    exit(45)


    # # x1,y1= abline(-0.8,25/3,-2 ,6 )
    # # plt.plot(x1,y1,'r-')
    # # x1, y1 = abline(-0.8, 41/15 , -2, 6)
    # # plt.plot(x1, y1, 'r-')
    # # x1, y1 = abline(-0.8, 82/15  , -2, 6)
    # # plt.plot(x1, y1, 'r-')
    #
    # # plt.vlines(x=0, ymin=0, ymax=25/3, colors='m')
    # x_values = [xun, xp ]
    # y_values = [yun, yp]
    # plt.plot(x_values, y_values, 'co', linestyle="--")
    # # plt.legend(['Light Speed', 'Light Speed', 'Space as persp Traveller', 'Prime time', 'Rest as obsereved  Frame'])
    # plt.plot(xp, yp, 'b*')
    #
    # plt.plot(xun  , yun, 'b*')
    #
    # arrow( l-1, 0, r-l+2, 0, length_includes_head = True, head_width = 0.1 )
    # arrow( 0, lo-1, 0, hi-lo+2, length_includes_head = True, head_width = 0.1 )
    # # ax.annotate('', xytext=(0, 0), xy=(7,35/4 ), arrowprops=dict(arrowstyle='->'))
    # # ax.annotate('', xytext=(0, 0), xy=(-7 , 7*0.8), arrowprops=dict(arrowstyle='->'))
    # # ax.annotate('', xytext=(0, 0), xy=(7, -7 * 0.8), arrowprops=dict(arrowstyle='->'))
    #
    # ax= create_annotiation(ax, 7, fast_obj)
    # ax = create_annotiation(ax, 7, slow_obj)
    # ax.set(xlim=(-8 ,8 ), ylim=(-8 , 12  ))
    #
    # # ax.annotate('a', xytext=(0, 0), xy=(7, 35 / 4), arrowprops=dict(arrowstyle='->'))
    # # ax.annotate('a', xytext=(0, 0), xy=(-7, 7 * 0.8), arrowprops=dict(arrowstyle='->'))
    # # ax.annotate('', xytext=(0, 0), xy=(7, -7 * 0.8), arrowprops=dict(arrowstyle='->'))
    # # ax.annotate('b', xytext=(0, 0), xy=(3, 3 / 0.3), arrowprops=dict(arrowstyle='->'))
    # # ax.annotate('b', xytext=(0, 0), xy=(-7, 7 * 0.3), arrowprops=dict(arrowstyle='->'))
    # # ax.annotate('', xytext=(0, 0), xy=(7, -7 * 0.3), arrowprops=dict(arrowstyle='->'))
    # #
    # # ax.set(xlim=(-8, 11), ylim=(-8, 12))
    #
    # plt.show()
    # return

if __name__ =='__main__':
    p_fast =parad_util(0.8)
    p_slow = parad_util(0.7)

    prime_2graph(p_fast,p_slow)
