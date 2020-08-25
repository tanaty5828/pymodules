import MDAnalysis as mda
from tqdm import tqdm
import argparse
import warnings
warnings.filterwarnings('ignore')


def PruneWater(coord, trj):
    print(f'Loading Trajectories...', end='')
    u = mda.Universe(coord, trj)
    print(f'OK')

    u = mda.Universe(coord, trj)
    nowat_trj = u.select_atoms('not (name W or name WAT or name TIP3 or resname SOL)')
    print(f'The system contains {set(nowat_trj.residues.resnames)}')
    nowat_trj.write('nowat_merged.pdb')
    with mda.Writer('nowat_merged.xtc', n_atoms=nowat_trj.n_atoms)as W:
        for ts in tqdm(u.trajectory):
            W.write(nowat_trj)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Remove water from trajectory")
    parser.add_argument("-p", "--psf", help="toporogy like psf", required=True)
    parser.add_argument(
        "-t",
        "--trajectory",
        help="trajectory like .dcd .xtc",
        required=True,
        nargs='*')
    args = parser.parse_args()

    PruneWater(args.psf, args.trajectory)
