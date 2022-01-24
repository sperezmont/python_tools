'''
  Author: Sergio Pérez Montero
  Date: 2022.01.20
  Aim: Some functions for dealing with custom colormaps
'''


import numpy as np
import matplotlib.pyplot as plt


def mk_cmap(nportions, values, ncolors, mode='linear'):
    '''
    Generates a color map splitting the colorbar into 'nportions' with colors='values' with a lenght of ncolors
    >>> value   value   value   value ...  len(values)
    >>>   |portion|portion|portion|   ...  nportions
    >>> \n
    >>> nportions = len(values) - 1
    >>> values = [[red, green, blue],...] in percentage units
    >>> mode, gradation mode, default is 'linear'
    '''
    import numpy as np
    import matplotlib as mpl
    ncol_port = int(ncolors/nportions)
    cmap = []
    for i in range(nportions):
        jcmap = []
        for x in range(ncol_port):
            vals = []
            for j in range(3):
                ini, fin = values[i][j], values[i+1][j]
                if mode == 'linear':
                    vals.append((fin - ini) * x / ncol_port + ini)
            jcmap.append(vals)
        cmap.append(jcmap)
    cmap = np.array(cmap).reshape(nportions*ncol_port, 3)
    cmap = cmap * 255/100  # convert to rgb values
    cmap = mpl.colors.ListedColormap(cmap/255)  # transform to cmap
    return cmap


def list2list(pylist, slice_len):
    '''
    Transform pylist with 1 dimension to pylist_converted with dimensions (len(pylist), slice_len)
    '''
    import numpy as np
    pylist_converted = []
    k = 0
    for i in range(int(len(pylist)/slice_len)):
        temp_list = []
        for j in np.arange(k, k + slice_len, 1):
            temp_list.append(pylist[j])
        pylist_converted.append(temp_list)
        k = k + slice_len
    return pylist_converted


def Ccmap(C):
    '''
    Transforms C (numpy array, dimC = (longitude of colors, 3)) into a colormap
    '''
    import matplotlib as mpl
    cm = mpl.colors.ListedColormap(C/255)
    return cm
