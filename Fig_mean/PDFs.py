import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter
import regionmask
import pandas as pd


var_name = 'PRECT'      # options: TREFHT/PRECT
exp_name = 'control'

# Ensemble 001
data1_1_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.201001-201912.nc"%(exp_name,var_name,exp_name,var_name))
data1_2_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.202001-202912.nc"%(exp_name,var_name,exp_name,var_name))
data1_3_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.203001-203912.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 002
data2_1_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.201001-201912.nc"%(exp_name,var_name,exp_name,var_name))
data2_2_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.202001-202912.nc"%(exp_name,var_name,exp_name,var_name))
data2_3_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.203001-203912.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 003
data3_1_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.201001-201912.nc"%(exp_name,var_name,exp_name,var_name))
data3_2_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.202001-202912.nc"%(exp_name,var_name,exp_name,var_name))
data3_3_base = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.203001-203912.nc"%(exp_name,var_name,exp_name,var_name))

data1_base = xr.merge([data1_1_base, data1_2_base, data1_3_base])[var_name].sel(time=slice('2010', '2030')) * 24 * 3600 * 1000
data2_base = xr.merge([data2_1_base, data2_2_base, data2_3_base])[var_name].sel(time=slice('2010', '2030')) * 24 * 3600 * 1000
data3_base = xr.merge([data3_1_base, data3_2_base, data3_3_base])[var_name].sel(time=slice('2010', '2030')) * 24 * 3600 * 1000

del data1_1_base, data1_2_base, data1_3_base
del data2_1_base, data2_2_base, data2_3_base
del data3_1_base, data3_2_base, data3_3_base


exp_name = 'control'

# Ensemble 001
data1_1_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data1_2_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data1_3_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.209001-209906.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 002
data2_1_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data2_2_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data2_3_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.209001-209807.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 003
data3_1_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data3_2_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data3_3_ctrl = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.209001-209912.nc"%(exp_name,var_name,exp_name,var_name))

data1_ctrl = xr.merge([data1_1_ctrl, data1_2_ctrl, data1_3_ctrl])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000
data2_ctrl = xr.merge([data2_1_ctrl, data2_2_ctrl, data2_3_ctrl])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000
data3_ctrl = xr.merge([data3_1_ctrl, data3_2_ctrl, data3_3_ctrl])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000

del data1_1_ctrl, data1_2_ctrl, data1_3_ctrl
del data2_1_ctrl, data2_2_ctrl, data2_3_ctrl
del data3_1_ctrl, data3_2_ctrl, data3_3_ctrl


exp_name = 'feedback'

# Ensemble 001
data1_1_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data1_2_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data1_3_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.209001-209912.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 002
data2_1_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data2_2_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data2_3_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.209001-209912.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 003
data3_1_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data3_2_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data3_3_glen = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.209001-209912.nc"%(exp_name,var_name,exp_name,var_name))

data1_glen = xr.merge([data1_1_glen, data1_2_glen, data1_3_glen])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000
data2_glen = xr.merge([data2_1_glen, data2_2_glen, data2_3_glen])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000
data3_glen = xr.merge([data3_1_glen, data3_2_glen, data3_3_glen])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000

del data1_1_glen, data1_2_glen, data1_3_glen
del data2_1_glen, data2_2_glen, data2_3_glen
del data3_1_glen, data3_2_glen, data3_3_glen


exp_name = 'feedback.eq'

# Ensemble 001
data1_1_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data1_2_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data1_3_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h0.%s.209001-209912.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 002
data2_1_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data2_2_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data2_3_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h0.%s.209001-209912.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 003
data3_1_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.207001-207912.nc"%(exp_name,var_name,exp_name,var_name))
data3_2_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.208001-208912.nc"%(exp_name,var_name,exp_name,var_name))
data3_3_equa = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/monthly/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h0.%s.209001-209912.nc"%(exp_name,var_name,exp_name,var_name))

data1_equa = xr.merge([data1_1_equa, data1_2_equa, data1_3_equa])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000
data2_equa = xr.merge([data2_1_equa, data2_2_equa, data2_3_equa])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000
data3_equa = xr.merge([data3_1_equa, data3_2_equa, data3_3_equa])[var_name].sel(time=slice('2075', '2095')) * 24 * 3600 * 1000

