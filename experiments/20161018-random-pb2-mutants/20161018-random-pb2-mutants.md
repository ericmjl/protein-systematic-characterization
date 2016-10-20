## Background/Context

1. While we were able to get a small library of random mutants in the latter 800 bp of PB2 using the Agilent enzyme, we weren't able to get the Agilent enzyme to amplify the first 1600 bp of PB2.
1. "HackyTaq" looks like it might work, but we're still not sure.
1. Thought: maybe just "wing it" with manganese? Who knows, we may still get random mutants anyways?

## Goals

1. [ ] Use 0.5 mM Mn<sup>2+</sup> to create random mutants of PB2 (both parts).
1. [ ] Amplify the pol assay plasmid backbone off the VicPB2 plasmid.
1. [ ] CPEC assemble the PB2 and plasmid backbone.
1. [ ] Transform into E. coli cells, grow overnight, miniprep, and send for sequencing.

In a separate branch, I will outline the design of new sequencing primers for sequencing portions of the polymerases.

## PCR setup

For amplifying the PB2 protein:

| Reagent      | 1 Reaction (µL) |
|--------------|-----------------|
| 2x MyTaq Red | 25              |
| Water        | 17              |
| 5 mM Mn2+    | 5               |
| Fw primer    | 1               |
| Re primer    | 1               |
| Template     | 1               |
| Total        | 50              |

For amplifying the backbone:

| Reagent   | 1 Reaction (µL) |
|-----------|-----------------|
| 2X KAPA   | 25              |
| Water     | 22              |
| Fw primer | 1               |
| Re primer | 1               |
| Template  | 1               |
| Total     | 50              |

Reactions & primers:

| Tube | Reactions  | Fw    | Re    | Tm (ºC) |
|------|------------|-------|-------|---------|
| 1    | PB2 Part 1 | EM-30 | EM-29 | 68      |
| 2    | PB2 Part 2 | EM-28 | EM-27 | 58      |
| 3    | pCI Part 1 | EM-32 | EM-31 | 68      |
| 4    | pCI Part 2 | EM-26 | EM-25 | 68      |

PCR Program

| Temperature (ºC) | Time (min, sec) | Cycles |
|------------------|-----------------|--------|
| 95               | 1, 00           | 1      |
| 95               | 0, 15           | 40     |
| Tm               | 0, 15           | 40     |
| 72               | 2, 00           | 40     |
| 72               | 10, 00          | 1      |
| 4                | hold            | n/a    |

### Gel Electrophoresis

[gel](./20161018-gel-random-pb2-mutatns.JPG)

| Ladder | PB2 part 1 | PB2 part 2 | pCI part 1 | pCI part 2| Ladder|

- 1% w/v agar 150mL gel
- 10 ul loading dye, 1:10 loading dye
- 30 min @ 150V

**Analysis**
- warped nature of gel is likely due to problems during gel solidification
- pCI fragments are the appropriate sizes, so they will be extracted. For pCI part 1, there is some ambiguity in the bands - I extracted the bottom half of the mush.
- Very faint PB2 part 2 band, indiscernible part 1 band - will re-run both with 0.25mM instead, since previous gel showed that 0.50mM yields very few PCR products.

### Re-run PCR for PB2

| Reagent        | 1 rxn | 2.2x MM |
|----------------|-------|---------|
| Water          | 17    | 37.4    |
| 2x MyTaq       | 25    | 55      |
| MnCl2 (2.5mM)  | 5     | 11      |
| Template       | 1     | N/A     |
| Forward Primer | 1     | N/A     |
| Reverse Primer | 1     | N/A     |
| Total          | 50    | 103.4   |

### Re-run Gel

[gel2](./20161019-gel-pb2-rerun.JPG)

| Ladder | PB2 part 1 | PB2 part 2 | Ladder|

Appropriate bands present.

### Gel Extraction

pCI part 1: 62mg
pCI part 2: 83mg
PB2 part 1: 170mg
PB2 part 2: 100mg

**Purified DNA**

| Fragment | [DNA] ng/ul | 260/280 |
|----------|-------------|---------|
| pCI pt1  | 94.4        | 2.02    |
| pCI pt2  | 277.5       | 1.93    |
| PB2 pt1  | 16.9        | 2.95    |
| PB2 pt2  | 6.4         | -49.58*    |

Despite discouraging results, we decided to proceed with CPEC anyway*

### CPEC Assembly

Followed same procedure as before.

Purified cpec product: 35.5ng/ul, 2.12 (260/280)

### Transformation

Followed transformation protocol.

Plates:

| CPEC 1ul | CPEC 10ul | CPEC "rest" |
| Control 1ul| Control 10ul | Control "rest"| (Vic template)
