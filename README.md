# 3D-surface-plot-Python

The <b>n*m</b> Z matrix can contain heights of water for example, to plot the submarine surface.
If you have any question, tell me!

## First setp

```py
from Interpolation_3D.LinearInterpolation3D import *
import pandas as pd

if __name__ == "__main__":
    mon_interpolateur = Interpolator(matrix=z_data)
    # With color gradient (unique plot)
    f1 = mon_interpolateur.graph_3D_color(display=False)  # display=True to juste plot this figure

    # With lines (unique plot)
    f2 = mon_interpolateur.graph_3D_line(display=False)

    # Subplot with gradient and lines
    mon_interpolateur.subplot_line_gradient()

```

<br>
<p align="center">
![Capture d’écran 2022-01-26 à 00 53 57](https://user-images.githubusercontent.com/63207451/151079703-79e25144-c0bf-47fc-8bd5-fb2c6c142062.png)
</p>

<br/>

<p align="center">
  <a href="https://github.com/antonin-lfv" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97302854-e484da80-1859-11eb-9374-5b319ca51197.png" title="GitHub" width="40" height="40"></a>
  <a href="https://www.linkedin.com/in/antonin-lefevre-565b8b141" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303444-b2c04380-185a-11eb-8cfc-864c33a64e4b.png" title="LinkedIn" width="40" height="40"></a>
  <a href="mailto:antoninlefevre45@icloud.com" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303543-cec3e500-185a-11eb-8adc-c1364e2054a9.png" title="Mail" width="40" height="40"></a>
</p>
