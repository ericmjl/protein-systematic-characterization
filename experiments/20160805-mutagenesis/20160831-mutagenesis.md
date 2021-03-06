## Goals

- Generate mutant PB2 PCR products as well as generate pcI backbone PCR products

## Setup

### Reactions:

1. PB2 w/ Agilent (4 rxns)
2. pCI w/ Phusion (4 rxns)

**PB2**

| PCR Mix    | 1 rxn | Master Mix (4.4x*) |
|------------|-------|-------------------|
| Water      | 41.5  | 182.6             |
| 10x buffer | 5     | 22                |
| 40 mM dNTP | 1     | 4.4               |
| F Primer   | 1     | N/A               |
| R Primer   | 1     | N/A               |
| Polymerase | 1     | 4.4               |
| Template   | 1     | N/A               |
| Total      | 51.5  | 213.4             |

| Reaction      | Primers      | PCR Tube Label |
|---------------|--------------|----------------|
| PB2 Part 1    | EM-30, EM-29 | A1             |
| PB2 Part 2    | EM-28, EM-27 | A2             |
| Water-only    | N/A          | AW             |
| Template-only | N/A          | AT             |

- 10% chance of error per reaction

**pCI**

| PCR Mix    | 1 rxn | Master Mix (4.4x) |
|------------|-------|-------------------|
| Water      | 22    | 96.8              |
| 2x Phusion** | 25    | 110               |
| Template   | 1     | N/A               |
| F Primer   | 1     | N/A               |
| R Primer   | 1     | N/A               |

| Reaction      | Primers      | PCR Tube Label |
|---------------|--------------|----------------|
| pCI Part 1    | EM-32, EM-31 | P1             |
| pCI Part 2    | EM-26, EM-25 | P2             |
| Water-only    | N/A          | PW             |
| Template-only | N/A          | PT             |

**Contains buffer, dNTPs, and DNA polymerase

**Note on prep**
- Phusion is much more resilient than Agilent and does not need to be put on ice
- Avoid touching inside of tube caps


### PCR Programs

**Agilent**

| Temperature (C)      | Time           | # cycles |
|----------------------|----------------|----------|
| 95                   | 2 min          | 1        |
| 95                   | 30 s           | Repeat   |
| A1: 68, A2: 56       | 30s            | 30       |
| 72                   | 2 min          | times    |
| 72                   | 10 min         | 1        |
| 4                    | hold           |          |

**Phusion**

| Temperature (C) | Time            | # cycles |
|-----------------|-----------------|----------|
| 95              | 30 s            | 1        |
| 95              | 15 s            | Repeat   |
| 68              | 15 s            | 30       |
| 72              | 2 min           | times    |
| 72              | 7 min           | 1        |
| 4               | hold            |          |

### Gel Electrophoresis

Gel Parameters
- 1% (w/v)
- 150 volts, 20 min

Gel Order

| Ladder | P1 | P2 | PW | PT | A1 | A2 | AW | AT | Ladder |
|--------|----|----|----|----|----|----|----|----|--------|

![mutagenesis_gel](./20160901-mutagenesis-pcr-gel.JPG)

## Analysis

- Only PCR with P1 (band at 2.7kb) appears successful.
- Since pCI part 2 worked previously under same conditions, reaction will be repeated.
- PB2 part 2 is present but faint; PB2 part 1 failed. Will lower annealing temperature of both by 5C to 50C and 63C respectively.

**Expected Sizes**

| Fragment        | expected size |
|-----------------|---------------|
| A1: PB2 Part 1  | 1600          |
| A2: PB2 Part 2  | 820           |
| P1: pCI Part 1  | 2707          |
| P2: pCI Part 2  | 1374          |

## Post-Processing

Because pCI Part 1 was produced successfully, we cut out the band from the gel, and used the Qiaquick Gel Extraction kit to extract the DNA from there.

Notes/deviations from protocol:

- Mass of gel: 1.177 g - 0.998 g = 0.189 g
- Buffer QG vol.: 3 x 189 = 567 µL
- Isopropanol vol.: 189 µL
- Final elution vol: 10 µL

Sample stored in cloning kit, -20ºC.
