""""
Author: Vivian Zhong
Date: 01/30/2017

Design overlapping DNA tiles from a database of sequence variants for tiled synthesis, 
with annealing overlaps optimized for melting temperatures within 4ºC of each other.

""""

# In[10]:

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp as mt

import numpy as np
vic = [seq.seq for seq in SeqIO.parse("victoria-pb2.fasta", "fasta")][0]

#Melting temperatures of forward and reverse primers
start_overlap = "NNNNNAGCAAAAGCAGGTCAATTATATTCAGT" #27 bp, UTR before start codon
end_overlap = "TGCTGAATAGTTTAAAAACGACCTTGTTTCTACNNNNN" #33 bp, UTR after stop codon

print("5' primer: ", mt.Tm_GC(Seq(start_overlap), strict=False))
print("3' primer: ", mt.Tm_GC(Seq(end_overlap), strict=False))


# In[11]:

def get_anneal_tm(get_seqs, tile_length, overlap, vic):
    """
    get_seqs: all the sequences in the fasta file, returned from the eponymous function
    tile_length (int): the length of variable DNA per fragment
    overlap (int): length of overlap between tile fragments
    vic (str): PB2 sequence to use for overlap
    
    Returns: list of melting temperatures of annealing overlaps between tiles
    """
    tm = []
    seq = get_seqs[0]
    for i in range(0, len(seq.seq)-1, tile_length+overlap):
        if i == 0:
            anneal = vic[i+tile_length:i+tile_length+overlap]            
        elif i == len(seq.seq)-tile_length:
            anneal = vic[i-overlap:i]
        else:
            anneal = vic[i-overlap:i]
        tm.append(mt.Tm_GC(anneal))
    return tm
tm = get_anneal_tm(get_seqs("AllUniqueDNA.fasta"), 180, 30, vic)
print("Range:", max(tm) - min(tm), "Mean:", sum(tm)/len(tm))
sorted(tm)


# In[12]:

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
        seq.seq = seq.seq[start:start+2280]
        all_seq.append(seq)   
    return all_seq
def generate_tiles(get_seqs, tile_length, overlap, vic, max_tm):
    """
    tile_length (int): the length of variable DNA per fragment
    overlap (int): length of overlap between tile fragments
    vic (str): PB2 sequence to use for overlap
    
    Returns: dictionary where keys are the id of the original PB2 sequence 
                and values are tuples of lists of the tiles generated from those sequences, 
                where the first list is the forward and the second is the reverse
    """
    new_overlap = overlap
    tiles = {}
    best_anneal = {}
    for seq in get_seqs:
        seq_tiles = []
        rev_tiles = []
        for i in range(0, len(seq.seq)-1, tile_length+overlap):
            if i == 0:
                if i not in best_anneal.keys(): 
                    anneal = vic[i+tile_length:i+tile_length+overlap]
                    while mt.Tm_GC(anneal) < max_tm-4:
                        
                        new_overlap += 1
                        anneal = vic[i+tile_length:i+tile_length+new_overlap]
                    best_anneal[i] = anneal
                else:
                    anneal = best_anneal[i]
                new_tile = Seq(start_overlap) + seq.seq[i:i+tile_length] + anneal
            elif i == len(seq.seq)-tile_length:
                if i not in best_anneal.keys(): 
                    anneal = vic[i-overlap:i]
                    while mt.Tm_GC(anneal) < max_tm:
                        new_overlap += 1
                        anneal = vic[i-new_overlap:i]         
                    best_anneal[i] = anneal
                else:
                    anneal = best_anneal[i]
                new_tile = anneal + seq.seq[i:i+tile_length] + Seq(end_overlap)
            else:
                if i not in best_anneal.keys(): 
                    anneal = vic[i+tile_length:i+tile_length+overlap]
                    while mt.Tm_GC(anneal) < max_tm:
                        new_overlap += 1
                        anneal = vic[i+tile_length:i+tile_length+new_overlap]                       
                    best_anneal[i] = anneal
                else:
                    anneal = best_anneal[i]
                new_tile = best_anneal[i-(tile_length+overlap)] + seq.seq[i:i+tile_length] + vic[i+tile_length:i+tile_length+overlap]
            seq_tiles.append(str(new_tile))
            rev_tiles.append(str(new_tile.reverse_complement()))
        tiles[seq.id] = (seq_tiles, rev_tiles)
    return tiles
tiles = generate_tiles(get_seqs("AllUniqueDNA.fasta"), 180, 30, vic, max(get_anneal_tm(get_seqs("AllUniqueDNA.fasta"), 180, 30, vic)))
tiles


# In[13]:

#find the number of unique end fragments
first_tiles = []
for seqs in tiles.values():
    first_tiles.append(str(seqs[0][0]))
unique = np.unique(first_tiles)
print("Unique 5' end fragments: ", len(unique))

last_tiles = []
for seqs in tiles.values():
    last_tiles.append(str(seqs[0][-1]))
unique = np.unique(last_tiles)
print("Unique 3' end fragments: ", len(unique))


# In[14]:

#Range and mean of melting temperatures of tiles
tm = []
for seq_tup in tiles.values():
    for seq_list in seq_tup:
        for seq in seq_list:
            tm.append(mt.Tm_GC(Seq(seq), strict=False))
            
print("Range:", max(tm) - min(tm), "Mean:", sum(tm)/len(tm))
    




# In[ ]:




# In[ ]:



