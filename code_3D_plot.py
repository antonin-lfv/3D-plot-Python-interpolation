""" 3D plot with matplotlib """

#import
from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
axes = plt.gca()

#size of your matrix data Z : n*n   with the heights
#you have to extract the x,y,z data in 3 lists

#for z

def list_z_n(n):
    c=[]
    for i in range (n):
        for j in range (n):
            c.append(Z[i][j])
    M = np.asarray(c)
    return M.reshape((n,n))
    
def zprime_n(n):
    l=[]
    for j in reversed(range (n)):
        for i in reversed(range (n)):
                l.append((list_z_n(n)[i])[j])
    return l

#for x

def list_x_n(n):
    c = [i for i in reversed(range (0,n))]
    return c

#for y

def list_y_n(n):
    c = [i for i in reversed(range (0,n))]
    return c

#for the three

def data_array_n(n): 
    c = []
    for i in range (n):
        for j in range (n):
                c.append(i)
                c.append(j)
                c.append(list_z_n(n)[i][j])
    M = np.asarray(c)
    M = M.reshape((n*n,3))
    return(M)

#by linear interpolation

def graph_3D_n(n):
    #create the 3D plot
    plt.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #data
    xp = list_x_n(n)
    yl = list_y_n(n)
    #make the plot
    for i in range (0,n): 
        yp = [i for k in (range (0,n))]
        zi = list_z_n(n)[i] 
        for i in reversed(range(0,n)): 
            xl = [i for k in (range (0,n))]
            ziprime = zprime_n(n)[(i*n):(i*n+n)]
            plt.plot(xp, yp, zi,'blue')
            plt.plot(xl,yl, ziprime,'red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0,n)
    plt.ylim(0,n)
    plt.title("linear interpolation")
    plt.show()
    
    
#with colours

def gr_3D_color_n(n):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    Xs = data_array_n(n)[:,0]
    Ys = data_array_n(n)[:,1]
    Zs = data_array_n(n)[:,2]
    surf = ax.plot_trisurf(Xs, Ys, Zs, cmap=cm.jet, linewidths=1)
    #cmap='viridis', edgecolor='none')
    fig.colorbar(surf)
    ax.xaxis.set_major_locator(MaxNLocator(5))    
    ax.yaxis.set_major_locator(MaxNLocator(6))    
    ax.zaxis.set_major_locator(MaxNLocator(5))
    fig.tight_layout()  
    ax.set_title('linear interpolation') 
    plt.show()
    
    
#Z example:

Z=[[0, 0, 0, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 4, 4, 5, 4, 4, 4, 4, 3, 3, 2, 2],
 [0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 5, 5, 5, 6, 5, 5, 5, 4, 4, 3, 3, 3],
 [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 4, 4, 3, 3],
 [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 4, 4, 3],
 [2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4],
 [2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 4],
 [2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 8, 7, 7, 7, 7, 7, 6, 5, 5, 4],
 [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6, 5, 5],
 [3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 6, 5],
 [3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10, 10, 9, 8, 8, 7, 7, 7, 7, 6, 6, 6, 5]]   
 
 
