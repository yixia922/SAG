import numpy as np


# For ensemble 001-003:
# the data of year 2010-2030 was seperated into 3 files
# select the function to run according to the index type
def cal_indices_base1(data1, data2, data3, indices):
    if indices == 'TNn':
        result = cal_TNn_base1(data1, data2, data3)
    elif indices == 'TXn':
        result = cal_TXn_base1(data1, data2, data3)
    elif indices == 'TNx':
        result = cal_TNx_base1(data1, data2, data3)
    elif indices == 'TXx':
        result = cal_TXx_base1(data1, data2, data3)
    elif indices == 'FD':
        result = cal_FD_base1(data1, data2, data3)
    elif indices == 'ID':
        result = cal_ID_base1(data1, data2, data3)
    elif indices == 'TR':
        result = cal_TR_base1(data1, data2, data3)
    elif indices == 'SU':
        result = cal_SU_base1(data1, data2, data3)
    elif indices == 'PRCPTOT':
        result = cal_PRCPTOT_base1(data1, data2, data3)
    elif indices == 'SDII':
        result = cal_SDII_base1(data1, data2, data3)
    elif indices == 'Rx1day':
        result = cal_Rx1day_base1(data1, data2, data3)
    elif indices == 'Rx5day':
        result = cal_Rx5day_base1(data1, data2, data3)
    elif indices == 'R10mm':
        result = cal_R10mm_base1(data1, data2, data3)
    elif indices == 'R20mm':
        result = cal_R20mm_base1(data1, data2, data3)
    return result


# For ensemble 004-020:
# all the data is in a single file
# select the function to run according to the index type
def cal_indices_base2(data, indices):
    len_year = 21  # year 2010-2030
    len_lat = len(data.lat)
    len_lon = len(data.lon)
    result = np.zeros((len_year, len_lat, len_lon))

    if indices == 'TNn':
        for year in range(2010, 2030 + 1):
            TN_now = data.TREFHTMN.sel(time='%d' % year)
            result[year - 2010, :, :] = TN_now.min(axis=0)
        result = result - 273.15  # change unit from K to celsius
    elif indices == 'TXn':
        for year in range(2010, 2030 + 1):
            TX_now = data.TREFHTMX.sel(time='%d' % year)
            result[year - 2010, :, :] = TX_now.min(axis=0)
        result = result - 273.15  # change unit from K to celsius
    elif indices == 'TNx':
        for year in range(2010, 2030 + 1):
            TN_now = data.TREFHTMN.sel(time='%d' % year)
            result[year - 2010, :, :] = TN_now.max(axis=0)
        result = result - 273.15  # change unit from K to celsius
    elif indices == 'TXx':
        for year in range(2010, 2030 + 1):
            TX_now = data.TREFHTMX.sel(time='%d' % year)
            result[year - 2010, :, :] = TX_now.max(axis=0)
        result = result - 273.15  # change unit from K to celsius
    elif indices == 'FD':
        for year in range(2010, 2030 + 1):
            FD_now = data.TREFHTMN.sel(time='%d'%year)
            result[year - 2010, :, :] = np.sum(FD_now <= 273.15, axis=0)
    elif indices == 'ID':
        for year in range(2010, 2030 + 1):
            ID_now = data.TREFHTMX.sel(time='%d'%year)
            result[year - 2010, :, :] = np.sum(ID_now <= 273.15, axis=0)
    elif indices == 'TR':
        for year in range(2010, 2030 + 1):
            TR_now = data.TREFHTMN.sel(time='%d'%year)
            result[year - 2010, :, :] = np.sum(TR_now >= 293.15, axis=0)
    elif indices == 'SU':
        for year in range(2010, 2030 + 1):
            SU_now = data.TREFHTMX.sel(time='%d'%year)
            result[year - 2010, :, :] = np.sum(SU_now >= 298.15, axis=0)
    elif indices == 'PRCPTOT':
        for year in range(2010, 2030 + 1):
            PRCPTOT_now = data.PRECT.sel(time='%d'%year)
            result[year - 2010, :, :] = np.sum(PRCPTOT_now, axis=0)
        result = result * 1000 * 3600 * 24  # change unit from m/s to mm/day
    elif indices == 'SDII':
        for year in range(2010, 2030 + 1):
            SDII_now = data.PRECT.sel(time='%d'%year)
            SDII_now = SDII_now * 1000 * 3600 * 24
            SDII_now = SDII_now.where(SDII_now >= 1, 0)  # Ignore daily precip less than 1mm, asign them with zero
            result[year - 2010, :, :] = np.sum(SDII_now, axis=0)
        result = result / len(SDII_now.time)
    elif indices == 'Rx1day':
        for year in range(2010, 2030 + 1):
            Rx1day_now = data.PRECT.sel(time='%d'%year)
            result[year - 2010, :, :] = Rx1day_now.max(axis=0)
        result = result * 1000 * 3600 * 24  # change unit from m/s to mm/day
    elif indices == 'Rx5day':
        for year in range(2010, 2030 + 1):
            daily_now = data.PRECT.sel(time='%d'%year)
            # change time format from cftime to datatime64
            daily_now = daily_now.assign_coords(time=daily_now.indexes['time'].to_datetimeindex());
            Rx5day_now = daily_now.rolling(time=5).sum()
            result[year - 2010, :, :] = Rx5day_now.max(axis=0)
        result = result * 1000 * 3600 * 24  # change unit from m/s to mm/day
    elif indices == 'R10mm':
        for year in range(2010, 2030 + 1):
            R10mm_now = data.PRECT.sel(time='%d'%year)
            R10mm_now = R10mm_now * 1000 * 3600 * 24
            result[year - 2010, :, :] = np.sum(R10mm_now >= 10, axis=0)
    elif indices == 'R20mm':
        for year in range(2010, 2030 + 1):
            R20mm_now = data.PRECT.sel(time='%d'%year)
            R20mm_now = R20mm_now * 1000 * 3600 * 24
            result[year - 2010, :, :] = np.sum(R20mm_now >= 20, axis=0)
    return result


