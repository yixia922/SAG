import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point
import matplotlib.colors as colors

import sys

sys.path.append("../Functions/")
import draw_map


def map_singlerow_t(axs, var, col):
    ax = axs[0, col]
    ax.set_global()
    ax.coastlines(color='grey')
    draw_map.label_latlon(ax, 12)  # second_input: fontsize of lon&lat label
    # cycle in longitude, to erease the gap line
    cycle_var, cycle_lon = add_cyclic_point(var, coord=var.lon)
    cycle_LON, cycle_LAT = np.meshgrid(cycle_lon, var.lat)
    fill_c = ax.contourf(cycle_LON, cycle_LAT, cycle_var,
                         levels=np.linspace(-2, 8, 21),
                         norm=draw_map.MidpointNormalize(midpoint=0.),
                         cmap='RdBu_r', extend='both',
                         transform=ccrs.PlateCarree(central_longitude=0))
    #     cbar = plt.colorbar(fill_c, pad=0.05, orientation='horizontal',
    #                         # fraction=0.05, shrink=1.6,
    #                         )
    if col == 0:
        cax = ax.inset_axes([0.62, -0.2, 2, 0.09])
        cbar = plt.colorbar(fill_c, orientation='horizontal', cax=cax,
                            pad=0.1)
        cbar.ax.tick_params(labelsize=12)
    return


def map_singlerow_pe(axs, var, lon, lat, col):
    ax = axs[1, col]
    ax.set_global()
    ax.coastlines(color='grey')
    draw_map.label_latlon(ax, 12)  # second_input: fontsize of lon&lat label
    # cycle in longitude, to erease the gap line
    cycle_var, cycle_lon = add_cyclic_point(var, coord=lon)
    cycle_LON, cycle_LAT = np.meshgrid(cycle_lon, lat)
    fill_c = ax.contourf(cycle_LON, cycle_LAT, cycle_var,
                         levels=np.linspace(-2, 2, 17),
                         norm=draw_map.MidpointNormalize(midpoint=0.),
                         cmap='BrBG',
                         extend='both',
                         transform=ccrs.PlateCarree(central_longitude=0))
    #     cbar = plt.colorbar(fill_c, pad=0.05, orientation='horizontal',
    #                         # fraction=0.05, shrink=1.6,
    #                         )
    if col == 0:
        cax = ax.inset_axes([0.62, -0.2, 2, 0.09])
        cbar = plt.colorbar(fill_c, orientation='horizontal', cax=cax,
                            pad=0.1)
        cbar.ax.tick_params(labelsize=12)
    return


var = 'TREFHT'

base = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.control.base.ensemble01-20.nc" % var)
ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.control.end.ensemble01-03.nc" % var)
glen = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.feedback.end.ensemble01-03.nc" % var)
equa = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.feedback.eq.end.ensemble01-03.nc" % var)

# calculate ensemble average
# mask year 2010 cause monthly data on 2010-01 is missing in the base exp.
my_base = ((base.ensemble1 + base.ensemble2 + base.ensemble3 + base.ensemble4 + base.ensemble5 +
            base.ensemble6 + base.ensemble7 + base.ensemble8 + base.ensemble9 + base.ensemble10 +
            base.ensemble11 + base.ensemble12 + base.ensemble13 + base.ensemble14 + base.ensemble15 +
            base.ensemble16 + base.ensemble17 + base.ensemble18 + base.ensemble19 + base.ensemble20) / 20 - 273.15).sel(
    time=slice('2011', '2030'))
my_ctrl = (ctrl.ensemble1 + ctrl.ensemble2 + ctrl.ensemble3) / 3 - 273.15  # convert the unit to celsius
my_glen = (glen.ensemble1 + glen.ensemble2 + glen.ensemble3) / 3 - 273.15
my_equa = (equa.ensemble1 + equa.ensemble2 + equa.ensemble3) / 3 - 273.15

# average along time axis
mean_base = my_base.mean('time')
mean_ctrl = my_ctrl.mean('time')
mean_glen = my_glen.mean('time')
mean_equa = my_equa.mean('time')

var1 = 'PRECC'
var2 = 'PRECL'
var3 = 'QSOIL'

base_pc = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.control.base.ensemble01-20.nc" % var1)
ctrl_pc = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.control.end.ensemble01-03.nc" % var1)
glen_pc = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.feedback.end.ensemble01-03.nc" % var1)
equa_pc = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.feedback.eq.end.ensemble01-03.nc" % var1)

base_pl = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.control.base.ensemble01-20.nc" % var2)
ctrl_pl = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.control.end.ensemble01-03.nc" % var2)
glen_pl = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.feedback.end.ensemble01-03.nc" % var2)
equa_pl = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.feedback.eq.end.ensemble01-03.nc" % var2)

base_q = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.control.base.ensemble01-20.nc" % var3)
ctrl_q = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.control.end.ensemble01-03.nc" % var3)
glen_q = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.feedback.end.ensemble01-03.nc" % var3)
equa_q = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/monthly/%s.feedback.eq.end.ensemble01-03.nc" % var3)

# calculate ensemble average
my_base_pl = ((base_pl.ensemble1 + base_pl.ensemble2 + base_pl.ensemble3 + base_pl.ensemble4 + base_pl.ensemble5 +
               base_pl.ensemble6 + base_pl.ensemble7 + base_pl.ensemble8 + base_pl.ensemble9 + base_pl.ensemble10 +
               base_pl.ensemble11 + base_pl.ensemble12 + base_pl.ensemble13 + base_pl.ensemble14 + base_pl.ensemble15 +
               base_pl.ensemble16 + base_pl.ensemble17 + base_pl.ensemble18 + base_pl.ensemble19 + base_pl.ensemble20) / 20).sel(
    time=slice('2011', '2030'))
