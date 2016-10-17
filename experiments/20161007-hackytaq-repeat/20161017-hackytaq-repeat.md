## Goals

Following the [previous results](./20161012-hackytaq-final-repeat.md), I have decided not to make that run the "final" run, but to repeat one more time to see what the number of mutations are.

As such, the goals here are:

1. Test the effect of varying concentrations of Mn<sup>2+</sup> on the replication fidelity of MyTaq Red.

## PCR reactions

I will test the following concentrations of Mn<sup>2+</sup>:

1. 0 mM
1. 0.1 mM
1. 0.2 mM
1. 0.3 mM
1. 0.4 mM
1. 0.5 mM

A total of six reactions.

PCR Setup:

| Reagent           | 1 rxn (µL) | MM x6.6 (µL) |
|-------------------|------------|--------------|
| MyTaq Red         | 25         | 165          |
| Water             | 17         | 112.2        |
| Mn2+              | 5          | N/A          |
| Fw (EM-28)        | 1          | 6.6          |
| Re (EM-27)        | 1          | 6.6          |
| Template (VicPB2) | 1          | 6.6          |
| Total             | 50         | 297          |

Added 5 µL of 10X final concentration of MnCl<sub>2</sub>, i.e. for 0.5 mM, added 5 µL of 5 mM in 50 µL total reaction volume.

PCR Program:

| Temperature | Time (min, sec) | Cycles |
|-------------|-----------------|--------|
| 95          | 1, 00           | 1      |
| 95          | 0, 15           | 40     |
| 58          | 0, 15           | 40     |
| 72          | 2, 00           | 40     |
| 72          | 10, 00          | 1      |
| 4           | inf             | n/a    |

Let it run overnight.
