import MDAnalysis as mda
import argparse


def Pdb2gmx(file_pdb, o_name, file_psf):
    if file_psf is None:
        u = mda.Universe(file_pdb)
        u.atoms.write(f'{o_name}', reindex=False)
    else:
        u = mda.Universe(file_psf, file_pdb)
        u.atoms.write(f'{o_name}', reindex=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Convert pdb to gro file")
    parser.add_argument("-p", "--psf", help="psf filename")
    parser.add_argument("-c", "--pdb", help="pdb filename", required=True)
    parser.add_argument(
        "-o",
        "--out",
        help="output gro filename",
        default='system.gro')
    args = parser.parse_args()

    Pdb2gmx(args.pdb, args.out, args.psf)
