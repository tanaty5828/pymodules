import MDAnalysis as mda
from makeanalydir import MakeAnalyDir
from tqdm import tqdm
import argparse
import warnings
warnings.filterwarnings('ignore')

MakeAnalyDir('Trajs')


def TrjSplitWrite(u_, frame_each=100):
    all_atomgroup = u_.select_atoms('all')
    last_step = u_.trajectory[-1].frame
    n_files = last_step // frame_each
    for i, (start_frame, stop_frame) in enumerate(zip(tqdm((range(0, last_step + 1, frame_each)), desc='Split'),
                                                      range(frame_each, last_step + 1, frame_each))):
        i = str(i).zfill(len(str(n_files)))  # if n_files is 100, i is 001
        with mda.Writer(f"./Trajs/traj_{i}.xtc", all_atomgroup.n_atoms)as W:
            for ts in u_.trajectory[start_frame: stop_frame]:
                W.write(all_atomgroup)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="This script calculate PersistenceLength and End-to-end distance")
    parser.add_argument("-p", "--psf",
                        help="toporogy like psf", required=True)
    parser.add_argument("-t", "--trajectory",
                        help="trajectory like .dcd .xtc", required=True, nargs='*')
    parser.add_argument('-f', '--frames',
                        help='n_frames', default=100)
    args = parser.parse_args()
    PSFFILE = args.psf
    TRJFILE = args.trajectory
    u = mda.Universe(PSFFILE, TRJFILE)

    TrjSplitWrite(u, int(args.frames))
