import matplotlib.pyplot as plt
import numpy as np

def my_plotter(ax, data1, data2, param_dict):
  """
  A helper function to make a graph

  Parameters
  ------------
  ax: Axes
    The axes to draw to

  data1: array
    The x data

  data2: array
    The y data

  param_dict: dict
    Dictionary of kwargs to pass to ax.plot

  Returns
  ------------
  out: list
    list of artist added
  """
  out = ax.plot(data1, data2, **param_dict)
  return out


data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

plt.show()
