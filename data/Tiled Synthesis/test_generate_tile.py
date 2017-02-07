#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:34:14 2017

@author: vivzhong

To be run after generate_tile.py. 
"""
from Bio import SeqIO
import generate_tiles as gt
import math

SEQ_LENGTH = 2280
VARIABLE_TILE_LENGTH = 180
OVERLAP = 30
TEMPLATE = [seq.seq for seq in SeqIO.parse("victoria-pb2.fasta", "fasta")][0]

num_tiles = math.ceil(SEQ_LENGTH/(VARIABLE_TILE_LENGTH+OVERLAP))

tiles = gt.generate_tiles(gt.get_seqs("AllUniqueDNA.fasta"), VARIABLE_TILE_LENGTH, OVERLAP, TEMPLATE, max(gt.get_anneal_tm(gt.get_seqs("AllUniqueDNA.fasta"), 180, 30, TEMPLATE)))

def test_ATG():
    num_errors = 0
    for seqs in tiles.values():
        if str(seqs[0][0]) != "ATG":
            num_errors += 1
    assert num_errors == 0, "{0} sequences do not begin with ATG.".format(num_errors)
def test_num_tiles():
    num_errors = 0
    for seq_pairs in tiles.values():
        for tile_set in seq_pairs:
            if len(tile_set) != num_tiles:
                num_errors +=1 
    assert num_errors == 0, "{0} sets of tiles do not have the right number of tiles.".format(num_errors)

