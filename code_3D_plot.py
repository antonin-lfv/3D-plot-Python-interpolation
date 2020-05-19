""" 3D plot with matplotlib """

#import
from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
axes = plt.gca()

#shape of your numpy matrix Z : n*n  

#for z
n=len(list(Z))
    
def zprime():
    l=[]
    for j in reversed(range (n)):
        for i in reversed(range (n)):
                l.append((Z[i])[j])
    return l

#for x and y

def list_coord():
    return([i for i in reversed(range (0,n))])

#for x,y,z

def data_array(): 
    c = []
    for i in range (n):
        for j in range (n):
                c.append(i)
                c.append(j)
                c.append(Z[i][j])
    M = np.asarray(c)
    M = M.reshape((n*n,3))
    return(M)

#by linear interpolation

def graph_3D_line():
    #create the 3D plot
    plt.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #data
    xp = list_coord()
    yl = list_coord()
    #make the plot
    for i in range (0,n): 
        yp = [i for k in (range (0,n))]
        zi = Z[i] 
        for i in reversed(range(0,n)): 
            xl = [i for k in (range (0,n))]
            ziprime = zprime()[(i*n):(i*n+n)]
            plt.plot(xp, yp, zi,'blue')
            plt.plot(xl,yl, ziprime,'red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0,n)
    plt.ylim(0,n)
    plt.title("linear interpolation")
    plt.show()
    
    
#with colours

def graph_3D_color():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    Xs = data_array()[:,0]
    Ys = data_array()[:,1]
    Zs = data_array()[:,2]
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

Z= np.array([[7.894736842105264, 7.894736842105264, 7.894736842105264, 8.947368421052632, 8.947368421052632, 10.0, 10.0, 10.0, 10.0, 10.0], [6.842105263157896, 6.842105263157896, 7.894736842105264, 8.947368421052632, 8.947368421052632, 8.947368421052632, 10.0, 10.0, 10.0, 10.0], [5.789473684210527, 5.789473684210527, 5.789473684210527, 6.842105263157896, 6.842105263157896, 7.894736842105264, 8.947368421052632, 10.0, 10.0, 10.0], [5.789473684210527, 5.789473684210527, 5.789473684210527, 5.789473684210527, 5.789473684210527, 6.842105263157896, 6.842105263157896, 8.947368421052632, 10.0, 10.0], [3.6842105263157894, 4.736842105263158, 4.736842105263158, 5.789473684210527, 5.789473684210527, 5.789473684210527, 6.842105263157896, 7.894736842105264, 8.947368421052632, 10.0], [3.6842105263157894, 3.6842105263157894, 3.6842105263157894, 3.6842105263157894, 4.736842105263158, 5.789473684210527, 5.789473684210527, 6.842105263157896, 8.947368421052632, 8.947368421052632], [2.6315789473684212, 2.6315789473684212, 2.6315789473684212, 3.6842105263157894, 3.6842105263157894, 5.789473684210527, 5.789473684210527, 6.842105263157896, 8.947368421052632, 8.947368421052632], [1.5789473684210527, 1.5789473684210527, 2.6315789473684212, 2.6315789473684212, 3.6842105263157894, 4.736842105263158, 5.789473684210527, 5.789473684210527, 7.894736842105264, 7.894736842105264], [0.5263157894736843, 0.5263157894736843, 1.5789473684210527, 2.6315789473684212, 3.6842105263157894, 4.736842105263158, 5.789473684210527, 5.789473684210527, 6.842105263157896, 7.894736842105264], [-0.5263157894736843, 0.5263157894736843, 1.5789473684210527, 2.6315789473684212, 3.6842105263157894, 3.6842105263157894, 5.789473684210527, 5.789473684210527, 6.842105263157896, 7.894736842105264]])



 
 
