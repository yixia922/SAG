import xarray as xr
import numpy as np

# For CWD
# change "xr_obj[i] == False" to "xr_obj[i] == True" in the max_cons_CDD function

# calculate CDD in a single year of one grid
def max_cons_CDD(xr_obj):
    overall_counter = []
    count = 0
    count = 0
    for i in range(len(xr_obj)):
        count = count + 1 if xr_obj[i] == False else 0
        overall_counter.append(count)
    return max(overall_counter)

# setting
exp = 'control'  # options: 'control'

# turn precipictiao data to boolean type
# boolean define:
# PRECT >= 1mm : True
# PRECT <  1mm : False
data_bool = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/PRECT.boolean.%s.base.nc"%exp)

CDD1 = np.zeros((21, 192, 288), dtype=int)
CDD2 = np.zeros((21, 192, 288), dtype=int)
CDD3 = np.zeros((21, 192, 288), dtype=int)
CDD4 = np.zeros((21, 192, 288), dtype=int)
CDD5 = np.zeros((21, 192, 288), dtype=int)
CDD6 = np.zeros((21, 192, 288), dtype=int)
CDD7 = np.zeros((21, 192, 288), dtype=int)
CDD8 = np.zeros((21, 192, 288), dtype=int)
CDD9 = np.zeros((21, 192, 288), dtype=int)
CDD10 = np.zeros((21, 192, 288), dtype=int)
CDD11 = np.zeros((21, 192, 288), dtype=int)
CDD12 = np.zeros((21, 192, 288), dtype=int)
CDD13 = np.zeros((21, 192, 288), dtype=int)
CDD14 = np.zeros((21, 192, 288), dtype=int)
CDD15 = np.zeros((21, 192, 288), dtype=int)
CDD16 = np.zeros((21, 192, 288), dtype=int)
CDD17 = np.zeros((21, 192, 288), dtype=int)
CDD18 = np.zeros((21, 192, 288), dtype=int)
CDD19 = np.zeros((21, 192, 288), dtype=int)
CDD20 = np.zeros((21, 192, 288), dtype=int)

CDD_list = [CDD1, CDD2, CDD3, CDD4, CDD5, CDD6, CDD7, CDD8, CDD9, CDD10,
            CDD11,CDD12,CDD13,CDD14,CDD15,CDD16,CDD17,CDD18,CDD19,CDD20]
ensemble_list = [ensemble1, ensemble2, ensemble3, ensemble4, ensemble5, ensemble6, ensemble7, ensemble8, ensemble9, ensemble10,
                 ensemble11,ensemble12,ensemble13,ensemble14,ensemble15,ensemble16,ensemble17,ensemble18,ensemble19,ensemble20]

for index in range(20):
    for year in range(2010, 2030 + 1):
        CDD_now = data_bool.ensemble_list[index].sel(time='%d' % year).data
        for i in range(192):  # loop for lat
            for j in range(288):  # loop for lon
                CDD_list[index][year - 2010, i, j] = max_cons_CDD(CDD_now[:, i, j])
# For average ensemble 001-020
CDD_avg = (CDD1 + CDD2 + CDD3 + CDD4 + CDD5 +
           CDD6 + CDD7 + CDD8 + CDD9 + CDD10+
           CDD11+ CDD12+ CDD13+ CDD14+ CDD15+
           CDD16+ CDD17+ CDD18+ CDD19+ CDD20)/20

# create the nc file to store the results
year = range(2010, 2030 + 1)
new_nc = xr.Dataset(
    data_vars=dict(
        ensemble1=(["year","lat","lon"], CDD1, {'long_name':'CDD ensemble 001','units':'days'}),
        ensemble2=(["year","lat","lon"], CDD2, {'long_name':'CDD ensemble 002','units':'days'}),
        ensemble3=(["year","lat","lon"], CDD3, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble4=(["year","lat","lon"], CDD4, {'long_name':'CDD ensemble 001','units':'days'}),
        ensemble5=(["year","lat","lon"], CDD5, {'long_name':'CDD ensemble 002','units':'days'}),
        ensemble6=(["year","lat","lon"], CDD6, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble7=(["year","lat","lon"], CDD7, {'long_name':'CDD ensemble 001','units':'days'}),
        ensemble8=(["year","lat","lon"], CDD8, {'long_name':'CDD ensemble 002','units':'days'}),
        ensemble9=(["year","lat","lon"], CDD9, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble10=(["year","lat","lon"], CDD10, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble11=(["year","lat","lon"], CDD11, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble12=(["year","lat","lon"], CDD12, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble13=(["year","lat","lon"], CDD13, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble14=(["year","lat","lon"], CDD14, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble15=(["year","lat","lon"], CDD15, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble16=(["year","lat","lon"], CDD16, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble17=(["year","lat","lon"], CDD17, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble18=(["year","lat","lon"], CDD18, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble19=(["year","lat","lon"], CDD19, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble20=(["year","lat","lon"], CDD20, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble_avg=(["year","lat","lon"], CDD_avg, {'long_name':'CDD averaged','units':'days'}),
    ),
    coords=dict(
        lat=("lat", data_bool.lat.data, {'long_name': 'latitude'}),
        lon=("lon", data_bool.lon.data, {'long_name': 'longitude'}),
        year=("year", year, {'long_name': 'year'}),
    ),
    attrs=dict(
        data_source='%s'%exp,
        time_range='year 2010-2030',
        method='get result in each year -> average between ensembles'
    ),
)

# solve the problem of Linux convert data to datetime64[ns]
my_CDD1 = new_nc.ensemble1.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD2 = new_nc.ensemble2.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD3 = new_nc.ensemble3.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD4 = new_nc.ensemble4.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD5 = new_nc.ensemble5.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD6 = new_nc.ensemble6.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD7 = new_nc.ensemble7.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD8 = new_nc.ensemble8.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD9 = new_nc.ensemble9.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD10 = new_nc.ensemble10.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD11 = new_nc.ensemble11.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD12 = new_nc.ensemble12.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD13 = new_nc.ensemble13.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD14 = new_nc.ensemble14.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD15 = new_nc.ensemble15.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD16 = new_nc.ensemble16.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD17 = new_nc.ensemble17.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD18 = new_nc.ensemble18.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD19 = new_nc.ensemble19.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD20 = new_nc.ensemble20.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD_avg = new_nc.ensemble_avg.astype('timedelta64[D]') / np.timedelta64(1, 'D')
new_nc2 = xr.Dataset(
    data_vars=dict(ensemble1=my_CDD1, ensemble2=my_CDD2, ensemble3=my_CDD3, ensemble4=my_CDD4, ensemble5=my_CDD5,
                   ensemble6=my_CDD6, ensemble7=my_CDD7, ensemble8=my_CDD8, ensemble9=my_CDD9, ensemble10=my_CDD10,
                   ensemble11=my_CDD11, ensemble12=my_CDD12, ensemble13=my_CDD13, ensemble14=my_CDD14, ensemble15=my_CDD15,
                   ensemble16=my_CDD16, ensemble17=my_CDD17, ensemble18=my_CDD18, ensemble19=my_CDD19, ensemble20=my_CDD20,
                   ensemble_avg=my_CDD_avg),
    coords=new_nc.coords, attrs=new_nc.attrs,
)
new_nc2.to_netcdf(path="/Volumes/DISK/GLENS_data/Results/CDD.%s.base.nc"%exp, mode='w')
