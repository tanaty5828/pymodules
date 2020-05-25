import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import argparse
import numpy as np
import os
from io import StringIO


plt.rcParams["font.family"] = "Spica Neue"  # 全体のフォントを設定
plt.rcParams["xtick.direction"] = "in"  # x軸の目盛線を内向きへ
plt.rcParams["ytick.direction"] = "in"  # y軸の目盛線を内向きへ
plt.rcParams["xtick.minor.visible"] = True  # x軸補助目盛りの追加
plt.rcParams["ytick.minor.visible"] = True  # y軸補助目盛りの追加
plt.rcParams["xtick.major.width"] = 1.5  # x軸主目盛り線の線幅
plt.rcParams["ytick.major.width"] = 1.5  # y軸主目盛り線の線幅
plt.rcParams["xtick.minor.width"] = 1.0  # x軸補助目盛り線の線幅
plt.rcParams["ytick.minor.width"] = 1.0  # y軸補助目盛り線の線幅
plt.rcParams["xtick.major.size"] = 10  # x軸主目盛り線の長さ
plt.rcParams["ytick.major.size"] = 10  # y軸主目盛り線の長さ
plt.rcParams["xtick.minor.size"] = 5  # x軸補助目盛り線の長さ
plt.rcParams["ytick.minor.size"] = 5  # y軸補助目盛り線の長さ
plt.rcParams["font.size"] = 14  # フォントの大きさ
plt.rcParams["axes.linewidth"] = 1.5  # 囲みの太さ

plt.rcParams["legend.markerscale"] = 2
plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["legend.edgecolor"] = 'black'

plt.rcParams['axes.grid'] = True
plt.rcParams['grid.linestyle'] = '--'
# plt.rcParams['grid.linewidth'] = 0.3

# plt.figure(dpi=200)                 # size of figure, resolution
#
parser = argparse.ArgumentParser(description="Fast plot like gnuplot!")
parser.add_argument("i_files", help="are ploted file.", nargs="*")
parser.add_argument("-u",  help="which column # ex) 1:3", default="1:2")
parser.add_argument("-xr", help="x_range ex) -10:10, :100")
parser.add_argument("-yr", help="y_range ex) -10:10, :100")
parser.add_argument("-e",  help="plot every # ex) 50", default=1)
parser.add_argument("-xt", help="xtics every # ex) 45")
parser.add_argument("-yt", help="ytics every # ex) 0.1")
parser.add_argument("-pn", help="picture name : ex) dihedral1")
args = parser.parse_args()

plot_every = int(args.e)
plot_files = []

# check file
for i_file in args.i_files:
    if os.path.exists(i_file):

        # deal with comment
        with open(i_file, "r")as f:
            string = f.read()
        string = string.replace("@", "#")
        string = string.replace("!", "#")
        string = StringIO(string)

        if i_file[-3:] == 'csv':  # deal with to csv file
            plot_files.append(np.loadtxt(string, delimiter=','))

        else:
            plot_files.append(np.loadtxt(string))

    else:
        print(f"Error : {i_file} can't find.")
        os.sys.exit()
# plot_setting
fig = plt.figure(figsize=(14, 10))
plt.subplots_adjust(wspace=0.3, hspace=0.3)
ax = fig.add_subplot(1, 1, 1)

# column set
columns = args.u.split(":")
columns = list(map(int, columns))
columns = list(map(lambda x: x-1, columns))  # u 1:2 is use 0:1

for j_filename, j_file in zip(args.i_files, plot_files):
    ax.plot(j_file[::plot_every, columns[0]],
            j_file[::plot_every, columns[1]], label=f"{j_filename}")

# xrange set
try:
    x_ran = args.xr
    # print(int(x_ran.split(":")[1]))
# start
    if x_ran[-1] == ":":
        ax.set_xlim(left=int(x_ran.split(":")[0]))
    elif x_ran[0] == ":":
        ax.set_xlim(right=int(x_ran.split(":")[1]))
    else:
        x_ran = x_ran.split(":")
        ax.set_xlim(left=int(x_ran[0]), right=int(x_ran[1]))
except:
    pass

# yrange set
try:
    y_ran = args.yr
# start
    if y_ran[-1] == ":":
        ax.set_ylim(bottom=int(y_ran.split(":")[0]))
    elif y_ran[0] == ":":
        ax.set_ylim(top=int(y_ran.split(":")[1]))
    else:
        y_ran = y_ran.split(":")
        ax.set_ylim(bottom=int(y_ran[0]), top=int(y_ran[1]))
except:
    pass

# ticks
try:
    xtics = args.xt
    ax.xaxis.set_major_locator(ticker.MultipleLocator(float(xtics)))
except:
    pass

try:
    ytics = args.yt
    ax.yaxis.set_major_locator(ticker.MultipleLocator(float(ytics)))
except:
    pass


ax.legend(loc="best")
fig.tight_layout()

# save picture
if args.pn == None:
    plt.show()
else:
    plt.savefig(f"{args.pn}.png")