# function to calculate each index
def cal_TNn_base1(data1, data2, data3):
    # calculate TNn in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    TNn = np.zeros((len_year, len_lat, len_lon))  # To store the TNn results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        TN_now = data1.TREFHTMN.sel(time='%d' % year)
        TNn[year - 2010, :, :] = TN_now.min(axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        TN_now = data2.TREFHTMN.sel(time='%d' % year)
        TNn[year - 2010, :, :] = TN_now.min(axis=0)
    # For p3 (year 2030)
    TN_now = data3.TREFHTMN.sel(time='2030')
    TNn[20, :, :] = TN_now.min(axis=0)
    TNn = TNn - 273.15  # change unit from K to celsius
    return TNn


def cal_TXn_base1(data1, data2, data3):
    # calculate TXn in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    TXn = np.zeros((len_year, len_lat, len_lon))  # To store the TXn results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        TX_now = data1.TREFHTMX.sel(time='%d' % year)
        TXn[year - 2010, :, :] = TX_now.min(axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        TX_now = data2.TREFHTMX.sel(time='%d' % year)
        TXn[year - 2010, :, :] = TX_now.min(axis=0)
    # For p3 (year 2030)
    TX_now = data3.TREFHTMX.sel(time='2030')
    TXn[20, :, :] = TX_now.min(axis=0)
    TXn = TXn - 273.15  # change unit from K to celsius
    return TXn


def cal_TNx_base1(data1, data2, data3):
    # calculate TNx in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    TNx = np.zeros((len_year, len_lat, len_lon))  # To store the TNx results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        TN_now = data1.TREFHTMN.sel(time='%d' % year)
        TNx[year - 2010, :, :] = TN_now.max(axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        TN_now = data2.TREFHTMN.sel(time='%d' % year)
        TNx[year - 2010, :, :] = TN_now.max(axis=0)
    # For p3 (year 2030)
    TN_now = data3.TREFHTMN.sel(time='2030')
    TNx[20, :, :] = TN_now.max(axis=0)
    TNx = TNx - 273.15  # change unit from K to celsius
    return TNx


def cal_TXx_base1(data1, data2, data3):
    # calculate TXx in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    TXx = np.zeros((len_year, len_lat, len_lon))  # To store the TXx results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        TX_now = data1.TREFHTMX.sel(time='%d' % year)
        TXx[year - 2010, :, :] = TX_now.max(axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        TX_now = data2.TREFHTMX.sel(time='%d' % year)
        TXx[year - 2010, :, :] = TX_now.max(axis=0)
    # For p3 (year 2030)
    TX_now = data3.TREFHTMX.sel(time='2030')
    TXx[20, :, :] = TX_now.max(axis=0)
    TXx = TXx - 273.15  # change unit from K to celsius
    return TXx


def cal_FD_base1(data1, data2, data3):
    # calculate Frost Day (FD) in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    FD = np.zeros((len_year, len_lat, len_lon))  # To store the FD results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        FD_now = data1.TREFHTMN.sel(time='%d' % year)
        FD[year - 2010, :, :] = np.sum(FD_now <= 273.15, axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        FD_now = data2.TREFHTMN.sel(time='%d' % year)
        FD[year - 2010, :, :] = np.sum(FD_now <= 273.15, axis=0)
    # For p3 (year 2030)
    FD_now = data3.TREFHTMN.sel(time='2030')
    FD[20, :, :] = np.sum(FD_now <= 273.15, axis=0)

    return FD


def cal_ID_base1(data1, data2, data3):
    # calculate Iced Day (ID) in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    ID = np.zeros((len_year, len_lat, len_lon))  # To store the ID results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        ID_now = data1.TREFHTMX.sel(time='%d' % year)
        ID[year - 2010, :, :] = np.sum(ID_now <= 273.15, axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        ID_now = data2.TREFHTMX.sel(time='%d' % year)
        ID[year - 2010, :, :] = np.sum(ID_now <= 273.15, axis=0)
    # For p3 (year 2030)
    ID_now = data3.TREFHTMX.sel(time='2030')
    ID[20, :, :] = np.sum(ID_now <= 273.15, axis=0)

    return ID


def cal_TR_base1(data1, data2, data3):
    # calculate Tropical Nights (TR) in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    TR = np.zeros((len_year, len_lat, len_lon))  # To store the TR results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        TR_now = data1.TREFHTMN.sel(time='%d' % year)
        TR[year - 2010, :, :] = np.sum(TR_now >= 293.15, axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        TR_now = data2.TREFHTMN.sel(time='%d' % year)
        TR[year - 2010, :, :] = np.sum(TR_now >= 293.15, axis=0)
    # For p3 (year 2030)
    TR_now = data3.TREFHTMN.sel(time='2030')
    TR[20, :, :] = np.sum(TR_now >= 293.15, axis=0)

    return TR


def cal_SU_base1(data1, data2, data3):
    # calculate Summer Day (SU) in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    SU = np.zeros((len_year, len_lat, len_lon))  # To store the SU results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        SU_now = data1.TREFHTMX.sel(time='%d' % year)
        SU[year - 2010, :, :] = np.sum(SU_now >= 298.15, axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        SU_now = data2.TREFHTMX.sel(time='%d' % year)
        SU[year - 2010, :, :] = np.sum(SU_now >= 298.15, axis=0)
    # For p3 (year 2030)
    SU_now = data3.TREFHTMX.sel(time='2030')
    SU[20, :, :] = np.sum(SU_now >= 298.15, axis=0)

    return SU


def cal_PRCPTOT_base1(data1, data2, data3):
    # calculate Anuual sum precipitation (PRCPTOT) in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    PRCPTOT = np.zeros((len_year, len_lat, len_lon))  # To store the PRCPTOT results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        PRCPTOT_now = data1.PRECT.sel(time='%d' % year)
        PRCPTOT[year - 2010, :, :] = np.sum(PRCPTOT_now, axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        PRCPTOT_now = data2.PRECT.sel(time='%d' % year)
        PRCPTOT[year - 2010, :, :] = np.sum(PRCPTOT_now, axis=0)
    # For p3 (year 2030)
    PRCPTOT_now = data3.PRECT.sel(time='2030')
    PRCPTOT[20, :, :] = np.sum(PRCPTOT_now, axis=0)
    PRCPTOT = PRCPTOT * 1000 * 3600 * 24  # change unit from m/s to mm/day
    return PRCPTOT


def cal_SDII_base1(data1, data2, data3):
    # calculate Simple daily precipitation (SDII) in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    SDII = np.zeros((len_year, len_lat, len_lon))  # To store the SDII results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        SDII_now = data1.PRECT.sel(time='%d' % year)
        SDII_now = SDII_now * 1000 * 3600 * 24  # change unit from m/s to mm/day
        SDII_now = SDII_now.where(SDII_now >= 1, 0)  # Ignore daily precip less than 1mm, asign them with zero
        SDII[year - 2010, :, :] = np.sum(SDII_now, axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        SDII_now = data2.PRECT.sel(time='%d' % year)
        SDII_now = SDII_now * 1000 * 3600 * 24
        SDII_now = SDII_now.where(SDII_now >= 1, 0)
        SDII[year - 2010, :, :] = np.sum(SDII_now, axis=0)
    # For p3 (year 2030)
    SDII_now = data3.PRECT.sel(time='2030')
    SDII_now = SDII_now * 1000 * 3600 * 24
    SDII_now = SDII_now.where(SDII_now >= 1, 0)
    SDII[20, :, :] = np.sum(SDII_now, axis=0)
    SDII = SDII / len(SDII_now.time)
    return SDII


def cal_Rx1day_base1(data1, data2, data3):
    # calculate maximum daily precipitation (Rx1day) in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    Rx1day = np.zeros((len_year, len_lat, len_lon))  # To store the Rx1day results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        Rx1day_now = data1.PRECT.sel(time='%d' % year)
        Rx1day[year - 2010, :, :] = Rx1day_now.max(axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        Rx1day_now = data2.PRECT.sel(time='%d' % year)
        Rx1day[year - 2010, :, :] = Rx1day_now.max(axis=0)
    # For p3 (year 2030)
    Rx1day_now = data3.PRECT.sel(time='2030')
    Rx1day[20, :, :] = Rx1day_now.max(axis=0)
    Rx1day = Rx1day * 1000 * 3600 * 24  # change unit from m/s to mm/day
    return Rx1day


def cal_Rx5day_base1(data1, data2, data3):
    # calculate maximum 5-day precipitation (Rx5day) in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    Rx5day = np.zeros((len_year, len_lat, len_lon))  # To store the Rx5day results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        daily_now = data1.PRECT.sel(time='%d' % year)
        # change time format from cftime to datatime64
        daily_now = daily_now.assign_coords(time=daily_now.indexes['time'].to_datetimeindex())
        Rx5day_now = daily_now.rolling(time=5).sum()
        Rx5day[year - 2010, :, :] = Rx5day_now.max(axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        daily_now = data2.PRECT.sel(time='%d' % year)
        daily_now = daily_now.assign_coords(time=daily_now.indexes['time'].to_datetimeindex())
        Rx5day_now = daily_now.rolling(time=5).sum()
        Rx5day[year - 2010, :, :] = Rx5day_now.max(axis=0)
    # For p3 (year 2030)
    daily_now = data3.PRECT.sel(time='2030')
    daily_now = daily_now.assign_coords(time=daily_now.indexes['time'].to_datetimeindex())
    Rx5day_now = daily_now.rolling(time=5).sum()
    Rx5day[20, :, :] = Rx5day_now.max(axis=0)
    Rx5day = Rx5day * 1000 * 3600 * 24  # change unit from m/s to mm/day
    return Rx5day


def cal_R10mm_base1(data1, data2, data3):
    # calculate R10mm in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    R10mm = np.zeros((len_year, len_lat, len_lon))  # To store the R10mm results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        R10mm_now = data1.PRECT.sel(time='%d' % year)
        R10mm_now = R10mm_now * 1000 * 3600 * 24
        R10mm[year - 2010, :, :] = np.sum(R10mm_now >= 10, axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        R10mm_now = data2.PRECT.sel(time='%d' % year)
        R10mm_now = R10mm_now * 1000 * 3600 * 24
        R10mm[year - 2010, :, :] = np.sum(R10mm_now >= 10, axis=0)
    # For p3 (year 2030)
    R10mm_now = data3.PRECT.sel(time='2030')
    R10mm_now = R10mm_now * 1000 * 3600 * 24
    R10mm[20, :, :] = np.sum(R10mm_now >= 10, axis=0)
    return R10mm


def cal_R20mm_base1(data1, data2, data3):
    # calculate R20mm in each year
    len_year = 21  # year 2010-2030
    len_lat = len(data1.lat)
    len_lon = len(data1.lon)
    R20mm = np.zeros((len_year, len_lat, len_lon))  # To store the R20mm results

    # For p1 (year 2010-2019)
    for year in range(2010, 2019 + 1):
        R20mm_now = data1.PRECT.sel(time='%d' % year)
        R20mm_now = R20mm_now * 1000 * 3600 * 24
        R20mm[year - 2010, :, :] = np.sum(R20mm_now >= 20, axis=0)
    # For p2 (year 2020-2029)
    for year in range(2020, 2029 + 1):
        R20mm_now = data2.PRECT.sel(time='%d' % year)
        R20mm_now = R20mm_now * 1000 * 3600 * 24
        R20mm[year - 2010, :, :] = np.sum(R20mm_now >= 20, axis=0)
    # For p3 (year 2030)
    R20mm_now = data3.PRECT.sel(time='2030')
    R20mm_now = R20mm_now * 1000 * 3600 * 24
    R20mm[20, :, :] = np.sum(R20mm_now >= 20, axis=0)
    return R20mm