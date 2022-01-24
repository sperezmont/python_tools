'''
  Author: Sergio Pérez Montero
  Date: 2022.01.20
  Aim: Some functions for dealing with custom colormaps
'''


def list2list(pylist, slice_len):
  '''
  Transform pylist with 1 dimension to pylist_converted with dimensions (len(pylist), slice_len)
  '''
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
  cm = mpl.colors.ListedColormap(C/255)
  return cm
