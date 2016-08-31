## Goals

- Generate mutant PB2 PCR products as well as generate pcI backbone PCR products

## Setup

### Reactions:

1. PB2 w/ Agilent (4 rxns)
2. pCI w/ Phusion (4 rxns)

1. **PB2**

| PCR Mix    | 1 rxn | Master Mix (4.4x) |
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

2. **pCI**

| PCR Mix    | 1 rxn | Master Mix (4.4x) |
|------------|-------|-------------------|
| Water      | 22    | 96.8              |
| 2x Phusion | 25    | 110               |
| Template   | 1     | N/A               |
| F Primer   | 1     | N/A               |
| R Primer   | 1     | N/A               |

| Reaction      | Primers      | PCR Tube Label |
|---------------|--------------|----------------|
| pCI Part 1    | EM-32, EM-31 | P1             |
| pCI Part 2    | EM-26, EM-25 | P2             |
| Water-only    | N/A          | PW             |
| Template-only | N/A          | PT             |

- Note on prep: Phusion is much more resilient than Agilent and does not need to be put on ice

### Programs:

**Agilent**

| Temperature (C)      | Time           | # cycles |
|----------------------|----------------|----------|
| 95                   | 2 min          | 1        |
| 95  | 30 s | Repeat       |
| P1: 68, P2: 56| 30s | 30       |
| 72 | 2 min | times       |
| 72                   | 10 min         | 1        |
| 4                    | hold           |          |

**Phusion**

| Temperature (C) | Time            | # cycles |
|-----------------|-----------------|----------|
| 95              | 30 s            | 1        |
| 95         | 15 s  | Repeat       |
| 68        | 15 s | 30       |
| 72        | 2 min | times       |
| 72              | 7 min           | 1        |
| 4               | hold            |          |