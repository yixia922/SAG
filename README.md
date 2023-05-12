# SAG

该项目采用了两个数据集来计算刻画全球极端天气情况的[ETCCDI](http://etccdi.pacificclimate.org/indices.shtml)指数：

1. [Geoengineering Large Ensemble Project (GLENS)](https://doi.org/10.5065/D6JH3JXX)
2. [UN WPP-Adjusted Population Count, v4.11 (2020)](https://doi.org/10.7927/H4PN93PB)



## 文件夹说明

### **指数计算 indices_calculation**

| 时间段缩写 |                         |
| ---------- | ----------------------- |
| BASE       | 2010-2030年（包含首尾） |
| END        | 2075-2095年（包含首尾） |

"indices_calculation"文件中各代码脚本所能计算的指数，注意两时间段的指数计算需使用不同的脚本，可根据脚本名称开头的BASE/END区分。其中针对相对阈值指数（TN10p、TN90p、TX10p、TX90p、R95pTOT、R99pTOT），需先利用“Percentile”脚本文件计算各地的相对阈值，再运行对应计算指数的脚本。

| 脚本文件名             | 计算指数                                                     |
| ---------------------- | ------------------------------------------------------------ |
| BASE                   | TNn、TXn、TNx、TXx、FD、ID、TR、SU、PRECPTOT、SDII、Rx1day、Rx5day、R10mm、R20mm |
| END                    | TNn、TXn、TNx、TXx、FD、ID、TR、SU、PRECPTOT、SDII、Rx1day、Rx5day、R10mm、R20mm |
| BASE-percentile-temp   | TN10p、TN90p、TX10p、TX90p                                   |
| END-percentile-temp    | TN10p、TN90p、TX10p、TX90p                                   |
| BASE-percentile-percip | R95pTOT、R99pTOT                                             |
| END-percentile-percip  | R95pTOT、R99pTOT                                             |
| BASE-CDDCWD            | CDD、CWD                                                     |
| END-CDDCWD             | CDD、CWD                                                     |
| *Percentile            | 相对阈值指数中各地的相对阈值                                 |

### 平均气候态作图 Fig_mean

"map"用于绘制气候变量的全球平均分布图。

"latitudinal_distribution"用于绘制气候变量随纬度的分布曲线。

"PDFs"用于绘制概率密度函数分布图。

### 极端天气指数作图 Fig_extreme

"map_2rows"与"map_4rows"均用于绘制极端天气指数的全球分布图，但前者在单一图像中能刻画两个极端天气指数，而后者在单一图像中能刻画四个极端天气指数。

### 分区域极端天气指数作图 Fig_regional

"regional_selected_data.xlsx"为按照IPCC SREX陆地部分地域分区，挑选出人口数量大于3亿的地区，分别计算其极端天气指数（TN10p、TX90p、R95pTOT、R99pTOT）平均值的结果。

"Dot_plot"用于绘制表格中四个极端天气指数在各筛选地区平均值的点图。

### 自定义函数 Functions

包含以上脚本所调用的所有自定义函数。
