import MDAnalysis as mda
from subprocess import call
from tqdm import tqdm


def Dcd2Xtc(psf, dcd):
    psffile = psf
    dcdfile = dcd
    xtcfile = dcdfile[0:-4] + '.xtc'
    u = mda.Universe(psffile, dcdfile)
    with mda.Writer(xtcfile, u.atoms.n_atoms)as w:
        for ts in tqdm(u.trajectory,
                       desc=f'{xtcfile}', leave=False):
            w.write(u)


def RemoveDcd(dcd):
    args = f'rm -rf {dcd}'.split()
    call(args)


if __name__ == '__main__':
    Dcd2Xtc()
