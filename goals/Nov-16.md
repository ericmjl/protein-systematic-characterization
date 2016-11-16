## Goals for Nov 17 - Nov 22

### Experiments
- Run another high-throughput experiment, with a clearer, modified protocol.
  - Specifically, the serial dilution to measure polymerase expression as a function of number of cells should be repeated with better mixing
- Sequence fully mutated PB2 plasmids
  - Design 20-mer primers that end 100bp upstream of end of pCI sequence and 100bp downstream of start of pCI
- PacBio
  - determine a position in the sequence to insert barcode that will not affect polymerase activity in cells
  - start by inserting a sequence of 8 N bases; assay plasmids with barcode inserted right after and right before the PB2 sequence against barcode-less plasmid

### Data Analysis
- Setup a procedure for efficiently organizing luminescence data
  - Use pandas library to normalize luminescence values such that they are all greater than 0
  - Combine data from separate assays into one master file
- Figure out what normalization standard to use