del data1_1_equa, data1_2_equa, data1_3_equa
del data2_1_equa, data2_2_equa, data2_3_equa
del data3_1_equa, data3_2_equa, data3_3_equa


monthly1 = data1_base.groupby("time.month").mean(skipna=True)
monthly2 = data2_base.groupby("time.month").mean(skipna=True)
monthly3 = data3_base.groupby("time.month").mean(skipna=True)
std1 = data1_base.groupby("time.month").std()
std2 = data2_base.groupby("time.month").std()
std3 = data3_base.groupby("time.month").std()


pdf1_ctrl = np.zeros((12*21, 192, 288))
pdf2_ctrl = np.zeros((12*21, 192, 288))
pdf3_ctrl = np.zeros((12*21, 192, 288))
pdf1_glen = np.zeros((12*21, 192, 288))
pdf2_glen = np.zeros((12*21, 192, 288))
pdf3_glen = np.zeros((12*21, 192, 288))
pdf1_equa = np.zeros((12*21, 192, 288))
pdf2_equa = np.zeros((12*21, 192, 288))
pdf3_equa = np.zeros((12*21, 192, 288))

for i in range(21):
    pdf1_ctrl[i*12:(i+1)*12, :, :] = (data1_ctrl.sel(time='%d'%(i+2075)).data - monthly1.data) / std1.data
    pdf2_ctrl[i*12:(i+1)*12, :, :] = (data2_ctrl.sel(time='%d'%(i+2075)).data - monthly2.data) / std2.data
    pdf3_ctrl[i*12:(i+1)*12, :, :] = (data3_ctrl.sel(time='%d'%(i+2075)).data - monthly3.data) / std3.data
    pdf1_glen[i*12:(i+1)*12, :, :] = (data1_glen.sel(time='%d'%(i+2075)).data - monthly1.data) / std1.data
    pdf2_glen[i*12:(i+1)*12, :, :] = (data2_glen.sel(time='%d'%(i+2075)).data - monthly2.data) / std2.data
    pdf3_glen[i*12:(i+1)*12, :, :] = (data3_glen.sel(time='%d'%(i+2075)).data - monthly3.data) / std3.data
    pdf1_equa[i*12:(i+1)*12, :, :] = (data1_equa.sel(time='%d'%(i+2075)).data - monthly1.data) / std1.data
    pdf2_equa[i*12:(i+1)*12, :, :] = (data2_equa.sel(time='%d'%(i+2075)).data - monthly2.data) / std2.data
    pdf3_equa[i*12:(i+1)*12, :, :] = (data3_equa.sel(time='%d'%(i+2075)).data - monthly3.data) / std3.data

pdf_ctrl = (pdf1_ctrl + pdf2_ctrl + pdf3_ctrl) / 3
pdf_glen = (pdf1_glen + pdf2_glen + pdf3_glen) / 3
pdf_equa = (pdf1_equa + pdf2_equa + pdf3_equa) / 3


# mask the ocean
lon = data1_ctrl.lon
lat = data1_ctrl.lat
pdf_ctrl_land = np.zeros((12*21, 192, 288))
pdf_glen_land = np.zeros((12*21, 192, 288))
pdf_equa_land = np.zeros((12*21, 192, 288))

mask = regionmask.defined_regions.natural_earth_v5_0_0.land_110.mask(lon, lat).values
for i in range(21*12):
    pdf_ctrl_land[i, :, :] = np.where(pd.isna(mask), float('nan'), pdf_ctrl[i])
    pdf_glen_land[i, :, :] = np.where(pd.isna(mask), float('nan'), pdf_glen[i])
    pdf_equa_land[i, :, :] = np.where(pd.isna(mask), float('nan'), pdf_equa[i])


# ATTENTION HERE:
# store the 6 arrays for temperature
# switch the varable to precipitation
# then store again using the block between dashed lines below
t_ctrl = pdf_ctrl
t_glen = pdf_glen
t_equa = pdf_equa

t_ctrl_land = pdf_ctrl_land
t_glen_land = pdf_glen_land
t_equa_land = pdf_equa_land

# -------------------

p_ctrl = pdf_ctrl
p_glen = pdf_glen
p_equa = pdf_equa

p_ctrl_land = pdf_ctrl_land
p_glen_land = pdf_glen_land
p_equa_land = pdf_equa_land

# -------------------

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8,8))
plt.subplots_adjust(wspace=0.25)
linewidth = 1.8
linewidth_sub = 0.8
alpha = 0.5

