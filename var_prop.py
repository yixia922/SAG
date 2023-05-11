def get_fullname(var_name):
    if var_name == 'TS':
        fullname = 'Surface Temperature'
    elif var_name == 'TREFHT':
        fullname = '2m Tempreature'
    elif var_name == 'PRECT':
        fullname = 'Precipitation Rate'
    elif var_name == 'PE':
        fullname = 'Precip minus Evap'
    elif var_name == 'QRUNOFF':
        fullname = 'Total Liquid Runoff'
    elif var_name == 'SOILMOI':
        fullname = 'Soil Moisture'
    elif var_name == 'NPP':
        fullname = 'Net Primary Production'
    elif var_name == 'GPP':
        fullname = 'Gross Primary Production'
    return fullname

def get_unit(var_name):
    if var_name in ['TS', 'TREFHT']:
        return '($^\circ$C)'
    elif var_name in ['PRECT', 'PE', 'QRUNOFF']:
        return '(mm/day)'
    elif var_name == 'SOILMOI':
        return '(kg m$^{-2}$)'
    elif var_name in ['NPP', 'GPP']:
        return '(kg C m$^{-2}$ year$^{-1}$)'
    elif var_name in ['TNn', 'TXn', 'TNx', 'TXx']:
        return '($^\circ$C)'
    elif var_name in ['FD', 'ID', 'TR', 'SU', 'CDD', 'CWD', 'R10mm', 'R20mm']:
        return '(days)'
    elif var_name in ['PRCPTOT', 'SDII', 'Rx1day', 'Rx5day', 'R95pTOT', 'R99pTOT']:
        return '(mm)'
    elif var_name in ['TN10p', 'TN90p', 'TX10p', 'TX90p']:
        return '(%)'

def get_cmap(var_name, if_change):
    if if_change == 1:
        if var_name in ['TS', 'TREFHT']:
            cmap = "RdBu_r"
        elif var_name in ['PRECT', 'PE', 'SOILMOI', 'QRUNOFF', 'NPP', 'GPP']:
            cmap = "BrBG"
        else:
            cmap = "PuBu_r"
    else:
        if var_name in ['TS', 'TREFHT']:
            cmap = "RdBu_r"
        elif var_name in ['PRECT', 'PE']:
            cmap = "BuGn"
        elif var_name in ['SOILMOI']:
            cmap = "Blues"
        elif var_name == 'QRUNOFF':
            cmap = "BrBG"
        elif var_name in ['NPP', 'GPP']:
            cmap = "PuBuGn"
        else:
            cmap = "PuBu_r"
    return cmap

def change_unit(xr_obj, var_name):
    if var_name in ['TS', 'TREFHT']:
        # K -> celsius
        changed = xr_obj - 273.15
    elif var_name in ['PRECT', 'PRECL', 'PE', 'QRUNOFF']:
        # m/s -> mm/day
        changed = xr_obj * 1000 * 3600 * 24
    elif var_name in ['GPP', 'NPP']:
        # gC/m2/s -> kgC/m2/year
        changed = xr_obj * 0.001 * 3600 * 24 * 365
    else:
        changed = xr_obj
    return changed

