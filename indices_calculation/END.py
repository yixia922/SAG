import xarray as xr
import numpy as np
import importlib

import sys
sys.path.append("../Functions/")
import cal_end
import var_prop


exp_name = 'feedback.eq'     # options: control/feedback/feedback.eq
var_name = 'PRECT'     # options: TREFHTMN/TREFHTMX/PRECT
cal_var = 'R20mm'           # the targeting indice

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


ensemble1 = cal_end.cal_indices_end(data1_1, data1_2, data1_3, cal_var)
ensemble2 = cal_end.cal_indices_end(data2_1, data2_2, data2_3, cal_var)
ensemble3 = cal_end.cal_indices_end(data3_1, data3_2, data3_3, cal_var)
ensemble_avg = (ensemble1 + ensemble2 + ensemble3)/3


# create the nc file to store the results
year_end = range(2075, 2095+1)
unit = var_prop.get_unit(cal_var)
new_nc = xr.Dataset(
    data_vars=dict(
        ensemble1=(["year","lat","lon"], ensemble1, {'long_name':'%s ensemble 001'%cal_var,'units':'%s'%unit}),
        ensemble2=(["year","lat","lon"], ensemble2, {'long_name':'%s ensemble 002'%cal_var,'units':'%s'%unit}),
        ensemble3=(["year","lat","lon"], ensemble3, {'long_name':'%s ensemble 003'%cal_var,'units':'%s'%unit}),
        ensemble_avg=(["year","lat","lon"], ensemble_avg, {'long_name':'%s averaged'%cal_var,'units':'%s'%unit}),
    ),
    coords=dict(
        lat=("lat", data1_1.lat.data, {'long_name':'latitude'}),
        lon=("lon", data1_1.lon.data, {'long_name':'longitude'}),
        year=("year", year_end, {'long_name':'year'}),
    ),
    attrs=dict(
        data_source='%s'%exp_name,
        time_range='year 2075-2095',
        method = 'get result in each year -> average between ensembles'
    ),
)


if unit == 'days':
    # solve the problem of converting data to datetime64[ns]
    ensemble1_d = new_nc.ensemble1.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble2_d = new_nc.ensemble2.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble3_d = new_nc.ensemble3.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble_avg_d = new_nc.ensemble_avg.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    new_nc2 = xr.Dataset(
        data_vars=dict(ensemble1=ensemble1_d, ensemble2=ensemble2_d, ensemble3=ensemble3_d, ensemble_avg=ensemble_avg_d),
        coords=new_nc.coords, attrs=new_nc.attrs,
    )
    new_nc2.to_netcdf(path="/Volumes/DISK/GLENS_data/Results/%s.%s.end.nc"%(cal_var,exp_name), mode='w')
else:
    new_nc.to_netcdf(path="/Volumes/DISK/GLENS_data/Results/%s.%s.end.nc"%(cal_var,exp_name), mode='w')