# panel a: global temperature--------------------------------------
binwidth = 1
sns.kdeplot(data=t_ctrl.ravel(), label='Control-Base', color='#AC2026', ax=axs[0,0], linewidth=linewidth)
sns.kdeplot(data=t_glen.ravel(), label='GLENS-Base', color='#BD8EC0', ax=axs[0,0], linewidth=linewidth)
sns.kdeplot(data=t_equa.ravel(), label='GLENS_eq-Base', color='#6F80BE',ax=axs[0,0], linewidth=linewidth)
axs[0,0].set_ylabel("Probability")
axs[0,0].set_xlabel("Standardized anomaly: T (Global)")
axs[0,0].legend(bbox_to_anchor=[0.35, 0.97])
axs[0,0].set_xlim(-6, 15); axs[0,0].set_ylim(0, 0.52)
axs[0,0].yaxis.set_major_formatter(PercentFormatter(1 / binwidth))  # show axis such that 1/binwidth corresponds to 100%
axs[0,0].annotate('(a)', xy=(0.09, 0.91), fontsize=14, xycoords='axes fraction', horizontalalignment='center')
axs[0,0].axvline(0, color='gray', zorder=1, linestyle='dashed')

# panel c: land temperature--------------------------------------
sns.kdeplot(t_ctrl_land.ravel(), color='#AC2026', ax=axs[1,0], linewidth=linewidth)
sns.kdeplot(t_glen_land.ravel(), color='#BD8EC0', ax=axs[1,0], linewidth=linewidth)
sns.kdeplot(t_equa_land.ravel(), color='#6F80BE', ax=axs[1,0], linewidth=linewidth)
axs[1,0].set_ylabel("Probability")
axs[1,0].set_xlabel("Standardized anomaly: T (Land)")
axs[1,0].set_xlim(-6, 15); axs[1,0].set_ylim(0, 0.52)
axs[1,0].yaxis.set_major_formatter(PercentFormatter(1 / binwidth))
axs[1,0].annotate('(c)', xy=(0.09, 0.91), fontsize=14, xycoords='axes fraction', horizontalalignment='center')
axs[1,0].axvline(0, color='gray', zorder=1, linestyle='dashed')

# panel b: global precipitation--------------------------------------
sns.kdeplot(p_ctrl[~(p_ctrl>10)].ravel(), color='#AC2026', ax=axs[0,1], linewidth=linewidth)
sns.kdeplot(p_glen[~(p_glen>10)].ravel(), color='#BD8EC0', ax=axs[0,1], linewidth=linewidth)
sns.kdeplot(p_equa[~(p_equa>10)].ravel(), color='#6F80BE', ax=axs[0,1], linewidth=linewidth)
axs[0,1].set_ylabel("Probability")
axs[0,1].set_xlabel("Standardized anomaly: P (Global)")
axs[0,1].set_xlim(-3, 5); axs[0,1].set_ylim(0, 0.78)
axs[0,1].yaxis.set_major_formatter(PercentFormatter(1 / binwidth))
axs[0,1].annotate('(b)', xy=(0.09, 0.91), fontsize=14, xycoords='axes fraction', horizontalalignment='center')
axs[0,1].axvline(0, color='gray', zorder=1, linestyle='dashed')

# panel d: land precipitation--------------------------------------
sns.kdeplot(p_ctrl_land[~(p_ctrl_land>10)].ravel(), color='#AC2026', ax=axs[1,1], linewidth=linewidth)
sns.kdeplot(p_glen_land[~(p_glen_land>10)].ravel(), color='#BD8EC0', ax=axs[1,1], linewidth=linewidth)
sns.kdeplot(p_equa_land[~(p_equa_land>10)].ravel(), color='#6F80BE', ax=axs[1,1], linewidth=linewidth)
axs[1,1].set_ylabel("Probability")
axs[1,1].set_xlabel("Standardized anomaly: P (Land)")
axs[1,1].set_xlim(-3, 5); axs[1,1].set_ylim(0, 0.78)
axs[1,1].yaxis.set_major_formatter(PercentFormatter(1 / binwidth))
axs[1,1].annotate('(d)', xy=(0.09, 0.91), fontsize=14, xycoords='axes fraction', horizontalalignment='center')
axs[1,1].axvline(0, color='gray', zorder=1, linestyle='dashed')
