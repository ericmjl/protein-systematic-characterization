
## Prior Work

- Previous rounds of mutagenesis using the agilent enzyme yielded very little product.
  - [Round 1](./20160831-mutagenesis.md) - no bands
  - [Round 2](./20160902-mutagenesis-2.md) - reduced annealing temperature by 6ºC, faint bands showed up, but also non-specific annealing showed up.

## Goals

- Test to see if 2% DMSO works to increase specificity of PCR reaction, and hence amount of reaction product.
  - Concurrently increase the number of reaction cycles to 40.

## PCR Setup

| Reaction        | Fw/Re        | Annealing Temp |
|-----------------|--------------|----------------|
| PB2 Part 1 (A1) | EM-30, EM-29 | 62ºC           |
| PB2 Part 2 (A2) | EM-28, EM-27 | 50ºC           |
| Water-only      | N/A          | 50ºC           |
| Template-only   | N/A          | 50ºC           |

## Reaction Master Mix

| Reagent      | 1 Rxn (µL) | MM x4.4 (µL) |
|--------------|------------|--------------|
| Water        | 39         | 171.6        |
| 10X Buffer   | 5          | 22           |
| 40 mM dNTP   | 1          | 4.4          |
| Fw primer    | 1          | N/A          |
| Re primer    | 1          | N/A          |
| Polymerase   | 1          | 4.4          |
| 100% DMSO    | 1          | 4.4          |
| Template     | 1          | N/A          |
| **Total Volume** | **50** | **206.6**    |

## PCR Program

| Temperature (C)      | Time           | # cycles |
|----------------------|----------------|----------|
| 95                   | 2 min          | 1        |
| 95                   | 30 s           | Repeat   |
| Variable (see PCR setup)| 30 s        | 40       |
| 72                   | 2 min          | times    |
| 72                   | 10 min         | 1        |
| 4                    | hold           | 1        |

## Gel

1% agarose gel (w/v), 150V, 30 min
