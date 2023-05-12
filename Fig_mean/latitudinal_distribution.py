import xarray as xr
import matplotlib.pyplot as plt
import regionmask
import pandas as pd
from matplotlib.pyplot import MultipleLocator

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

my_base1 = (base.ensemble1 - 273.15).sel(time=slice('2011', '2030')).mean('time')
my_ctrl1 = (ctrl.ensemble1 - 273.15).mean('time')
my_glen1 = (glen.ensemble1 - 273.15).mean('time')
my_equa1 = (equa.ensemble1 - 273.15).mean('time')

my_base2 = (base.ensemble2 - 273.15).sel(time=slice('2011', '2030')).mean('time')
my_ctrl2 = (ctrl.ensemble2 - 273.15).mean('time')
my_glen2 = (glen.ensemble2 - 273.15).mean('time')
my_equa2 = (equa.ensemble2 - 273.15).mean('time')

my_base3 = (base.ensemble3 - 273.15).sel(time=slice('2011', '2030')).mean('time')
my_ctrl3 = (ctrl.ensemble3 - 273.15).mean('time')
my_glen3 = (glen.ensemble3 - 273.15).mean('time')
my_equa3 = (equa.ensemble3 - 273.15).mean('time')

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

# mask the ocean
lon = base_pc.lon
lat = base_pc.lat

mask = regionmask.defined_regions.natural_earth_v5_0_0.land_110.mask(lon, lat).values

base_t_land = np.where(pd.isna(mask), float('nan'), mean_base)
ctrl_t_land = np.where(pd.isna(mask), float('nan'), mean_ctrl)
glen_t_land = np.where(pd.isna(mask), float('nan'), mean_glen)
equa_t_land = np.where(pd.isna(mask), float('nan'), mean_equa)

base1_t_land = np.where(pd.isna(mask), float('nan'), my_base1)
ctrl1_t_land = np.where(pd.isna(mask), float('nan'), my_ctrl1)
glen1_t_land = np.where(pd.isna(mask), float('nan'), my_glen1)
equa1_t_land = np.where(pd.isna(mask), float('nan'), my_equa1)

base2_t_land = np.where(pd.isna(mask), float('nan'), my_base2)
ctrl2_t_land = np.where(pd.isna(mask), float('nan'), my_ctrl2)
glen2_t_land = np.where(pd.isna(mask), float('nan'), my_glen2)
equa2_t_land = np.where(pd.isna(mask), float('nan'), my_equa2)

base3_t_land = np.where(pd.isna(mask), float('nan'), my_base3)
ctrl3_t_land = np.where(pd.isna(mask), float('nan'), my_ctrl3)
glen3_t_land = np.where(pd.isna(mask), float('nan'), my_glen3)
equa3_t_land = np.where(pd.isna(mask), float('nan'), my_equa3)

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

base_pe1 = (base_pc.ensemble1.sel(time=slice('2011', '2030')).data * 1000 +
            base_pl.ensemble1.sel(time=slice('2011', '2030')).data * 1000 -
            base_q.ensemble1.sel(time=slice('2011', '2030')).data) * 3600 * 24
ctrl_pe1 = (ctrl_pc.ensemble1.data * 1000 + ctrl_pl.ensemble1.data * 1000 - ctrl_q.ensemble1.data) * 3600 * 24
glen_pe1 = (glen_pc.ensemble1.data * 1000 + glen_pl.ensemble1.data * 1000 - glen_q.ensemble1.data) * 3600 * 24
equa_pe1 = (equa_pc.ensemble1.data * 1000 + equa_pl.ensemble1.data * 1000 - equa_q.ensemble1.data) * 3600 * 24

base_pe2 = (base_pc.ensemble2.sel(time=slice('2011', '2030')).data * 1000 +
            base_pl.ensemble2.sel(time=slice('2011', '2030')).data * 1000 -
            base_q.ensemble2.sel(time=slice('2011', '2030')).data) * 3600 * 24
ctrl_pe2 = (ctrl_pc.ensemble2.data * 1000 + ctrl_pl.ensemble2.data * 1000 - ctrl_q.ensemble2.data) * 3600 * 24
glen_pe2 = (glen_pc.ensemble2.data * 1000 + glen_pl.ensemble2.data * 1000 - glen_q.ensemble2.data) * 3600 * 24
equa_pe2 = (equa_pc.ensemble2.data * 1000 + equa_pl.ensemble2.data * 1000 - equa_q.ensemble2.data) * 3600 * 24

