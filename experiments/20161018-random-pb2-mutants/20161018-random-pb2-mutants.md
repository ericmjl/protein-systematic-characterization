## Background/Context

1. While we were able to get a small library of random mutants in the latter 800 bp of PB2 using the Agilent enzyme, we weren't able to get the Agilent enzyme to amplify the first 1600 bp of PB2.
1. "HackyTaq" looks like it might work, but we're still not sure.
1. Thought: maybe just "wing it" with manganese? Who knows, we may still get random mutants anyways?

## Goals

1. [x] Use 0.25 mM Mn<sup>2+</sup> to create random mutants of PB2 (both parts).
1. [x] Amplify the pol assay plasmid backbone off the VicPB2 plasmid.
1. [x] CPEC assemble the PB2 and plasmid backbone.
1. [X] Transform into E. coli cells, grow overnight, miniprep, and send for sequencing.

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

## Re-run PCR for PB2

| Reagent        | 1 rxn | 2.2x MM |
|----------------|-------|---------|
| Water          | 17    | 37.4    |
| 2x MyTaq       | 25    | 55      |
| MnCl2 (2.5mM)  | 5     | 11      |
| Template       | 1     | N/A     |
| Forward Primer | 1     | N/A     |
| Reverse Primer | 1     | N/A     |
| Total          | 50    | 103.4   |

## Re-run Gel

[gel2](./20161019-gel-pb2-rerun.JPG)

| Ladder | PB2 part 1 | PB2 part 2 | Ladder|

Appropriate bands present.

## Gel Extraction

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

## CPEC Assembly

Followed same procedure as before.

Purified cpec product: 35.5ng/ul, 2.12 (260/280)

## Transformation

Followed [transformation protocol](../../protocols/transformation.md).

Plates:

| CPEC 1ul | CPEC 10ul | CPEC "rest" |
| Control 1ul| Control 10ul | Control "rest"| (Vic template)

Result: No colonies on any of the plates.

Repeated transformation on 25 October 2016. Same protocol, except added pUC 19. Here is the full list of plasmids that I will transform:

- pUC19 (provided with kit, control), 1 µL = 100 pg
- VicPB2 (control), 1 µL = 416 ng
- CPEC assembly from above 5 µL = 177.5 ng

Minor protocol change: the SOC media had not fully thawed when I finished the 2 min. incubation on ice. Therefore, microwaved the SOC media for 15 seconds, resulting in SOC that was a bit too warm. I then pipetted out 950 µL into individual microfuge tubes and let them chill on ice before adding them to the cell/. In total, I let the final ice incubation step go for longer than 2 min (~4 min total).

On 26 October 2016, checking on the plates, here's the number of colonies counted.

| Sample | DNA (ng) | 1 µL | 10 µL | Rest (89 µL) | Colonies per (µg DNA) |
|--------|----------|------|-------|--------------|-----------------------|
| CPEC   | 177.5    | 0    | 0     | 5            | 3.80E+01              |
| pUC19  | 0.1      | 16   | TNTC  | TNTC         | 1.60E+07              |
| VicPB2 | 416      | 3    | TNTC  | TNTC         | 7.21E+02              |

Note: "TNTC" stands for "too numerous to count". Comes from a microbiology tradition.

It looks like there's empirically no point in only transforming 5 µL of CPEC product. Best to elute in as small of a volume as possible (10 µL), transform the whole thing, and plate "10 µL" and "Rest".

I repeated the CPEC transformation one final time. Here is the list of plasmids being transformed.

- VicPB2 (control), 5 µL = 2.265 µg
- CPEC, 15 µL = 532.5 ng

Plated 10 µL and 90 µL ("the rest") of transformation mix.

The next day, here's the number of colonies counted.

| Sample | DNA (ng) | 10 µL | 90 µL | Colonies per µg DNA |
|--------|----------|-------|-------|---------------------|
| VicPB2 | 2265     | 55    | TNTC  | 243                 |
| CPEC   | 532.5    | 0     | 5     | 10                  |

Same order of magnitude as the previous run.

Vivian picked all 10 colonies and grew them as an overnight culture in 1 mL LB-Amp.

About 20 hours later, Vivian miniprepped the bacteria culture. DNA concentration was measured by Eric.

| #  | Sample ID | User name        | Date and Time         | Nucleic Acid Conc. | Unit  | A260  | A280  | 260/280 | 260/230 | Sample Type | Factor |
|----|-----------|------------------|-----------------------|--------------------|-------|-------|-------|---------|---------|-------------|--------|
| 1  | L17       | Eric Jinglong Ma | 10/28/2016 1:28:46 PM | 221.0              | ng/µl | 4.420 | 2.312 | 1.91    | 2.29    | DNA         | 50.00  |
| 2  | L18       | Eric Jinglong Ma | 10/28/2016 1:29:05 PM | 167.3              | ng/µl | 3.347 | 1.769 | 1.89    | 1.90    | DNA         | 50.00  |
| 3  | L19       | Eric Jinglong Ma | 10/28/2016 1:29:29 PM | 180.5              | ng/µl | 3.610 | 1.875 | 1.93    | 2.44    | DNA         | 50.00  |
| 4  | L20       | Eric Jinglong Ma | 10/28/2016 1:29:52 PM | 201.6              | ng/µl | 4.033 | 2.095 | 1.93    | 2.42    | DNA         | 50.00  |
| 5  | L21       | Eric Jinglong Ma | 10/28/2016 1:30:13 PM | 93.6               | ng/µl | 1.871 | 0.952 | 1.97    | 2.58    | DNA         | 50.00  |
| 6  | L22       | Eric Jinglong Ma | 10/28/2016 1:30:33 PM | 128.8              | ng/µl | 2.575 | 1.319 | 1.95    | 2.28    | DNA         | 50.00  |
| 7  | L23       | Eric Jinglong Ma | 10/28/2016 1:30:52 PM | 110.1              | ng/µl | 2.201 | 1.120 | 1.96    | 2.55    | DNA         | 50.00  |
| 8  | L24       | Eric Jinglong Ma | 10/28/2016 1:31:11 PM | 96.1               | ng/µl | 1.922 | 0.974 | 1.97    | 2.60    | DNA         | 50.00  |
| 9  | L25       | Eric Jinglong Ma | 10/28/2016 1:31:29 PM | 47.4               | ng/µl | 0.948 | 0.442 | 2.14    | 2.79    | DNA         | 50.00  |
| 10 | L26       | Eric Jinglong Ma | 10/28/2016 1:31:51 PM | 113.0              | ng/µl | 2.259 | 1.149 | 1.97    | 2.53    | DNA         | 50.00  |

## Transfection

2016-10-31: Seeded 1:40 dilution (25ul cells in 1mL DMEM) of passage-3 293T cells in a 12-well plate. The 8 mutant strains with the highest DNA concentration will be assayed.
- Cell count upon seeding: (74.5)(40)(10<sup>4</sup>)(25/1000) = 7.4 million cells per well

2016-11-02: Transfected cells with mutant plasmids.

|   | 1    | 2    | 3   | 4   |
|---|------|------|-----|-----|
| A | Mock | PHH  | PCD | Vic |
| B | L17   | L18   | L19  | L20  |
| C | L22   | L23  | L24 | L26 |

Volume of PB2 plasmid added: int(500ng/[DNA])

2016-11-04: Stored supernatant in -4C. Medium was very yellow, and big clumps of cells seem to have peeled off the well bottom to float in the supernatant. They were avoided were pipetting out the sup.
