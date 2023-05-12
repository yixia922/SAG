import xarray as xr
import numpy as np
import importlib
import sys

sys.path.append("../Functions/")
import cal_base
import var_prop


exp_name = 'control'     # options: control
var_name = 'PRECT'     # options: TREFHTMN/TREFHTMX/PRECT
cal_var = 'Rx5day'           # the targeting indice (besides the percentile ones)

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
# Ensemble 004-020
data04 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.004.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data05 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.005.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data06 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.006.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data07 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.007.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data08 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.008.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data09 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.009.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data10 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.010.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data11 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.011.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data12 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.012.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data13 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.013.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data14 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.014.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data15 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.015.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data16 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.016.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data17 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.017.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data18 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.018.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data19 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.019.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))
data20 = xr.open_dataset("/Volumes/DISK/GLENS_data/%s/daily/%s/b.e15.B5505C5WCCML45BGCR.f09_g16.%s.020.cam.h3.%s.20100101-20301231.nc"%(exp_name,var_name,exp_name,var_name))


ensemble1 = cal_base.cal_indices_base1(data01_1, data01_2, data01_3, cal_var)
ensemble2 = cal_base.cal_indices_base1(data02_1, data02_2, data02_3, cal_var)
ensemble3 = cal_base.cal_indices_base1(data03_1, data03_2, data03_3, cal_var)
ensemble4 = cal_base.cal_indices_base2(data04, cal_var)
ensemble5 = cal_base.cal_indices_base2(data05, cal_var)
ensemble6 = cal_base.cal_indices_base2(data06, cal_var)
ensemble7 = cal_base.cal_indices_base2(data07, cal_var)
ensemble8 = cal_base.cal_indices_base2(data08, cal_var)
ensemble9 = cal_base.cal_indices_base2(data09, cal_var)
ensemble10= cal_base.cal_indices_base2(data10, cal_var)
ensemble11= cal_base.cal_indices_base2(data11, cal_var)
ensemble12= cal_base.cal_indices_base2(data12, cal_var)
ensemble13= cal_base.cal_indices_base2(data13, cal_var)
ensemble14= cal_base.cal_indices_base2(data14, cal_var)
ensemble15= cal_base.cal_indices_base2(data15, cal_var)
ensemble16= cal_base.cal_indices_base2(data16, cal_var)
ensemble17= cal_base.cal_indices_base2(data17, cal_var)
ensemble18= cal_base.cal_indices_base2(data18, cal_var)
ensemble19= cal_base.cal_indices_base2(data19, cal_var)
ensemble20= cal_base.cal_indices_base2(data20, cal_var)

ensemble_avg = (ensemble1 + ensemble2 + ensemble3 + ensemble4 + ensemble5 + 
                ensemble6 + ensemble7 + ensemble8 + ensemble9 + ensemble10+
                ensemble11+ ensemble12+ ensemble13+ ensemble14+ ensemble15+
                ensemble16+ ensemble17+ ensemble18+ ensemble19+ ensemble20)/20


# create the nc file to store the results
year_base = range(2010, 2030+1)
unit = var_prop.get_unit(cal_var)
new_nc = xr.Dataset(
    data_vars=dict(
        ensemble1=(["year","lat","lon"], ensemble1, {'long_name':'%s ensemble 001'%cal_var,'units':'%s'%unit}),
        ensemble2=(["year","lat","lon"], ensemble2, {'long_name':'%s ensemble 002'%cal_var,'units':'%s'%unit}),
        ensemble3=(["year","lat","lon"], ensemble3, {'long_name':'%s ensemble 003'%cal_var,'units':'%s'%unit}),
        ensemble4=(["year","lat","lon"], ensemble4, {'long_name':'%s ensemble 004'%cal_var,'units':'%s'%unit}),
        ensemble5=(["year","lat","lon"], ensemble5, {'long_name':'%s ensemble 005'%cal_var,'units':'%s'%unit}),
        ensemble6=(["year","lat","lon"], ensemble6, {'long_name':'%s ensemble 006'%cal_var,'units':'%s'%unit}),
        ensemble7=(["year","lat","lon"], ensemble7, {'long_name':'%s ensemble 007'%cal_var,'units':'%s'%unit}),
        ensemble8=(["year","lat","lon"], ensemble8, {'long_name':'%s ensemble 008'%cal_var,'units':'%s'%unit}),
        ensemble9=(["year","lat","lon"], ensemble9, {'long_name':'%s ensemble 009'%cal_var,'units':'%s'%unit}),
        ensemble10=(["year","lat","lon"], ensemble10, {'long_name':'%s ensemble 010'%cal_var,'units':'%s'%unit}),
        ensemble11=(["year","lat","lon"], ensemble11, {'long_name':'%s ensemble 011'%cal_var,'units':'%s'%unit}),
        ensemble12=(["year","lat","lon"], ensemble12, {'long_name':'%s ensemble 012'%cal_var,'units':'%s'%unit}),
        ensemble13=(["year","lat","lon"], ensemble13, {'long_name':'%s ensemble 013'%cal_var,'units':'%s'%unit}),
        ensemble14=(["year","lat","lon"], ensemble14, {'long_name':'%s ensemble 014'%cal_var,'units':'%s'%unit}),
        ensemble15=(["year","lat","lon"], ensemble15, {'long_name':'%s ensemble 015'%cal_var,'units':'%s'%unit}),
        ensemble16=(["year","lat","lon"], ensemble16, {'long_name':'%s ensemble 016'%cal_var,'units':'%s'%unit}),
        ensemble17=(["year","lat","lon"], ensemble17, {'long_name':'%s ensemble 017'%cal_var,'units':'%s'%unit}),
        ensemble18=(["year","lat","lon"], ensemble18, {'long_name':'%s ensemble 018'%cal_var,'units':'%s'%unit}),
        ensemble19=(["year","lat","lon"], ensemble19, {'long_name':'%s ensemble 019'%cal_var,'units':'%s'%unit}),
        ensemble20=(["year","lat","lon"], ensemble20, {'long_name':'%s ensemble 020'%cal_var,'units':'%s'%unit}),
        ensemble_avg=(["year","lat","lon"], ensemble_avg, {'long_name':'%s averaged'%cal_var,'units':'%s'%unit}),
    ),
    coords=dict(
        lat=("lat", data01_1.lat.data, {'long_name':'latitude'}),
        lon=("lon", data01_1.lon.data, {'long_name':'longitude'}),
        year=("year", year_base, {'long_name':'year'}),
    ),
    attrs=dict(
        data_source='%s'%exp_name,
        time_range='year 2010-2030',
        method = 'get result in each year -> average between ensembles'
    ),
)


if unit == 'days':
    # solve the problem of converting data to datetime64[ns]
    ensemble1_d = new_nc.ensemble1.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble2_d = new_nc.ensemble2.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble3_d = new_nc.ensemble3.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble4_d = new_nc.ensemble4.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble5_d = new_nc.ensemble5.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble6_d = new_nc.ensemble6.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble7_d = new_nc.ensemble7.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble8_d = new_nc.ensemble8.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble9_d = new_nc.ensemble9.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble10_d = new_nc.ensemble10.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble11_d = new_nc.ensemble11.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble12_d = new_nc.ensemble12.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble13_d = new_nc.ensemble13.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble14_d = new_nc.ensemble14.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble15_d = new_nc.ensemble15.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble16_d = new_nc.ensemble16.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble17_d = new_nc.ensemble17.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble18_d = new_nc.ensemble18.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble19_d = new_nc.ensemble19.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble20_d = new_nc.ensemble20.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    ensemble_avg_d = new_nc.ensemble_avg.astype('timedelta64[D]') / np.timedelta64(1, 'D')
    new_nc2 = xr.Dataset(
        data_vars=dict(ensemble1=ensemble1_d, ensemble2=ensemble2_d, ensemble3=ensemble3_d, 
                       ensemble4=ensemble4_d, ensemble5=ensemble5_d, ensemble6=ensemble6_d, 
                       ensemble7=ensemble7_d, ensemble8=ensemble8_d, ensemble9=ensemble9_d, 
                       ensemble10=ensemble10_d, ensemble11=ensemble11_d, ensemble12=ensemble12_d, 
                       ensemble13=ensemble13_d, ensemble14=ensemble14_d, ensemble15=ensemble15_d, 
                       ensemble16=ensemble16_d, ensemble17=ensemble17_d, ensemble18=ensemble18_d, 
                       ensemble19=ensemble19_d, ensemble20=ensemble20_d, ensemble_avg=ensemble_avg_d),
        coords=new_nc.coords, attrs=new_nc.attrs,
    )
    new_nc2.to_netcdf(path="/Volumes/DISK/GLENS_data/Results/%s.%s.base.nc"%(cal_var,exp_name), mode='w')
else:
    new_nc.to_netcdf(path="/Volumes/DISK/GLENS_data/Results/%s.%s.base.nc"%(cal_var,exp_name), mode='w')
