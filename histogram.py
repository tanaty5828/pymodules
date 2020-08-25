def normal_output(data_, range_, bins_, filename_="temp.dat"):
    import numpy as np

    if filename_ == "temp.dat":
        print("Can't find argument of filename. Write it as 'temp.dat'")

    histogram_ = np.histogram(data_, range=range_, bins=bins_)
    hist_x_ = [(histogram_[1][i] + histogram_[1][i+1]) / 2. for i in range(0, len(histogram_[0]))]
    # normalize
    y_sum = np.sum(histogram_[0])
    hist_y_ = histogram_[0] / float(y_sum)
    hist_output_ = np.stack([hist_x_, hist_y_], 1)
    np.savetxt(filename_, hist_output_)


def make_hist(data_, range_, bins_ ):
    import numpy as np

    histogram_ = np.histogram(data_, range=range_, bins=bins_)
    hist_x_ = [(histogram_[1][i] + histogram_[1][i+1]) / 2. for i in range(0, len(histogram_[0]))]
    hist_y_ = histogram_[0]
    hist = np.vstack((hist_x_, hist_y_)).T
    return hist