my_ctrl_pl = (ctrl_pl.ensemble1 + ctrl_pl.ensemble2 + ctrl_pl.ensemble3) / 3
my_glen_pl = (glen_pl.ensemble1 + glen_pl.ensemble2 + glen_pl.ensemble3) / 3
my_equa_pl = (equa_pl.ensemble1 + equa_pl.ensemble2 + equa_pl.ensemble3) / 3

my_base_pc = ((base_pc.ensemble1 + base_pc.ensemble2 + base_pc.ensemble3 + base_pc.ensemble4 + base_pc.ensemble5 +
               base_pc.ensemble6 + base_pc.ensemble7 + base_pc.ensemble8 + base_pc.ensemble9 + base_pc.ensemble10 +
               base_pc.ensemble11 + base_pc.ensemble12 + base_pc.ensemble13 + base_pc.ensemble14 + base_pc.ensemble15 +
               base_pc.ensemble16 + base_pc.ensemble17 + base_pc.ensemble18 + base_pc.ensemble19 + base_pc.ensemble20) / 20).sel(
    time=slice('2011', '2030'))
my_ctrl_pc = (ctrl_pc.ensemble1 + ctrl_pc.ensemble2 + ctrl_pc.ensemble3) / 3
my_glen_pc = (glen_pc.ensemble1 + glen_pc.ensemble2 + glen_pc.ensemble3) / 3
my_equa_pc = (equa_pc.ensemble1 + equa_pc.ensemble2 + equa_pc.ensemble3) / 3

my_base_q = ((base_q.ensemble1 + base_q.ensemble2 + base_q.ensemble3 + base_q.ensemble4 + base_q.ensemble5 +
              base_q.ensemble6 + base_q.ensemble7 + base_q.ensemble8 + base_q.ensemble9 + base_q.ensemble10 +
              base_q.ensemble11 + base_q.ensemble12 + base_q.ensemble13 + base_q.ensemble14 + base_q.ensemble15 +
              base_q.ensemble16 + base_q.ensemble17 + base_q.ensemble18 + base_q.ensemble19 + base_q.ensemble20) / 20).sel(
    time=slice('2011', '2030'))
my_ctrl_q = (ctrl_q.ensemble1 + ctrl_q.ensemble2 + ctrl_q.ensemble3) / 3
my_glen_q = (glen_q.ensemble1 + glen_q.ensemble2 + glen_q.ensemble3) / 3
my_equa_q = (equa_q.ensemble1 + equa_q.ensemble2 + equa_q.ensemble3) / 3

# calculate PE: PE = PRECC(m/s) + PRECL(m/s) - QSOIL(mm/s)
# unify the unit to be (mm/day)
base_pe = (my_base_pc.data * 1000 + my_base_pl.data * 1000 - my_base_q.data) * 3600 * 24
ctrl_pe = (my_ctrl_pc.data * 1000 + my_ctrl_pl.data * 1000 - my_ctrl_q.data) * 3600 * 24
glen_pe = (my_glen_pc.data * 1000 + my_glen_pl.data * 1000 - my_glen_q.data) * 3600 * 24
equa_pe = (my_equa_pc.data * 1000 + my_equa_pl.data * 1000 - my_equa_q.data) * 3600 * 24

# average along time axis
mean_base_pe = base_pe.mean(axis=0)
mean_ctrl_pe = ctrl_pe.mean(axis=0)
mean_glen_pe = glen_pe.mean(axis=0)
mean_equa_pe = equa_pe.mean(axis=0)

# draw the figures
lon = base_pc.lon
lat = base_pc.lat
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(22, 8),
                        subplot_kw=dict(projection=ccrs.Robinson(central_longitude=0)))
plt.subplots_adjust(hspace=0.35, wspace=0.02)

map_singlerow_t(axs, mean_ctrl - mean_base, 0)
map_singlerow_t(axs, mean_glen - mean_base, 1)
map_singlerow_t(axs, mean_equa - mean_base, 2)

map_singlerow_pe(axs, mean_ctrl_pe - mean_base_pe, lon, lat, 0)
map_singlerow_pe(axs, mean_glen_pe - mean_base_pe, lon, lat, 1)
map_singlerow_pe(axs, mean_equa_pe - mean_base_pe, lon, lat, 2)

# subtitle (weight='bold')
axs[0, 0].annotate('Control - Base', xy=(0.5, 1.1), xycoords='axes fraction', fontsize=20,
                   horizontalalignment='center', verticalalignment='bottom')
axs[0, 1].annotate('GLENS - Base', xy=(0.5, 1.1), xycoords='axes fraction', fontsize=20,
                   horizontalalignment='center', verticalalignment='bottom')
axs[0, 2].annotate('GLENS_eq - Base', xy=(0.5, 1.1), xycoords='axes fraction', fontsize=20,
                   horizontalalignment='center', verticalalignment='bottom')

axs[0, 0].annotate('T ($^{\circ}$C)', xy=(-0.15, 0.5), xycoords='axes fraction', fontsize=20,
                   rotation=90, ha='center', va='center')
axs[1, 0].annotate('PE (mm/day)', xy=(-0.15, 0.5), xycoords='axes fraction', fontsize=20,
                   rotation=90, ha='center', va='center')

label = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']
label_location = [0.0, 0.96]
for i in range(2):
    for j in range(3):
        axs[i, j].annotate(label[i * 3 + j], xy=label_location, xycoords='axes fraction', fontsize=18)
