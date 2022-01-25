# 3D-surface-plot-Python

The n*m Z matrix can contain heights of water for example, to plot the submarine surface.
If you have any question, tell me!

## First setp

```py
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

```

<br>
<p align="center">
<img width="1329" alt="Capture d’écran 2022-01-25 à 13 46 08" src="https://user-images.githubusercontent.com/63207451/150979706-952eed20-cef5-46ce-aaf1-0c181ded5924.png">
<img width="1151" alt="Capture d’écran 2022-01-25 à 13 46 22" src="https://user-images.githubusercontent.com/63207451/150979750-7bf81912-58fc-4244-a0ff-345aef5cea04.png">
</p>

<p align="center">
<img width="1177" alt="interpolation_linéaire" src="https://user-images.githubusercontent.com/63207451/92334896-65152f00-f092-11ea-9b81-fd24accc9d89.png">
<img width="430" alt="Capture d’écran 2022-01-24 à 19 40 00" src="https://user-images.githubusercontent.com/63207451/150843835-5f25643b-f874-4226-8211-cfd418493179.png">
</p>

<br/>

<p align="center">
  <a href="https://github.com/antonin-lfv" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97302854-e484da80-1859-11eb-9374-5b319ca51197.png" title="GitHub" width="40" height="40"></a>
  <a href="https://www.linkedin.com/in/antonin-lefevre-565b8b141" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303444-b2c04380-185a-11eb-8cfc-864c33a64e4b.png" title="LinkedIn" width="40" height="40"></a>
  <a href="mailto:antoninlefevre45@icloud.com" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303543-cec3e500-185a-11eb-8adc-c1364e2054a9.png" title="Mail" width="40" height="40"></a>
</p>