base_pe3 = (base_pc.ensemble3.sel(time=slice('2011', '2030')).data * 1000 +
            base_pl.ensemble3.sel(time=slice('2011', '2030')).data * 1000 -
            base_q.ensemble3.sel(time=slice('2011', '2030')).data) * 3600 * 24
ctrl_pe3 = (ctrl_pc.ensemble3.data * 1000 + ctrl_pl.ensemble3.data * 1000 - ctrl_q.ensemble3.data) * 3600 * 24
glen_pe3 = (glen_pc.ensemble3.data * 1000 + glen_pl.ensemble3.data * 1000 - glen_q.ensemble3.data) * 3600 * 24
equa_pe3 = (equa_pc.ensemble3.data * 1000 + equa_pl.ensemble3.data * 1000 - equa_q.ensemble3.data) * 3600 * 24

# average along time axis
mean_base_pe = base_pe.mean(axis=0)
mean_ctrl_pe = ctrl_pe.mean(axis=0)
mean_glen_pe = glen_pe.mean(axis=0)
mean_equa_pe = equa_pe.mean(axis=0)

mean_base1_pe = base_pe1.mean(axis=0)
mean_ctrl1_pe = ctrl_pe1.mean(axis=0)
mean_glen1_pe = glen_pe1.mean(axis=0)
mean_equa1_pe = equa_pe1.mean(axis=0)

mean_base2_pe = base_pe2.mean(axis=0)
mean_ctrl2_pe = ctrl_pe2.mean(axis=0)
mean_glen2_pe = glen_pe2.mean(axis=0)
mean_equa2_pe = equa_pe2.mean(axis=0)

mean_base3_pe = base_pe3.mean(axis=0)
mean_ctrl3_pe = ctrl_pe3.mean(axis=0)
mean_glen3_pe = glen_pe3.mean(axis=0)
mean_equa3_pe = equa_pe3.mean(axis=0)

p1_ctrl = ctrl_t_land - base_t_land; p1_glen = glen_t_land - base_t_land; p1_equa = equa_t_land - base_t_land

p1_ctrl1 = ctrl1_t_land - base1_t_land; p1_glen1 = glen1_t_land - base1_t_land; p1_equa1 = equa1_t_land - base1_t_land
p1_ctrl2 = ctrl2_t_land - base2_t_land; p1_glen2 = glen2_t_land - base2_t_land; p1_equa2 = equa2_t_land - base2_t_land
p1_ctrl3 = ctrl3_t_land - base3_t_land; p1_glen3 = glen3_t_land - base3_t_land; p1_equa3 = equa3_t_land - base3_t_land

p2_ctrl = mean_ctrl_pe - mean_base_pe; p2_glen = mean_glen_pe - mean_base_pe; p2_equa = mean_equa_pe - mean_base_pe

p2_ctrl1 = mean_ctrl1_pe - mean_base1_pe; p2_glen1 = mean_glen1_pe - mean_base1_pe; p2_equa1 = mean_equa1_pe - mean_base1_pe
p2_ctrl2 = mean_ctrl2_pe - mean_base2_pe; p2_glen2 = mean_glen2_pe - mean_base2_pe; p2_equa2 = mean_equa2_pe - mean_base2_pe
p2_ctrl3 = mean_ctrl3_pe - mean_base3_pe; p2_glen3 = mean_glen3_pe - mean_base3_pe; p2_equa3 = mean_equa3_pe - mean_base3_pe


fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8.5, 4))
plt.subplots_adjust(wspace=0.30)
linewidth = 1.8
linewidth_sub = 0.8

# panel a: land temperature
axs[0].axhline(0, color='gray', zorder=1, linestyle='dashed')
axs[0].plot(lat, np.nanmean(p1_ctrl, axis=1), color='#AC2026', label='Control-Base', linewidth=linewidth)
axs[0].plot(lat, np.nanmean(p1_glen, axis=1), color='#BD8EC0', label='GLENS-Base', linewidth=linewidth)
axs[0].plot(lat, np.nanmean(p1_equa, axis=1), color='#6F80BE', label='GLENS_eq-Base', linewidth=linewidth)

