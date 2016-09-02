## Goals

- Generate mutant PB2 PCR products as well as generate pcI backbone PCR products
- Resolve problems from previous mutagenesis - changes are bolded

## Setup

### Reactions:

1. PB2 w/ Agilent (4 rxns)
2. pCI w/ Phusion (3 rxns)

**PB2**

| PCR Mix    | 1 rxn | Master Mix (4.4x) |
|------------|-------|-------------------|
| Water      | 41.5  | 182.6             |
| 10x buffer | 5     | 22                |
| 40 mM dNTP | 1     | 4.4               |
| F Primer   | 1     | N/A               |
| R Primer   | 1     | N/A               |
| Polymerase | 1     | **N/A***               |
| Template   | 1     | N/A               |
| Total      | 51.5  | 213.4             |

| Reaction      | Primers      | PCR Tube Label |
|---------------|--------------|----------------|
| PB2 Part 1    | EM-30, EM-29 | A1             |
| PB2 Part 2    | EM-28, EM-27 | A2             |
| Water-only    | N/A          | AW             |
| Template-only | N/A          | AT             |

*Added polymerase to each reaction separately after primers

**pCI**

| PCR Mix    | 1 rxn | Master Mix (3.3x) |
|------------|-------|-------------------|
| Water      | 22    | 72.6              |
| 2x Phusion** | 25    | 82.5               |
| Template   | 1     | N/A               |
| F Primer   | 1     | N/A               |
| R Primer   | 1     | N/A               |

| Reaction      | Primers      | PCR Tube Label |
|---------------|--------------|----------------|
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
| **A1: 62, A2: 50**       | 30s            | 30       |
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
