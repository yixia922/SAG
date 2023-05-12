def get_fullname(var_name):
    if var_name == 'TS':
        return 'Surface Temperature'
    elif var_name == 'TREFHT':
        return '2m Tempreature'
    elif var_name == 'PRECT':
        return 'Precipitation Rate'
    elif var_name == 'PE':
        return 'Precip minus Evap'
    elif var_name == 'QRUNOFF':
        return 'Total Liquid Runoff'
    elif var_name == 'SOILMOI':
        return 'Soil Moisture'
    elif var_name == 'NPP':
        return 'Net Primary Production'
    elif var_name == 'GPP':
        return 'Gross Primary Production'


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


def get_cmap(var):
    if var in ['TNn', 'TXn', 'TNx', 'TXx', 'TR', 'SU', 'TN90p', 'TX90p']:
        return 'RdBu_r'
    elif var in ['TN10p', 'TX10p', 'FD', 'ID']:
        return 'RdBu'
    elif var in ['PRCPTOT', 'Rx5day', 'CWD', 'R10mm', 'R20mm', 'R95pTOT', 'R99pTOT']:
        return 'BrBG'
    elif var in ['CDD']:
        return 'BrBG_r'


def change_unit(xr_obj, var_name):
    if var_name in ['TS', 'TREFHT']:
        return xr_obj - 273.15     # K -> celsius
    elif var_name in ['PRECT', 'PRECL', 'PE', 'QRUNOFF']:
        return xr_obj * 1000 * 3600 * 24     # m/s -> mm/day
    elif var_name in ['GPP', 'NPP']:
        # gC/m2/s -> kgC/m2/year
        return xr_obj * 0.001 * 3600 * 24 * 365      # gC/m2/s -> kgC/m2/year
    else:
        return xr_obj

