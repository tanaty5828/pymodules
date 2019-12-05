import matplotlib.pyplot as plt
import argparse
import numpy as np
import os

PLOT_FILES  = ['../Adenine/merge/normal_ade_dope11272032.pmf',
               '/home/tanaka/CG/TransferFE/PMF/normal_ade_dope.pmf']
PLOT_LABELS = ['CG', 'AA']
X_RANGE = [0.0, 30.0] # 0.0, 10.0
Y_RANGE = [-1.0, 8.0]
EVERY = 1 # default 1
COLORS = ['#048D91',  # green
          '#FF3E00']  # orenge
NAME_PICTURE = "dope_ade.png" # default "test.png"

# plt.rcParams["font.family"] = "Spica Neue"      #全体のフォントを設定
plt.rcParams["font.family"] = "Times New Roman"      #全体のフォントを設定
plt.rcParams["xtick.direction"] = "in"               #x軸の目盛線を内向きへ
plt.rcParams["ytick.direction"] = "in"               #y軸の目盛線を内向きへ
plt.rcParams["xtick.minor.visible"] = True           #x軸補助目盛りの追加
plt.rcParams["ytick.minor.visible"] = True           #y軸補助目盛りの追加
plt.rcParams["xtick.major.width"] = 1.5              #x軸主目盛り線の線幅
plt.rcParams["ytick.major.width"] = 1.5              #y軸主目盛り線の線幅
plt.rcParams["xtick.minor.width"] = 1.0              #x軸補助目盛り線の線幅
plt.rcParams["ytick.minor.width"] = 1.0              #y軸補助目盛り線の線幅
plt.rcParams["xtick.major.size"] = 10                #x軸主目盛り線の長さ
plt.rcParams["ytick.major.size"] = 10                #y軸主目盛り線の長さ
plt.rcParams["xtick.minor.size"] = 5                 #x軸補助目盛り線の長さ
plt.rcParams["ytick.minor.size"] = 5                 #y軸補助目盛り線の長さ
plt.rcParams["font.size"] = 20                       #フォントの大きさ
plt.rcParams["axes.linewidth"] = 1.5                 #囲みの太さ

plt.rcParams["legend.markerscale"] = 2
plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["legend.edgecolor"] = 'black'

plt.rcParams['axes.grid']=True
plt.rcParams['grid.linestyle']='--'
# plt.rcParams['grid.linewidth'] = 0.3

#  load
#

# FILE-LABEL
if len(PLOT_FILES) == len(PLOT_LABELS):
    PLOT_FILES = [np.loadtxt(i) for i in PLOT_FILES]
else:
    print(f"Error : n_PLOT_FILEs and n_PLOT_LABLEs did not match.")
    os.sys.exit()


# plot_setting
fig = plt.figure(figsize=(16,9))
plt.subplots_adjust(wspace=0.3, hspace=0.3)
ax = fig.add_subplot(1,1,1)

for i_file, i_label in zip(PLOT_FILES, PLOT_LABELS):
    if i_label == 'CG':
        ax.plot(i_file[::EVERY, 0], i_file[::EVERY, 1],
                color = '#048D91',
                linewidth = 3.0,
                label=f"{i_label}")
    elif i_label == 'AA':
        ax.plot(i_file[::EVERY, 0], i_file[::EVERY, 1],
                color = '#048D91',
                linestyle = 'dashed',
                linewidth = 3.0,
                label=f"{i_label}")

# range set
ax.set_xlim(left = int(X_RANGE[0]), right = int(X_RANGE[1]))
ax.set_ylim(bottom = int(Y_RANGE[0]), top = int(Y_RANGE[1]))

# axis label set
ax.set_xlabel('Z [$\AA$]')
ax.set_ylabel('$\Delta$G [kcal/mol]')


ax.legend(loc="best")
fig.tight_layout()

# save picture
plt.savefig(NAME_PICTURE)
plt.show()
