import var_prop
import matplotlib.pyplot as plt
import matplotlib as mpl
from cartopy.util import add_cyclic_point
import numpy as np
import cartopy.crs as ccrs
import matplotlib.colors as colors


def label_latlon(ax, fontsize):
    gl = ax.gridlines(draw_labels=False, linestyle=":", linewidth=0.3, color='k')
    ax.annotate('60S', xy=(0.05, 0.126), fontsize=fontsize, horizontalalignment='center',
                verticalalignment='center', xycoords='axes fraction')
    ax.annotate('30S', xy=(-0.022, 0.31), fontsize=fontsize, horizontalalignment='center',
                verticalalignment='center', xycoords='axes fraction')
    ax.annotate('0', xy=(-0.024, 0.50), fontsize=fontsize, horizontalalignment='center', verticalalignment='center',
                xycoords='axes fraction')
    ax.annotate('30N', xy=(-0.022, 0.69), fontsize=fontsize, horizontalalignment='center',
                verticalalignment='center', xycoords='axes fraction')
    ax.annotate('60N', xy=(0.05, 0.874), fontsize=fontsize, horizontalalignment='center',
                verticalalignment='center', xycoords='axes fraction')
    ax.annotate('120W', xy=(0.30, -0.04), fontsize=fontsize, horizontalalignment='center',
                verticalalignment='center', xycoords='axes fraction')
    ax.annotate('60W', xy=(0.42, -0.04), fontsize=fontsize, horizontalalignment='center',
                verticalalignment='center', xycoords='axes fraction')
    ax.annotate('0', xy=(0.5, -0.04), fontsize=fontsize, horizontalalignment='center', verticalalignment='center',
                xycoords='axes fraction')
    ax.annotate('60E', xy=(0.58, -0.04), fontsize=fontsize, horizontalalignment='center',
                verticalalignment='center', xycoords='axes fraction')
    ax.annotate('120E', xy=(0.70, -0.04), fontsize=fontsize, horizontalalignment='center',
                verticalalignment='center', xycoords='axes fraction')
    return


# Create norm for colorbar, set zero value with white color in the middle
# Example:
###  fill_c = ax.contourf(lon, lat, var, norm=MidpointNormalize(midpoint=0.), extend='both')
###  cbar = plt.colorbar(fill_c, pad=0.05, orientation='horizontal')
class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # make color distributed evenly according to the original colormap
        if self.vmax >= -self.vmin:
            x, y = [self.vmin, self.midpoint, self.vmax], [0.5 + self.vmin / self.vmax / 2, 0.5, 1]
        else:
            x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 0.5 - self.vmax / self.vmin / 2]
        return np.ma.masked_array(np.interp(value, x, y))