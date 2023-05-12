import pandas as pd
import matplotlib.pyplot as plt

# add abbrevs as x-axis
df = pd.read_excel('/regional_selected_data.xlsx', sheet_name='TN10p', usecols='B')
my_xlabel = df['Abbrevs']

index = ['TN10p', 'TX90p', 'R95pTOT', 'R99pTOT']
unit = ['%', '%', 'mm', 'mm']
label = ['(a)', '(b)', '(c)', '(d)']
label_location = [0.08, 0.85]
my_xlabel = ['SAS', 'SAS', 'EAS', 'SEA', 'WAF', 'MED', 'EAF', 'CEU']
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8.5, 7.1))
plt.subplots_adjust(hspace=0.1, wspace=0.22)

for i in range(2):
    for j in range(2):
        df = pd.read_excel('/regional_selected_data.xlsx',
                           sheet_name=index[i * 2 + j], usecols='D:G')
        ax[i][j].scatter(range(7), df['Base'], s=None, c='Black', label='Base', zorder=8)
        ax[i][j].scatter(range(7), df['Ctrl'], s=None, c='#AC2026', label='Control', zorder=7)
        ax[i][j].scatter(range(7), df['GLENS'], s=None, c='#BD8EC0', label='GLENS', zorder=6)
        ax[i][j].scatter(range(7), df['GLENS_eq'], s=None, c='#6F80BE', label='GLENS_eq', zorder=5)
        ax[i][j].set_ylabel('%s (%s)' % (index[i * 2 + j], unit[i * 2 + j]))
        ax[i][j].annotate(label[i * 2 + j], xy=label_location, xycoords='axes fraction', fontsize=14)
        if i == 0:
            ax[i][j].set_xticklabels([])
            ax[i][j].axhline(10, color='gray', zorder=1, linestyle='dashed')
        else:
            ax[i][j].set_xticklabels(my_xlabel)

ax[0][1].legend()

dot_size = 20
alpha = 0.5
for ensemble in range(3):
    for i in range(2):
        for j in range(2):
            df = pd.read_excel('/regional_selected_data.xlsx',
                               sheet_name=index[i * 2 + j], usecols='H:S')
            ax[i][j].scatter(range(7), df['Base%d' % (ensemble + 1)], s=dot_size, c='Black', alpha=alpha, linewidths=0,
                             zorder=4)
            ax[i][j].scatter(range(7), df['Ctrl%d' % (ensemble + 1)], s=dot_size, c='#AC2026', alpha=alpha,
                             linewidths=0, zorder=3)
            ax[i][j].scatter(range(7), df['GLENS%d' % (ensemble + 1)], s=dot_size, c='#BD8EC0', alpha=alpha,
                             linewidths=0, zorder=2)
            ax[i][j].scatter(range(7), df['GLENS_eq%d' % (ensemble + 1)], s=dot_size, c='#6F80BE', alpha=alpha,
                             linewidths=0, zorder=1)
