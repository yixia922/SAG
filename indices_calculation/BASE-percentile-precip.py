import xarray as xr
import numpy as np

import sys
sys.path.append("../Functions/") 
import var_prop


def cal_base(data, thr):
    result = np.zeros((21, 192, 288))  # To store the results
    for year in range(2010, 2030 + 1):
        data_now = data.sel(time='%d' % year)
        result[year - 2010, :, :] = np.sum(data_now, axis=0)
    return result


exp_name = 'control'     # options: control
var_name = 'PRECT'     # options: PRECT
cal_var = 'R99pTOT'           # options: R95pTOT/R99pTOT
threshold = 'R99'         # options: R95/R99

# input the threshold
thr = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/threshold_temp&precip.nc")

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


data01 = xr.merge([data01_1, data01_2, data01_3]).sel(time=slice("2010", "2030"))
data02 = xr.merge([data02_1, data02_2, data02_3]).sel(time=slice("2010", "2030"))
data03 = xr.merge([data03_1, data03_2, data03_3]).sel(time=slice("2010", "2030"))

del data01_1, data01_2, data01_3
del data02_1, data02_2, data02_3
del data03_1, data03_2, data03_3


# add a dimension to threshold array
new_thr = np.zeros((len(data01.time), 192, 288))
for i in range(len(data01.time)):
    new_thr[i] = thr[threshold]

# set 0 to values less than the threshold
filtered_data01 = np.where(data01[var_name] < new_thr, 0, data01[var_name])
filtered_data02 = np.where(data02[var_name] < new_thr, 0, data02[var_name])
filtered_data03 = np.where(data03[var_name] < new_thr, 0, data03[var_name])

filtered_data01 = xr.DataArray(filtered_data01, coords=data01[var_name].coords, dims=data01[var_name].dims)
filtered_data02 = xr.DataArray(filtered_data02, coords=data01[var_name].coords, dims=data01[var_name].dims)
filtered_data03 = xr.DataArray(filtered_data03, coords=data01[var_name].coords, dims=data01[var_name].dims)

ensemble1 = cal_base(filtered_data01, thr[threshold])
ensemble2 = cal_base(filtered_data02, thr[threshold])
ensemble3 = cal_base(filtered_data03, thr[threshold])
ensemble_avg = (ensemble1 + ensemble2 + ensemble3)/3


# create the nc file to store the results
year_base = range(2010, 2030+1)
new_nc = xr.Dataset(
    data_vars=dict(
        ensemble1=(["year","lat","lon"], ensemble1*1000*24*3600, {'long_name':'%s ensemble 001'%cal_var,'units':'mm'}),
        ensemble2=(["year","lat","lon"], ensemble2*1000*24*3600, {'long_name':'%s ensemble 002'%cal_var,'units':'mm'}),
        ensemble3=(["year","lat","lon"], ensemble3*1000*24*3600, {'long_name':'%s ensemble 003'%cal_var,'units':'mm'}),
        ensemble_avg=(["year","lat","lon"], ensemble_avg*1000*24*3600, {'long_name':'%s averaged'%cal_var,'units':'mm'}),
    ),
    coords=dict(
        lat=("lat", data01.lat.data, {'long_name':'latitude'}),
        lon=("lon", data01.lon.data, {'long_name':'longitude'}),
        year=("year", year_base, {'long_name':'year'}),
    ),
    attrs=dict(
        data_source='%s'%exp_name,
        time_range='year 2010-2030',
        method = 'get result in each year -> average between ensembles'
    ),
)
new_nc.to_netcdf(path="/Volumes/DISK/GLENS_data/Results/%s.%s.base.nc"%(cal_var,exp_name), mode='w')
