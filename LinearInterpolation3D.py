""" 3D plot with matplotlib """
import numpy
from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
mpl.use('macosx')

class Interpolator():
    def __init__(self, matrix):
        self.matrix = matrix
        self.row_mat, self.col_mat = self.matrix.shape

    def __str__(self):
        return "This is an interpolator on a Matrix"

    def __repr__(self):
        return f"Interpolator({self.matrix})"

    def __zprime(self):
        l = []
        for j in reversed(range(self.col_mat)):
            for i in reversed(range(self.row_mat)):
                l.append((self.matrix[i])[j])
        return l

    def __data_array(self):
        c = []
        for i in range(self.row_mat):
            for j in range(self.col_mat):
                c.append(i)
                c.append(j)
                c.append(self.matrix[i][j])
        M = np.asarray(c)
        M = M.reshape((self.row_mat * self.col_mat, 3))
        return M

    def graph_3D_line(self):
        """ With lines """
        # create the 3D plot
        plt.rcParams['legend.fontsize'] = 10
        fig = plt.figure('Line plot')
        ax = fig.add_subplot(projection='3d')
        # data
        xp = [i for i in reversed(range(0, self.col_mat))]
        yl = [i for i in reversed(range(0, self.row_mat))]
        # make the plot
        for i in range(0, self.row_mat):
            yp = [i] * self.col_mat
            zi = self.matrix[i]
            for j in reversed(range(0, self.col_mat)):
                xl = [j] * self.row_mat
                ziprime = self.__zprime()[(j * self.row_mat):(j * self.row_mat + self.row_mat)]
                plt.plot(xp, yp, zi, 'blue', linewidth=1)
                plt.plot(xl, yl, ziprime, 'red', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim(0, self.col_mat)
        plt.ylim(0, self.row_mat)
        return fig

    def graph_3D_color(self):
        """ With Gradient color """
        fig = plt.figure('Gradient color')
        ax = fig.add_subplot(projection='3d')
        Xs = self.__data_array()[:, 0]
        Ys = self.__data_array()[:, 1]
        Zs = self.__data_array()[:, 2]
        surf = ax.plot_trisurf(Xs, Ys, Zs, cmap=cm.ocean, linewidths=1, edgecolor='none')
        fig.colorbar(surf)
        ax.xaxis.set_major_locator(MaxNLocator(5))
        ax.yaxis.set_major_locator(MaxNLocator(6))
        ax.zaxis.set_major_locator(MaxNLocator(5))
        fig.tight_layout()
        return fig
