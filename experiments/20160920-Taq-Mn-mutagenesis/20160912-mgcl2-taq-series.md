## Goals
- identify the effect of Mn<sup>2+</sup> concentration on mutation frequency during Taq-based PCR
- "hack" a way of inducing random mutation in PB2 Part 1, which has heretofore been unsuccessful

## Setup

**MnCl<sub>2</sub> Dilutions**

| Concentration (mM) | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0   | 3.5  | 4.0 | 4.5  | 5.0 | 5.5  | 6.0 |
|--------------------|-----|-----|-----|-----|-----|-------|------|-----|------|-----|------|------|
| H2O (ul)*          | 950 | 450 | 283.3 | 200 | 150 | 116.7 | 92.9 | 75  | 61.1 | 50  | 40.9 | 33.3 |

*Added to 50 ul 10mM MgCl<sub>2</sub>

**PCR Reactions**

For every concentration:
 - PB2 part 1: EM-30, 29
 - PB2 part 2: EM-28, 27
 - Template-only: substitute primers with water

**PCR Mix**

For each set of reactions:

| PCR Mix    | 1 rxn | Master Mix (13.2x) |
|------------|-------|-------------------|
| Water      | 17    |    224          |
| 2x MyTaq Red | 25    | 330            |
| MnCl2       | 5 |              N/A     |
| Template   | 1     | 13.2               |
| F Primer   | 1     | 13.2               |
| R Primer   | 1     | 13.2               |

**PCR Reactions**

For every concentration:
 - (1) PB2 part 1: EM-30, 29
 - (2) PB2 part 2: EM-28, 27
 - (T) Template-only

Labelled with 1, 2, or T and [MnCl2]

**PCR Program**

Used mytaq red program in PCR machine.

## Analysis

**DNA Concentration**

Pre-purification:

| MnCl2 Concentration (mM) | PB2 Part 1                          | PB2 Part 2   | Template     |
|--------------------------|-------------------------------------|--------------|--------------|
| 0.05                     | 17439 (43.6)                        | 17148 (41.1) | 17132 (41.7) |
| 0.55                     | 17552 (39.3)                        | 17233 (39.4) | 17255 (39.1) |

Post-purification (PB2 part 2 only):

| [MnCl2] (mM) | [DNA] (ng/ul) | 260/280 |
|--------------|---------------|---------|
| 0            | 31.1          | 2.55    |
| .25          | 25.6          | 2.95    |
| .55          | 20.6          | 2.88    |

Sent in samples for Sanger sequencing (Genewiz). (by EM)

| Tube  | Sample   | Primer | DNA (µL) | Primer (µL) |
|-------|----------|--------|----------|-------------|
| IH-01 | 0 mM Mn  | EM-28  | 10       | 5           |
| IH-02 | 0 mM Mn  | EM-27  | 10       | 5           |
| IH-03 | 25 mM Mn | EM-28  | 10       | 5           |
| IH-04 | 25 mM Mn | EM-27  | 10       | 5           |
| IH-05 | 55 mM Mn | EM-28  | 10       | 5           |
| IH-06 | 55 mM Mn | EM-27  | 10       | 5           |

[Sequencing order](./20160920-sequencing-order.pdf)
