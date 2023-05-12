import xarray as xr
import numpy as np

# For CWD
# change "xr_obj[i] == False" to "xr_obj[i] == True" in the max_cons_CDD function

# calculate CDD in a single year of one grid
def max_cons_CDD(xr_obj):
    overall_counter = []
    count = 0
    for i in range(len(xr_obj)):
        count = count + 1 if xr_obj[i] == False else 0
        overall_counter.append(count)
    return max(overall_counter)

# setting
exp = 'feedback.eq'  # options: 'control', 'feedback', 'feedback.eq'

# turn precipictiao data to boolean type
# boolean define:
# PRECT >= 1mm : True
# PRECT <  1mm : False
data_bool = xr.open_dataset("/Volumes/DISK/GLENS_data/Results/PRECT.boolean.%s.end.nc"%exp)

CDD1 = np.zeros((21, 192, 288), dtype=int)
CDD2 = np.zeros((21, 192, 288), dtype=int)
CDD3 = np.zeros((21, 192, 288), dtype=int)

CDD_list = [CDD1, CDD2, CDD3]
ensemble_list = [ensemble1, ensemble2, ensemble3]

for index in range(3):
    for year in range(2075, 2095 + 1):
        CDD_now = data_bool.ensemble_list[index].sel(time='%d' % year).data
        for i in range(192):  # loop for lat
            for j in range(288):  # loop for lon
                CDD_list[index][year - 2075, i, j] = max_cons_CDD(CDD_now[:, i, j])
# For average ensemble 001-003
CDD_avg = (CDD1 + CDD2 + CDD3)/3

# create the nc file to store the results
year = range(2075, 2095 + 1)
new_nc = xr.Dataset(
    data_vars=dict(
        ensemble1=(["year","lat","lon"], CDD1, {'long_name': 'CDD ensemble 001', 'units': 'days'}),
        ensemble2=(["year","lat","lon"], CDD2, {'long_name':'CDD ensemble 002','units':'days'}),
        ensemble3=(["year","lat","lon"], CDD3, {'long_name':'CDD ensemble 003','units':'days'}),
        ensemble_avg=(["year","lat","lon"], CDD_avg, {'long_name':'CDD averaged','units':'days'}),
    ),
    coords=dict(
        lat=("lat", data_bool.lat.data, {'long_name': 'latitude'}),
        lon=("lon", data_bool.lon.data, {'long_name': 'longitude'}),
        year=("year", year, {'long_name': 'year'}),
    ),
    attrs=dict(
        data_source='%s'%exp,
        time_range='year 2075-2095',
        method='get result in each year -> average between ensembles'
    ),
)

# solve the problem of converting data to datetime64[ns]
my_CDD1 = new_nc.ensemble1.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD2 = new_nc.ensemble2.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD3 = new_nc.ensemble3.astype('timedelta64[D]') / np.timedelta64(1, 'D')
my_CDD_avg = new_nc.ensemble_avg.astype('timedelta64[D]') / np.timedelta64(1, 'D')
new_nc2 = xr.Dataset(
    data_vars=dict(ensemble1=my_CDD1, ensemble2=my_CDD2, ensemble3=my_CDD3, ensemble_avg=my_CDD_avg),
    coords=new_nc.coords, attrs=new_nc.attrs,
)
new_nc2.to_netcdf(path="/Volumes/DISK/GLENS_data/Results/CDD.%s.end.nc"%exp, mode='w')
