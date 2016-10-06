## Goals

Following up on Vivian's set of excellently-conducted prior experiments (date: [2016-09-20](../20160920-Taq-Mn-mutagenesis/20160912-mgcl2-taq-series.md)), I wanted to fill in the blanks w.r.t. the concentrations not yet tested and sequenced.

As such, the goals are below:

1. Produce replicate PCRs for a range of Mn<sup>2+</sup> concentrations.
1. Sequence them to count the number of mutations present.

## PCR Setup

### PCR

- Primers:
    - Fw: EM-28
    - Re: EM-27
- Template: VicPB2

### Reaction conditions

| [Mn] (mM) | Replicates | 96-well plate row |
|:---------:|:----------:|:-----------------:|
|    0.00   |      3     |         A         |
|    0.10   |      3     |         B         |
|    0.20   |      3     |         C         |
|    0.25   |      3     |         D         |
|    0.30   |      3     |         E         |
|    0.35   |      3     |         F         |
|    0.40   |      3     |         G         |
|    0.50   |      3     |         H         |

Total estimated cost @ $6/sequencing reaction: $144.

### PCR Master Mix

| Ingredient   | 1 Rxn Vol (µL) | MM x26.4 |
|--------------|:--------------:|:--------:|
| Water        |       17       |   448.8  |
| 2X MyTaq Red |       25       |    660   |
| 10X MnCl2    |        5       |    N/A   |
| Template     |        1       |   26.4   |
| Fw Primer    |        1       |   26.4   |
| Re Primer    |        1       |   26.4   |

### PCR Program

MyTaq Red

- 68ºC annealing
- 2 min extension @ 72ºC
- 40 cycles in total

## PCR Purification

Didn't bother with gel checking, as we know from prior experience that this PCR reaction works reliably.
