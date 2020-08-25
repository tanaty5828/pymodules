import matplotlib.pyplot as plt
import argparse
import numpy as np
import os

plt.rcParams["font.family"] = "Liberation Serif"      #全体のフォントを設定
# plt.rcParams["font.family"] = "Times New Roman"      #全体のフォントを設定
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
plt.rcParams["font.size"] = 30                       #フォントの大きさ
plt.rcParams["axes.linewidth"] = 1.5                 #囲みの太さ
plt.rcParams["legend.markerscale"] = 2
plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["legend.edgecolor"] = 'black'
plt.rcParams['axes.grid']=True
plt.rcParams['grid.linestyle']='--'
plt.rcParams['legend.framealpha'] = 0.5


def cg_plot(axes, index_figure, data):
    axes[index_figure].plot(data[:, 0], data[:, 1], color='C0', label='CG')


def aa_plot(axes, index_figure, data):
    axes[index_figure].plot(data[:, 0], data[:, 1], linestyle='--', color='C0', label='AA')

axes = []
fig = plt.figure(figsize=(14, 10))
plt.subplots_adjust(wspace=0.0, hspace=0.0)

dope_filenames = ['DOPE-DOPE',
                  'CHL1-DOPE',
                  'CHL1-CHL1']

dotap_filenames = ['DOTA-DOTA',
                   'CHL1-DOTA',
                   'CHL1-CHL1']

for i, name_i in enumerate(dope_filenames, start=1):
    axes.append(fig.add_subplot(2, 3, i))
    axes[i-1].set_title(name_i, fontsize=30)
    data = np.loadtxt(f'./RDFG2D_{name_i}.dat')
    cg_plot(axes, i-1, data)
    data = np.loadtxt(f'/home/tanaka/AA/DOPE-CHOL/namd/RDFG2D_{name_i}.dat')
    aa_plot(axes, i-1, data)

for i, name_i in enumerate(dotap_filenames, start=4):
    axes.append(fig.add_subplot(2, 3, i))
    axes[i-1].set_title(name_i, fontsize=30)
    data = np.loadtxt(f'/home/tanaka/CG/DOTAP-CHOL/RDFG2D_{name_i}.dat')
    cg_plot(axes, i-1, data)
    data = np.loadtxt(f'/home/tanaka/AA/DOTAP-CHOL/namd/RDFG2D_{name_i}.dat')
    aa_plot(axes, i-1, data)

axes[0].legend(loc='best', fontsize=15)
axes[3].set_ylabel('g(r)[-]')
axes[4].set_xlabel(r'r[$\AA$]')
for i in range(0, 6):

    axes[i].set_xlim(0, 20)
    axes[i].set_ylim(0, 2.5)

# axes[1].set_yticks(np.linspace(dotap_fig_lim[0], dotap_fig_lim[1], 3))
# axes[1].set_xlim(0, 100)
# axes[1].set_ylim(dotap_fig_lim[0], dotap_fig_lim[1])
# axes[1].set_title('DOTAP-CHOL')

#     axes[i].set_xlabel('Time [ns]')
#     axes[i].set_ylabel(r'Area / lipid [$\AA$]')

plt.tight_layout()
plt.show()
# plt.savefig('RDFG2D_DOPE_DOTAP_CHL1.svg')

