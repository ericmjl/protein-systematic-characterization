#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:29:14 2017

@author: vivzhong


Design overlapping DNA tiles from a database of sequence variants for tiled synthesis, 
with annealing overlaps optimized for melting temperatures within 4ºC of each other.
"""


from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp as mt

import numpy as np

SEQ_LENGTH = 2280
TILE_LENGTH = 180 #between overlaps
OVERLAP = 30
TEMPLATE = [seq.seq for seq in SeqIO.parse("victoria-pb2.fasta", "fasta")][0]

num_tiles = np.ceil((SEQ_LENGTH-TILE_LENGTH)/(TILE_LENGTH+OVERLAP))
tile_length = (SEQ_LENGTH-OVERLAP)/num_tiles-OVERLAP
#print(num_tiles, tile_length)
#Melting temperatures of forward and reverse primers
start_overlap = "GATTACAGATTACAGNNNNNAGCAAAAGCAGGTCAATTATATTCAGT" #47 bp, UTR before start codon
end_overlap = "TGCTGAATAGTTTAAAAACGACCTTGTTTCTACNNNNNGATTACAGATTACAG" #33 bp, UTR after stop codon

print("5' primer: ", mt.Tm_GC(Seq(start_overlap), strict=False))
print("3' primer: ", mt.Tm_GC(Seq(end_overlap), strict=False))


def get_seqs(variants_file):
    """
    variant_file: fasta file of PB2 sequences
    
    Returns: list of SeqRecords for all PB2 sequences in fasta file
    """
    all_seq = []
    for i, seq in enumerate(SeqIO.parse(variants_file, "fasta")):
        #trim sequences to ORF
        if str(seq.seq)[0:3] != "ATG":
            for index, base in enumerate(seq.seq):
                if seq.seq[index:index+3] == "ATG":
                    start = index
                    break
        else:
            start = 0
        seq.seq = seq.seq[start:start+SEQ_LENGTH]
        all_seq.append(seq)   
    return all_seq

#%%

def generate_tiles(get_seqs, tile_length, overlap, vic):
    """
    tile_length (int): the length of variable DNA per fragment
    overlap (int): length of overlap between tile fragments
    TEMPLATE (str): PB2 sequence to use for overlap
    
    Tm Optimization: From get_anneal_tm, get the highest Tm (max_tm) of all the annealing
                overlaps in the sequence (approximate with Vic sequence). When 
                generating tiles for the first sequence, bases are added to 
                overlap sequences until the Tm of the overlap is within 4ºC
                of the max_tm and saves the length of that overlap to a dictionary
                by tile number. All subsequent sequences pull from that dictionary. 
                
    
    Returns: dictionary where keys are the id of the original PB2 sequence 
                and values are tuples of lists of the tiles generated from those sequences, 
                where the first list is the forward and the second is the reverse
    """
    tiles = {}
    for seq in get_seqs:
        seq_tiles = []
        #rev_tiles = []
        for i in range(0, len(seq.seq)-1, tile_length+overlap):
            if i == 0:
                new_tile = Seq(start_overlap) + seq.seq[i:i+tile_length] + seq.seq[i+tile_length:i+tile_length+overlap]
            elif i == len(seq.seq)-tile_length:
                new_tile = seq.seq[i-overlap:i] + seq.seq[i:i+tile_length] + Seq(end_overlap)
            else:
                new_tile = seq.seq[i-overlap:i] + seq.seq[i:i+tile_length] + seq.seq[i+tile_length:i+tile_length+overlap]
            seq_tiles.append(str(new_tile))
            #rev_tiles.append(str(new_tile.reverse_complement()))
        tiles[seq.id] = seq_tiles
    return tiles

tiles = generate_tiles(get_seqs("AllUniqueDNA.fasta"), TILE_LENGTH, OVERLAP, TEMPLATE)
print(tiles['gb:KT838064|Organism:Influenza'])

#find the number of unique end fragments
first_tiles = []
for seqs in tiles.values():
    first_tiles.append(str(seqs[0]))
unique = np.unique(first_tiles)
print("Unique 5' end fragments: ", len(unique))

last_tiles = []
for seqs in tiles.values():
    last_tiles.append(str(seqs[-1]))
unique = np.unique(last_tiles)
print("Unique 3' end fragments: ", len(unique))
# In[14]:

#Range and mean of melting temperatures of tiles
#tm = []
#for seq_tup in tiles.values():
#    for seq_list in seq_tup:
#        for seq in seq_list:
#            tm.append(mt.Tm_GC(Seq(seq), strict=False))
#            
#print("Range:", max(tm) - min(tm), "Mean:", sum(tm)/len(tm))