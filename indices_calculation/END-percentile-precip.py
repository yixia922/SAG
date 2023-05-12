import xarray as xr
import numpy as np

import sys
sys.path.append("../Functions/") 
import var_prop


def cal_end(data, thr):
    result = np.zeros((21, 192, 288))  # To store the results
    for year in range(2075, 2095 + 1):
        data_now = data.sel(time='%d' % year)
        result[year - 2075, :, :] = np.sum(data_now, axis=0)   
    return result

exp_name = 'feedback.eq'     # options: control/feedback/feedback.eq
var_name = 'PRECT'     # options: PRECT
cal_var = 'R99pTOT'           # options: R95pTOT/R99pTOT
threshold = 'R99'         # options: R95/R99

# input the threshold
thr = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/threshold_temp&precip.nc")

if exp_name == 'control':
    # Ensemble 001
    data1_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20691231-20791230.nc"%(exp_name,var_name,exp_name,var_name))
    data1_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20791231-20891230.nc"%(exp_name,var_name,exp_name,var_name))
    data1_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20891231-20990630.nc"%(exp_name,var_name,exp_name,var_name))
    # Ensemble 002
    data2_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20691231-20791230.nc"%(exp_name,var_name,exp_name,var_name))
    data2_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20791231-20891230.nc"%(exp_name,var_name,exp_name,var_name))
    data2_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20891231-20980811.nc"%(exp_name,var_name,exp_name,var_name))
    # Ensemble 003
    data3_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20691231-20791230.nc"%(exp_name,var_name,exp_name,var_name))
    data3_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20791231-20891230.nc"%(exp_name,var_name,exp_name,var_name))
    data3_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20891231-20991230.nc"%(exp_name,var_name,exp_name,var_name))
else:
    # Ensemble 001
    data1_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20700101-20791231.nc"%(exp_name,var_name,exp_name,var_name))
    data1_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20800101-20891231.nc"%(exp_name,var_name,exp_name,var_name))
    data1_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.001.cam.h3.%s.20900101-20991231.nc"%(exp_name,var_name,exp_name,var_name))
    # Ensemble 002
    data2_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20700101-20791231.nc"%(exp_name,var_name,exp_name,var_name))
    data2_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20800101-20891231.nc"%(exp_name,var_name,exp_name,var_name))
    data2_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.002.cam.h3.%s.20900101-20991231.nc"%(exp_name,var_name,exp_name,var_name))
    # Ensemble 003
    data3_1 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20700101-20791231.nc"%(exp_name,var_name,exp_name,var_name))
    data3_2 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20800101-20891231.nc"%(exp_name,var_name,exp_name,var_name))
    data3_3 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.003.cam.h3.%s.20900101-20991231.nc"%(exp_name,var_name,exp_name,var_name))


data1 = xr.merge([data1_1, data1_2, data1_3]).sel(time=slice("2075", "2095"))
data2 = xr.merge([data2_1, data2_2, data2_3]).sel(time=slice("2075", "2095"))
data3 = xr.merge([data3_1, data3_2, data3_3]).sel(time=slice("2075", "2095"))

# add a dimension to threshold array
new_thr = np.zeros((len(data1.time), 192, 288))
for i in range(len(data1.time)):
    new_thr[i] = thr[threshold]


# set 0 to values less than the threshold
filtered_data1 = np.where(data1[var_name] < new_thr, 0, data1[var_name])
filtered_data2 = np.where(data2[var_name] < new_thr, 0, data2[var_name])
filtered_data3 = np.where(data3[var_name] < new_thr, 0, data3[var_name])

filtered_data1 = xr.DataArray(filtered_data1, coords=data1[var_name].coords, dims=data1[var_name].dims)
filtered_data2 = xr.DataArray(filtered_data2, coords=data1[var_name].coords, dims=data1[var_name].dims)
filtered_data3 = xr.DataArray(filtered_data3, coords=data1[var_name].coords, dims=data1[var_name].dims)

ensemble1 = cal_end(filtered_data1, thr[threshold])
ensemble2 = cal_end(filtered_data2, thr[threshold])
ensemble3 = cal_end(filtered_data3, thr[threshold])
ensemble_avg = (ensemble1 + ensemble2 + ensemble3)/3

# create the nc file to store the results
year_end = range(2075, 2095+1)
new_nc = xr.Dataset(
    data_vars=dict(
        ensemble1=(["year","lat","lon"], ensemble1*1000*24*3600, {'long_name':'%s ensemble 001'%cal_var,'units':'mm'}),
        ensemble2=(["year","lat","lon"], ensemble2*1000*24*3600, {'long_name':'%s ensemble 002'%cal_var,'units':'mm'}),
        ensemble3=(["year","lat","lon"], ensemble3*1000*24*3600, {'long_name':'%s ensemble 003'%cal_var,'units':'mm'}),
        ensemble_avg=(["year","lat","lon"], ensemble_avg*1000*24*3600, {'long_name':'%s averaged'%cal_var,'units':'mm'}),
    ),
    coords=dict(
        lat=("lat", data1.lat.data, {'long_name':'latitude'}),
        lon=("lon", data1.lon.data, {'long_name':'longitude'}),
        year=("year", year_end, {'long_name':'year'}),
    ),
    attrs=dict(
        data_source='%s'%exp_name,
        time_range='year 2075-2095',
        method = 'get result in each year -> average between ensembles'
    ),
)

new_nc.to_netcdf(path="/Volumes/DISK/GLENS_data/Results/%s.%s.end.nc"%(cal_var,exp_name), mode='w')
