import numpy as np
import argparse


def RetMeanStd(filename):
    data_array = np.loadtxt(filename)
    ave = np.mean(data_array[:, 1])
    std = np.std(data_array[:, 1])
    print(f'ave = {ave}', f'std = {std}')
    return ave, std


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description="This script calculate average and std")
    parser.add_argument("-f", "--files",
                        nargs='*',
                        help="value_files",
                        required=True)
    args = parser.parse_args()

    for i_file in args.files:
        print(i_file)
        RetMeanStd(i_file)
