import os
import sys
import numpy as np

import SimpleITK as sitk
import pyTEMlib
import pyTEMlib.file_tools as ft
import pyTEMlib.image_tools as it
from pyTEMlib.atom_tools import atom_refine
from pyTEMlib import graph_tools as gt
from pyTEMlib import crystal_tools as ct

from skimage.feature import blob_log
from scipy.spatial import KDTree
from scipy.signal import correlate
from scipy.signal import correlate2d
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans

from collections import defaultdict, deque

from scipy.spatial import Delaunay, Voronoi, ConvexHull, voronoi_plot_2d
from sklearn.mixture import GaussianMixture
from scipy.spatial import cKDTree

from matplotlib import cm
import matplotlib.patches as patches
import matplotlib as mpl

%matplotlib widget
import matplotlib.pyplot as plt
# %matplotlib ipympl
%load_ext autoreload
%autoreload 2