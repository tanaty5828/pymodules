def plot_init():
    import matplotlib.pyplot as plt
    global plt
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
    # plt.figure(dpi=200)                 # size of figure, resolution
    plt.rcParams["legend.markerscale"] = 2
    plt.rcParams["legend.fancybox"] = False
    plt.rcParams["legend.framealpha"] = 1
    plt.rcParams["legend.edgecolor"] = 'black'

    plt.rcParams['axes.grid']=True
    plt.rcParams['grid.linestyle']='--'
