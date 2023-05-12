import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point
import matplotlib.colors as colors
import pandas as pd
import regionmask

import sys

sys.path.append("../Functions/")
import draw_map; import var_prop


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
            cax = ax.inset_axes([0.62, -0.2, 2, 0.09])
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
        levels = np.linspace(-90, 30, 25)
    elif var in ['TR', 'SU']:
        levels = np.linspace(-38, 78, 30)
    elif var == 'SDII':
        levels = np.linspace(-1.7, 1.7, 35)
    elif var == 'Rx1day':
        levels = np.linspace(-30, 30, 31)
    elif var == 'Rx5day':
        levels = np.linspace(-50, 50, 21)
    elif var in ['TN10p', 'TX10p']:
        levels = np.linspace(-14, 16, 16)
    elif var in ['TN90p', 'TX90p']:
        levels = np.linspace(-5, 80, 18)
    elif var == 'PRCPTOT':
        levels = np.linspace(-650, 700, 28)
    elif var == 'CDD':
        levels = np.linspace(-60, 60, 25)
    elif var == 'CWD':
        levels = np.linspace(-15, 20, 36)
    elif var == 'R10mm':
        levels = np.linspace(-30, 30, 31)
    elif var == 'R20mm':
        levels = np.linspace(-15.5, 15.5, 32)
    elif var == 'R95pTOT':
        levels = np.linspace(-400, 500, 19)
    elif var == 'R99pTOT':
        levels = np.linspace(-200, 200, 21)
    return levels


### INPORT DATA selection
# row1: 'TNn', 'TXx'
# row2: 'PRCPTOT', 'Rx5day'
# row3: 'FD', 'SU'
# row4: 'R10mm', 'R20mm'
# row5: 'TN10p', 'TX90p'
# row6: 'R95pTOT', 'R99pTOT'
# row7: 'CDD', 'CWD'

row_var = ['CDD', 'CWD']

r1base = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.base.nc" % row_var[0])
r1ctrl = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.end.nc" % row_var[0])
r1glen = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.end.nc" % row_var[0])
r1eq = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.eq.end.nc" % row_var[0])

r2base = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.base.nc" % row_var[1])
r2ctrl = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.control.end.nc" % row_var[1])
r2glen = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.end.nc" % row_var[1])
r2eq = xr.open_dataset("/Volumes/XY_disk1/GLENS_data/Results/%s.feedback.eq.end.nc" % row_var[1])

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

var_matrix = [[r1c1, r1c2, r1c3],
              [r2c1, r2c2, r2c3], ]

# clear storage
del r1base, r1glen, r1eq
del r2base, r2glen, r2eq

if row_var[0] in ['FD', 'R10mm']:
    # mask the ocean
    mask = regionmask.defined_regions.natural_earth_v5_0_0.land_110.mask(lon, lat).values
    for i in range(2):
        for j in range(3):
            var_matrix[i][j] = np.where(pd.isna(mask), float('nan'), var_matrix[i][j])

if row_var[0] == 'TN10p':
    # change days to percentage
    for i in range(2):
        for j in range(3):
            var_matrix[i][j] = var_matrix[i][j] / 3.65

# draw the figures
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(22, 8),
                        subplot_kw=dict(projection=ccrs.Robinson(central_longitude=0)))
plt.subplots_adjust(hspace=0.35, wspace=0.02)

for row in range(2):
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

label = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']
label_location = [0.0, 0.96]
for i in range(2):
    for j in range(3):
        axs[i, j].annotate(label[i * 3 + j], xy=label_location, xycoords='axes fraction', fontsize=18)
