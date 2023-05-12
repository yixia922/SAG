import xarray as xr
import numpy as np


exp_name = 'control'     # options: control
var_name = 'PRECT'     # options: TREFHTMN/TREFHTMX/PRECT

# Ensemble 001
data01_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20100101-20191230.nc"%(exp_name,var_name,exp_name,var_name))
data01_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20191231-20291230.nc"%(exp_name,var_name,exp_name,var_name))
data01_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20291231-20391230.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 002
data02_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20100101-20191230.nc"%(exp_name,var_name,exp_name,var_name))
data02_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20191231-20291230.nc"%(exp_name,var_name,exp_name,var_name))
data02_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20291231-20391230.nc"%(exp_name,var_name,exp_name,var_name))
# Ensemble 003
data03_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20100101-20191230.nc"%(exp_name,var_name,exp_name,var_name))
data03_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20191231-20291230.nc"%(exp_name,var_name,exp_name,var_name))
data03_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20291231-20391230.nc"%(exp_name,var_name,exp_name,var_name))

data01 = xr.merge([data01_1, data01_2, data01_3])
data02 = xr.merge([data02_1, data02_2, data02_3])
data03 = xr.merge([data03_1, data03_2, data03_3])


ensemble01 = data01[var_name].sel(time=slice('2010', '2030'))
ensemble02 = data02[var_name].sel(time=slice('2010', '2030'))
ensemble03 = data03[var_name].sel(time=slice('2010', '2030'))

lat_len = len(ensemble01.lat)
lon_len = len(ensemble01.lon)
percentile = np.zeros((lat_len, lon_len))
percentile1 = np.zeros((lat_len, lon_len))
percentile2 = np.zeros((lat_len, lon_len))
percentile3 = np.zeros((lat_len, lon_len))

for i in range(lat_len):
    for j in range(lon_len):
        percentile1[i,j] = np.percentile(ensemble01[:,i,j], 99)
        percentile2[i,j] = np.percentile(ensemble02[:,i,j], 99)
        percentile3[i,j] = np.percentile(ensemble03[:,i,j], 99)
        
percentile = (percentile1 + percentile2 + percentile3)/3
