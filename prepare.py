import numpy as np

def avg_time(xr_obj):
    # average to one year with 12 months data
    avg_time=xr_obj.mean(("time"))
    return avg_time

def avg_month(xr_obj):
    # average to one year with 12 months data
    avg_month=xr_obj.groupby('time.month').mean()
    return avg_month

def avg_year(xr_obj):
    # average to annual data
    avg_year=xr_obj.groupby('time.year').mean()
    return avg_year

def std_month(xr_obj):
    # standard deviation to one year with 12 months data
    std_month=xr_obj.groupby('time.month').std()
    return std_month

def avg_latlon(xr_obj):
    # !!!! input single variable !!!!
    # average to global mean
    # get weights
    weights = np.cos(np.deg2rad(xr_obj.lat))
    weights.name = "weights"
    # average on lat, lon
    xr_obj_weighted = xr_obj.weighted(weights)
    avg_latlon = xr_obj_weighted.mean(("lon", "lat"))
    return avg_latlon

def avg_lat(xr_obj):
    # deminish latitude demention
    # get weights
    weights = np.cos(np.deg2rad(xr_obj.lat))
    weights.name = "weights"
    # average on lat
    xr_obj_weighted = xr_obj.weighted(weights)
    avg_lat = xr_obj_weighted.mean(("lat"))
    return avg_lat

def avg_lon(xr_obj):
    # deminish longitude demention
    avg_lon = xr_obj.mean(("lon"))
    return avg_lon

def AVG(xr_obj):
    # avgerage lat, lon, time
    # get weights
    weights = np.cos(np.deg2rad(xr_obj.lat))
    weights.name = "weights"
    # average on lat, lon
    xr_obj_weighted = xr_obj.weighted(weights)
    avg_latlon = xr_obj_weighted.mean(("lon", "lat"))
    # average on time
    AVG = avg_latlon.mean(("time"))
    return AVG
