import matplotlib.pyplot as plt
import argparse
import numpy as np
import os

PLOT_FILES  = []
PLOT_LABELS = []
X_RANGE = [] # 0.0, 10.0
Y_RANGE = []
EVERY = 1 # default 1
NAME_PICTURE = "test.png" # default "test.png"

plt.rcParams["font.family"] = "Spica Neue"      #全体のフォントを設定
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
plt.rcParams["font.size"] = 14                       #フォントの大きさ
plt.rcParams["axes.linewidth"] = 1.5                 #囲みの太さ

plt.rcParams["legend.markerscale"] = 2
plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["legend.edgecolor"] = 'black'

plt.rcParams['axes.grid']=True
plt.rcParams['grid.linestyle']='--'
# plt.rcParams['grid.linewidth'] = 0.3

#
# parser = argparse.ArgumentParser(description="Fast plot like gnuplot!")
# parser.add_argument("i_files", help="are ploted file.", nargs="*")
# parser.add_argument("-xr", help="x_range ex) -10:10, :100")
# parser.add_argument("-yr", help="y_range ex) -10:10, :100")
# parser.add_argument("-e", help="plot every # ex) 50", default=1)
# parser.add_argument("-pn", help="picture name : ex) dihedral1")
# args = parser.parse_args()

# check file
for i_file in PLOT_FILES:
    if os.path.exists(i_file):
        plot_files.append(np.loadtxt(f"{i_file}"))
    else:
        print(f"Error : {i_file} can't find.")
        os.sys.exit()

# FILE-LABEL
if len(PLOT_FILES) == len(PLOT_LABELS):
    continue
elif:
    print(f"Error : n_PLOT_FILEs and n_PLOT_LABLEs did not match.")
    os.sys.exit()


# plot_setting
fig = plt.figure(figsize=(16,9))
plt.subplots_adjust(wspace=0.3, hspace=0.3)
ax = fig.add_subplot(1,1,1)

for i_file, i_label in zip(PLOT_FILES, PLOT_LABELS):
    ax.plot(i_file[::EVERY, 0], i_file[::EVERY, 1], label=f"{i_label}")

# range set
ax.set_xlim(left = int(X_LANGE[0]), right = int(X_LANGE[1]))
ax.set_ylim(bottom = int(Y_LANGE[0]), top = int(Y_LANGE[1]))

ax.legend(loc="best")
fig.tight_layout()

# save picture
plt.show()
plt.savefig(f"{args.pn}.png")
