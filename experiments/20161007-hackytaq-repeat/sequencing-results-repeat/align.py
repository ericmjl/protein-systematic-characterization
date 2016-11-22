from Bio import SeqIO
from Bio.Align.Applications import ClustalOmegaCommandline
import os

sequences = []

for f in os.listdir(os.getcwd()):
    if f[-4:] == '.seq':
        print(f)
        s = SeqIO.read(f, 'fasta')
        sequences.append(s)

vic = SeqIO.read('victoria-pb2.fasta', 'fasta')
vic.seq = vic.seq[-800:]

sequences.append(vic)

print('Sequences:')
print(sequences)

# Write all sequences to disk.
SeqIO.write(sequences, 'all-sequences.fasta', 'fasta')

# Align

cline = ClustalOmegaCommandline(infile='all-sequences.fasta',
                                outfile='all-sequences.aligned.fasta',
                                verbose=True, auto=True, force=True)
cline()
