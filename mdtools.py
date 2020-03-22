import MDAnalysis as mda
from MDAnalysis.analysis import polymer


def PersistenceLengthDNA(u_):
    PH_beads = u_.select_atoms('name PH or name RB1 or name DB2 or name RB2')
    PB_beads = u_.select_atoms('name PB or name RB1 or name DB2 or name RB2')
    if PH_beads.n_atoms > 39:
        dnas = [PH_beads, PH_beads]
    elif PB_beads.n_atoms > 39:
        dnas = [PB_beads, PB_beads]
    else:
        print('I cant find backbone P beads!!')

    # Persistance
    per = polymer.PersistenceLength(dnas).run()
    return per.lp / 10.  # convert to nm


def RadiusOfGyration(atoms_):
    return atoms_.radius_of_gyration() / 10.  # convert to nm


def EndToEndDist(i_atom, j_atom):
    dist = mda.lib.distances.distance_array(i_atom.position, j_atom.position)
    return dist / 10.  # convert to nm


def IonNumMolecules(density_molar, box_len_ang):
    N_avogadro = 6.02214086e+23
    n_ions = density_molar * N_avogadro * ((box_len_ang * 1e-10) ** 3.) * 1e3
    return n_ions
