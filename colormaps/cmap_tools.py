'''
  Author: Sergio Pérez Montero
  Date: 2022.01.20
  Aim: Some functions for dealing with custom colormaps
'''

def mk_cmap(nportions, values, ncolors, mode='linear', deg=2):
    '''
    Generates a color map splitting the colorbar into 'nportions' with colors='values' with a lenght of ncolors
    >>> nportions = len(values) - 1
    >>> ncolors > nportions
    >>> values = [[red, green, blue],...] in percentage units
    >>> mode, gradation mode, default is 'linear', 'power'
    >>> default power mode is 2 --> ax**2 + bx + c
    '''
    import numpy as np
    import matplotlib as mpl

    if nportions > len(values)-1:
        raise ValueError('nportions must be equal to len(values) - 1')

    if ncolors < nportions:
        raise ValueError('ncolors must be >= nportions')

    ncol_port = int(ncolors/nportions)
    cmap = []
    for i in range(nportions):
        jcmap = []
        for x in range(ncol_port):
            vals = []
            for j in range(3):
                ini, fin = values[i][j], values[i+1][j]
                if ini == fin:
                    vals.append(np.array(ini))
                elif mode == 'linear':
                    vals.append((fin - ini) * x / ncol_port + ini)
                elif mode == 'power':
                    xpoints = np.arange(0, ncol_port*(1+1/deg), ncol_port/deg)
                    ypoints = np.arange(
                        ini, fin + (fin-ini)/(len(xpoints)-1), (fin-ini)/(len(xpoints)-1))
                    coef = np.polyfit(xpoints, ypoints, deg)
                    term = 0
                    for p in range(0, deg+1):
                        term = term + coef[p]*x**(deg-p)
                    vals.append(term)
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
