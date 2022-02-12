## Usage example
from LinearInterpolation3D import *
import pandas as pd

if __name__ == "__main__":
    # Data 
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    
    mon_interpolateur = Interpolator(matrix=z_data)
    # With color gradient (unique plot)
    f1 = mon_interpolateur.graph_3D_color(display=False)  # display=True to juste plot this figure

    # With lines (unique plot)
    f2 = mon_interpolateur.graph_3D_line(display=False)

    # Subplot with gradient and lines
    mon_interpolateur.subplot_line_gradient()
