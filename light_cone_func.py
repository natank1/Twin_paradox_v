from twin_util import abline,lo,hi,r,l,arrow_style
import matplotlib.pyplot as plt
import numpy as np
def plot_light_cones(terimaite=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    a_val, b_val = abline(1, 0, -8, 8)
    c_val, d_val = abline(-1, 0, -8, 8)
    plt.plot(a_val, b_val, 'y-')
    plt.plot(c_val, d_val, 'y-')
    plt.xlabel('X-space')
    plt.ylabel("CT")
    plt.arrow( l-1, 0, r-l+2, 0, length_includes_head = True, head_width = 0.2 )
    plt.arrow( 0, lo-1, 0, hi-lo+2, length_includes_head = True, head_width = 0.2 )
    # plt.arrow(l - 1, 0, r - l + 2, 0, **arrow_style)
    # plt.annotate('X-space',
    #              xy=(1 / 2, 1 / 2),
    #              xytext=(10, -10),
    #              textcoords='offset points')
    # plt.arrow(0, lo - 1, 0, hi - lo + 2, **arrow_style)
    # plt.annotate('CT',
    #              xy=(1 / 2, 1 / 2),
    #              xytext=(10, -10),
    #              textcoords='offset points')


    if terimaite:
        plt.legend(['Light Cone', 'Light Cone'])
        plt.show()
        return


    x=np
    x = np.arange(-8.0, 8, 0.01)
    y1 = abs(x)
    y2 = 8
    ax.fill_between(x=x,y1=y1,y2=y2)
    ax.fill_between(x=x, y1=-y1, y2=-y2,color='r')
    # plt.legend(['Light Cone', 'Light Cone','Future','Past'])
    # ax.fill_between(x=a_val, y1=np.array([d_val[0], 0]))



    # ax2.fill_between(x, y1, 1)
    # ax2.set_ylabel('between y1 and 1')
    plt.show()
    return
if __name__=='__main__':
    # plot_light_cones(terimaite=True)
    plot_light_cones()
