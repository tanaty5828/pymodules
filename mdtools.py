import MDAnalysis as mda
from MDAnalysis.analysis import polymer

def PersistenceLengthDNA(u_):
    PH_beads = u_.select_atoms('name PH')
    PB_beads = u_.select_atoms('name PB')
    if PH_beads.n_atoms > 0:
        dnas = [PH_beads, PH_beads]
    elif PB_beads.n_atoms > 0:
        dnas = [PB_beads, PB_beads]
    else:
        print('I cant find backbone P beads!!')

    # Persistance
    per = polymer.PersistenceLength(dnas).run()
    return per.lp / 10.  # convert to nm

def RadiusOfGyration(atoms_):
    return atoms_.radius_of_gyration() / 10.

def EndToEndDist(i_atom, j_atom):
    dist = mda.lib.distances.distance_array(i_atom.position, j_atom.position)
    return dist / 10.
