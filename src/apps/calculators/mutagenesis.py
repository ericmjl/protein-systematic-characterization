"""
Computes necessary volumes for mutagenesis.
"""

import numpy as np
import math


def input_plasmid_mass(target_len, plasmid_len, target_mass):
    """
    Computes the mass of total input plasmid mass required to get a given mass
    of target DNA.

    Silently assumes that the units are:
    - target_len: bp (base pairs)
    - plasmid_len: bp (base pairs)
    - target_mass: ng (nanograms)
    """
    return target_mass * plasmid_len / target_len


def input_volume(input_mass, input_conc):
    """
    Computes the required amount of volume for a given mass and concentration.

    Silently assumes that the units are:
    - input_mass: ng (nanograms)
    - input_conc: ng/µL (nanograms per microlitre)
    """
    return input_mass / input_conc


def num_cycles(fold_amp):
    """
    Computes the necessary number of cycles. Rounds up to the next integer.
    """
    return math.ceil(np.log10(fold_amp) / np.log10(2))
