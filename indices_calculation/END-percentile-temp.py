import xarray as xr
import numpy as np

import sys
sys.path.append("../Functions/") 
import var_prop


def cal_end(data1, data2, data3, thr, if_lower):
    len_year = 21
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    result = np.zeros((len_year, len_lat, len_lon))  # To store the results

    if if_lower == True:
        # For p1 (year 2075-2095)
        for year in range(2075, 2079 + 1):
            data_now = data1.sel(time='%d' % year)
            result[year - 2075, :, :] = np.sum(data_now < thr, axis=0)
        # For p2 (year 2080-2089)
        for year in range(2080, 2089 + 1):
            data_now = data2.sel(time='%d' % year)
            result[year - 2075, :, :] = np.sum(data_now < thr, axis=0)
        # For p3 (year 2090-2095)
        for year in range(2090, 2095 + 1):
            data_now = data3.sel(time='%d' % year)
            result[year - 2075, :, :] = np.sum(data_now < thr, axis=0)
    else:
        # For p1 (year 2075-2095)
        for year in range(2075, 2079 + 1):
            data_now = data1.sel(time='%d' % year)
            result[year - 2075, :, :] = np.sum(data_now > thr, axis=0)
        # For p2 (year 2080-2089)
        for year in range(2080, 2089 + 1):
            data_now = data2.sel(time='%d' % year)
            result[year - 2075, :, :] = np.sum(data_now > thr, axis=0)
        # For p3 (year 2090-2095)
        for year in range(2090, 2095 + 1):
            data_now = data3.sel(time='%d' % year)
            result[year - 2075, :, :] = np.sum(data_now > thr, axis=0)
    return result

exp_name = 'feedback.eq'     # options: control/feedback/feedback.eq
var_name = 'TREFHTMX'     # options: TREFHTMN/TREFHTMX
cal_var = 'TX90p'           # options: TN10p/TN90p/TX10p/TX90p
threshold = 'TX90'          # options: TN10/TN90/TX10/TX90

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

if cal_var in ['TN10p', 'TX10p']:
    if_lower = True
else:
    if_lower = False

ensemble1 = cal_end(data1_1[var_name], data1_2[var_name], data1_3[var_name], thr[threshold], if_lower)
ensemble2 = cal_end(data2_1[var_name], data2_2[var_name], data2_3[var_name], thr[threshold], if_lower)
ensemble3 = cal_end(data3_1[var_name], data3_2[var_name], data3_3[var_name], thr[threshold], if_lower)
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