import MDAnalysis as mda
from tqdm import tqdm
import argparse
import warnings
warnings.filterwarnings('ignore')


def WriteLastPdb(psf, trj):
    outname = trj[0:-4] + '.pdb'

    print(f'Loading Trajectories...', end='')
    u = mda.Universe(psf, trj)
    print(f'OK')

    atoms = u.select_atoms('all')
    atoms.write(outname, bonds=None, frames=u.trajectory[-1:])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Remove water from trajectory")
    parser.add_argument("-p", "--psf", help="toporogy like psf", required=True)
    parser.add_argument(
        "-t",
        "--trajectory",
        help="trajectory like .dcd .xtc",
        required=True)
    args = parser.parse_args()

    WriteLastPdb(args.psf, args.trajectory)
