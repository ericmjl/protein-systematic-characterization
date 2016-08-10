# Goals

1. Generate mutant Victoria PB2 using random mutagenesis.

# Experiment Design

1. Amplify pCI using primers EM-15 and EM-6, use Phusion GC master mix.
1. Amplify Victoria PB2 using primers EM-2 and EM-11, use GeneMorph II enzyme.

# Key Protocol Steps

## PCR Preparation and Protocol

### pCI backbone PCR for Gibson Assembly

#### Preparation

Two reactions - one sample (named "pCI") and one negative control (named "NC").

Reagent | Volume (µL) | Master Mix Volume x2.2 (µL)
--------|-------------|----------------------------
(fw primer 10 mM) EM-15   | 1.0         | 2.2
(re primer 10 mM) EM-6    | 1.0         | 2.2
(template) VicPB2 in pCI| 1.0    | N/A
Phusion master mix| 10.0 | 22.0
Water   | 7.0         | 15.4
**Total:** | **20.0** | **41.8**

#### PCR Protocol

Temperature (ºC) | Time (min, sec) | cycles
------|-------|-----
98 | 0, 30 | 1
98 | 0, 5  | repeat
67 | 0, 30 | 35
72 | 2, 00 | cycles
72 | 5, 00 | 1
4  | hold  | n/a


### VicPB2 mutagenesis PCR

#### Preparation

Total of two reactions - one for sample (named "VicPB2") and one negative control (named "mut NC" to distinguish from pCI's negative control).

First off, mix 2 µL each of 10 mM EM-2 and EM-11 to create the "primer mix".

Reagent | Volume (µL) | Master Mix Volume (x2.2) (µL)
--------|-------------|----------
Reaction Buffer | 5.0 | 11.0
dNTP | 1.0 | 2.2
GeneMorph II enzyme | 1.0 | 2.2
VicPB2 in pCI | 1.0 | N/A
Primer mix | 0.5 | 1.1
Water | 41.5 | 91.3
**Total:** | **50.0** | **107.8**

#### PCR Protocol

Temperature (ºC) | Time (min, sec) | cycles
------|-------|-----
95 | 2, 00 | 1
95 | 0, 30 | repeat
58 | 0, 30 | 4
72 | 2, 30 | cycles
72 | 10, 00 | 1
4  | hold   | n/a

# Results
