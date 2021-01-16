import matplotlib.pyplot as plt
import numpy as np
import pandas

# to convert a pandas.DataFrame
a = pandas.DataFrame(np.random.rand(4, 5), columns=list('abcde'))
a_asarray = a.values
print(a_asarray)

b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)
print(b_asarray)
