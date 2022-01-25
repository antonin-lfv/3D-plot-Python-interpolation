## Usage example
import matplotlib.pyplot as plt

from Interpolation_3D.LinearInterpolation3D import *
import pandas as pd

if __name__ == "__main__":
    # Data 
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    
    mon_interpolateur = Interpolator(matrix=z_data.values)
    # With color gradient
    f1 = mon_interpolateur.graph_3D_color()
    # With lines
    f2 = mon_interpolateur.graph_3D_line()
    # Plot the 2 fig
    plt.show()
