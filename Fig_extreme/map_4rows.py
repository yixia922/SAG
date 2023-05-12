import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point
import matplotlib.colors as colors

import sys
sys.path.append("../Functions/")
import draw_map; import var_prop;


def map_singlerow(axs, var, lat, lon, row_order, index):
    # plot setting
    for col in range(3):
        ax = axs[row_order, col]
        ax.set_global();
        ax.coastlines(color='grey')
        draw_map.label_latlon(ax, 12)  # second_input: fontsize of lon&lat label
        # cycle in longitude, to erease the gap line
        cycle_var, cycle_lon = add_cyclic_point(var[col], coord=lon)
        cycle_LON, cycle_LAT = np.meshgrid(cycle_lon, lat)
        fill_c = ax.contourf(cycle_LON, cycle_LAT, cycle_var,
                             levels=get_colorbar_level(index),
                             cmap=var_prop.get_cmap(index), norm=draw_map.MidpointNormalize(midpoint=0.),
                             transform=ccrs.PlateCarree(central_longitude=0), extend='both')
        #         cbar = plt.colorbar(fill_c, pad=0.05, orientation='horizontal',
        #                             # fraction=0.05, shrink=1.6,
        #                            )
        if col == 0:
            cax = ax.inset_axes([0.6, -0.2, 2.2, 0.09])
            cbar = plt.colorbar(fill_c, orientation='horizontal', cax=cax,
                                pad=0.1)
            cbar.ax.tick_params(labelsize=12)
    return


def get_colorbar_level(var):
    if var in ['TNn', 'TXn']:
        levels = np.linspace(-2, 15, 35)
    elif var in ['TNx', 'TXx']:
        levels = np.linspace(-4, 8, 25)
    elif var in ['FD', 'ID']:
        levels = np.linspace(-100, 30, 27)
    elif var in ['TR', 'SU']:
        levels = np.linspace(-40, 100, 29)
    elif var == 'PRCPTOT':
        levels = np.linspace(-650, 650, 27)
    elif var == 'SDII':
        levels = np.linspace(-1.7, 1.7, 35)
    elif var == 'Rx1day':
        levels = np.linspace(-30, 30, 31)
    elif var == 'Rx5day':
        levels = np.linspace(-50, 50, 26)
    elif var in ['TN10p', 'TX10p']:
        levels = np.linspace(-50, 60, 23)
    elif var in ['TN90p', 'TX90p']:
        levels = np.linspace(-20, 300, 33)
    return levels


### INPORT DATA selection
# row1: 'TNn', 'TXn', 'TNx', 'TXx'
# row2: 'FD', 'ID', 'TR', 'SU'
# row3: 'PRCPTOT', 'SDII', 'Rx1day', 'Rx5day'  # delete 'SDII'&'Rx5day' for similiar characteristics
# row4: 'TN10p', 'TN90p', 'TX10p', 'TX90p'
row_var = ['TN10p', 'TX10p', 'TN90p', 'TX90p']

r1base = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.base.nc" % row_var[0])
r1ctrl = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.end.nc" % row_var[0])
r1glen = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.end.nc" % row_var[0])
r1eq = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.eq.end.nc" % row_var[0])

r2base = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.base.nc" % row_var[1])
r2ctrl = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.end.nc" % row_var[1])
r2glen = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.end.nc" % row_var[1])
r2eq = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.eq.end.nc" % row_var[1])

r3base = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.base.nc" % row_var[2])
r3ctrl = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.end.nc" % row_var[2])
r3glen = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.end.nc" % row_var[2])
r3eq = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.eq.end.nc" % row_var[2])

r4base = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.base.nc" % row_var[3])
r4ctrl = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.end.nc" % row_var[3])
r4glen = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.end.nc" % row_var[3])
r4eq = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.eq.end.nc" % row_var[3])

### GET DATA FOR MAPS
# latitude & longitude
lat = r1base.lat
lon = r1base.lon

# columns: Control-base(c1), GLENS-base(c2), EQ-base(c3)
r1c1 = np.mean(r1ctrl.ensemble_avg.data - r1base.ensemble_avg.data, axis=0)
r1c2 = np.mean(r1glen.ensemble_avg.data - r1base.ensemble_avg.data, axis=0)
r1c3 = np.mean(r1eq.ensemble_avg.data - r1base.ensemble_avg.data, axis=0)

r2c1 = np.mean(r2ctrl.ensemble_avg.data - r2base.ensemble_avg.data, axis=0)
r2c2 = np.mean(r2glen.ensemble_avg.data - r2base.ensemble_avg.data, axis=0)
r2c3 = np.mean(r2eq.ensemble_avg.data - r2base.ensemble_avg.data, axis=0)

r3c1 = np.mean(r3ctrl.ensemble_avg.data - r3base.ensemble_avg.data, axis=0)
r3c2 = np.mean(r3glen.ensemble_avg.data - r3base.ensemble_avg.data, axis=0)
r3c3 = np.mean(r3eq.ensemble_avg.data - r3base.ensemble_avg.data, axis=0)

r4c1 = np.mean(r4ctrl.ensemble_avg.data - r4base.ensemble_avg.data, axis=0)
r4c2 = np.mean(r4glen.ensemble_avg.data - r4base.ensemble_avg.data, axis=0)
r4c3 = np.mean(r4eq.ensemble_avg.data - r4base.ensemble_avg.data, axis=0)

var_matrix = [[r1c1, r1c2, r1c3],
              [r2c1, r2c2, r2c3],
              [r3c1, r3c2, r3c3],
              [r4c1, r4c2, r4c3], ]

# clear storage
del r1base, r1ctrl, r1glen, r1eq
del r2base, r2ctrl, r2glen, r2eq
del r3base, r3ctrl, r3glen, r3eq
del r4base, r4ctrl, r4glen, r4eq

# draw the figures
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(22, 16),
                        subplot_kw=dict(projection=ccrs.Robinson(central_longitude=0)))
plt.subplots_adjust(hspace=0.35, wspace=0.02)

for row in range(4):
    map_singlerow(axs, var_matrix[row][:], lat, lon, row, row_var[row])
    axs[row, 0].annotate('%s %s' % (row_var[row], var_prop.get_unit(row_var[row])),
                         xy=(-0.15, 0.5), xycoords='axes fraction', fontsize=20,
                         rotation=90, ha='center', va='center')

# subtitle (weight='bold')
axs[0, 0].annotate('Control - Base', xy=(0.5, 1.1), xycoords='axes fraction', fontsize=20,
                   horizontalalignment='center', verticalalignment='bottom')
axs[0, 1].annotate('GLENS - Base', xy=(0.5, 1.1), xycoords='axes fraction', fontsize=20,
                   horizontalalignment='center', verticalalignment='bottom')
axs[0, 2].annotate('GLENS_eq - Base', xy=(0.5, 1.1), xycoords='axes fraction', fontsize=20,
                   horizontalalignment='center', verticalalignment='bottom')
