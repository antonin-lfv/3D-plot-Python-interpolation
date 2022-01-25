""" 3D plot with plotly """
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
from plotly.subplots import make_subplots


class Interpolator:
    def __init__(self, matrix):
        if isinstance(matrix, pd.DataFrame):
            self.matrix = matrix.values
        else:
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

    def graph_3D_line(self, display=True):
        """ With lines """
        # create the 3D plot
        fig = go.Figure()
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
                fig.add_scatter3d(x=xp, y=yp, z=zi, line=dict(width=1, color='blue'), mode='lines', showlegend=False)
                fig.add_scatter3d(x=xl, y=yl, z=ziprime, line=dict(width=1, color='red'), mode='lines',
                                  showlegend=False)
        if display:
            plot(fig)
        else:
            return fig

    def graph_3D_color(self, display=True):
        """ With Gradient color """
        fig = go.Figure()
        fig.add_surface(z=self.matrix, colorscale='earth')
        fig.update_traces(contours_z=dict(show=True,
                                          usecolormap=True,
                                          highlightcolor="limegreen",
                                          project_z=True))
        fig.update_layout(
            template='simple_white',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
        )
        if display:
            plot(fig)
        else:
            return fig

    def subplot_line_gradient(self):
        """ Both gradient and lines """
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{"type": "surface"}, {"type": "surface"}]],
            subplot_titles=['Linear interpolation', 'Gradient surface plot']
        )

        # data first plot
        xp = [i for i in reversed(range(0, self.col_mat))]
        yl = [i for i in reversed(range(0, self.row_mat))]
        # make the plot
        for i in range(0, self.row_mat):
            yp = [i] * self.col_mat
            zi = self.matrix[i]
            for j in reversed(range(0, self.col_mat)):
                xl = [j] * self.row_mat
                ziprime = self.__zprime()[(j * self.row_mat):(j * self.row_mat + self.row_mat)]
                fig.add_scatter3d(x=xp, y=yp, z=zi, line=dict(width=1, color='blue'), mode='lines', showlegend=False, row=1, col=1)
                fig.add_scatter3d(x=xl, y=yl, z=ziprime, line=dict(width=1, color='red'), mode='lines',
                                  showlegend=False, row=1, col=1)

        fig.add_surface(z=self.matrix, colorscale='earth', showscale=False, row=1, col=2)
        fig.update_traces(contours_z=dict(show=True,
                                          usecolormap=True,
                                          highlightcolor="limegreen",
                                          project_z=True), row=1, col=2)
        fig.update_layout(
            template='simple_white',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
        )
        plot(fig)