axs[0].plot(lat, np.nanmean(p1_ctrl1, axis=1), color='#AC2026', linewidth=linewidth_sub, alpha=0.5)
axs[0].plot(lat, np.nanmean(p1_glen1, axis=1), color='#BD8EC0', linewidth=linewidth_sub, alpha=0.5)
axs[0].plot(lat, np.nanmean(p1_equa1, axis=1), color='#6F80BE', linewidth=linewidth_sub, alpha=0.5)

axs[0].plot(lat, np.nanmean(p1_ctrl2, axis=1), color='#AC2026', linewidth=linewidth_sub, alpha=0.5)
axs[0].plot(lat, np.nanmean(p1_glen2, axis=1), color='#BD8EC0', linewidth=linewidth_sub, alpha=0.5)
axs[0].plot(lat, np.nanmean(p1_equa2, axis=1), color='#6F80BE', linewidth=linewidth_sub, alpha=0.5)

axs[0].plot(lat, np.nanmean(p1_ctrl3, axis=1), color='#AC2026', linewidth=linewidth_sub, alpha=0.5)
axs[0].plot(lat, np.nanmean(p1_glen3, axis=1), color='#BD8EC0', linewidth=linewidth_sub, alpha=0.5)
axs[0].plot(lat, np.nanmean(p1_equa3, axis=1), color='#6F80BE', linewidth=linewidth_sub, alpha=0.5)

axs[0].set_ylabel("T on Land ($^{\circ}$C)")
axs[0].set_xlabel("Latitude")
axs[0].legend(bbox_to_anchor=[0.80, 0.72])
axs[0].set_xlim(-90, 90)
x_major_locator = MultipleLocator(30)
axs[0].xaxis.set_major_locator(x_major_locator)
axs[0].annotate('(a)', xy=(0.09, 0.91), fontsize=14, xycoords='axes fraction', horizontalalignment='center')

# panel b: land PE
axs[1].axhline(0, color='gray', zorder=1, linestyle='dashed')
axs[1].plot(lat, np.nanmean(p2_ctrl, axis=1), color='#AC2026', linewidth=linewidth)
axs[1].plot(lat, np.nanmean(p2_glen, axis=1), color='#BD8EC0', linewidth=linewidth)
axs[1].plot(lat, np.nanmean(p2_equa, axis=1), color='#6F80BE', linewidth=linewidth)

axs[1].plot(lat, np.nanmean(p2_ctrl1, axis=1), color='#AC2026', linewidth=linewidth_sub, alpha=0.5)
axs[1].plot(lat, np.nanmean(p2_glen1, axis=1), color='#BD8EC0', linewidth=linewidth_sub, alpha=0.5)
axs[1].plot(lat, np.nanmean(p2_equa1, axis=1), color='#6F80BE', linewidth=linewidth_sub, alpha=0.5)

axs[1].plot(lat, np.nanmean(p2_ctrl2, axis=1), color='#AC2026', linewidth=linewidth_sub, alpha=0.5)
axs[1].plot(lat, np.nanmean(p2_glen2, axis=1), color='#BD8EC0', linewidth=linewidth_sub, alpha=0.5)
axs[1].plot(lat, np.nanmean(p2_equa2, axis=1), color='#6F80BE', linewidth=linewidth_sub, alpha=0.5)

axs[1].plot(lat, np.nanmean(p2_ctrl3, axis=1), color='#AC2026', linewidth=linewidth_sub, alpha=0.5)
axs[1].plot(lat, np.nanmean(p2_glen3, axis=1), color='#BD8EC0', linewidth=linewidth_sub, alpha=0.5)
axs[1].plot(lat, np.nanmean(p2_equa3, axis=1), color='#6F80BE', linewidth=linewidth_sub, alpha=0.5)

axs[1].set_ylabel("PE on Land (mm/day)")
axs[1].set_xlabel("Latitude")
axs[1].set_xlim(-90, 90)
x_major_locator = MultipleLocator(30)
axs[1].xaxis.set_major_locator(x_major_locator)
axs[1].annotate('(b)', xy=(0.09, 0.91), fontsize=14, xycoords='axes fraction', horizontalalignment='center')
