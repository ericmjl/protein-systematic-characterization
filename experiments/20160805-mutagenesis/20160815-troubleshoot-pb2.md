## Goals

- Troubleshoot PCR.

Hypothesis: the primers do not work.

How will we know? If we run the PCR reaction with regular MyTaq Red, then if the primers work, we will get the expected 1.6 and 0.8 kb bands. If they don't work, then I will re-order new primers for amplification.

Note to self: in the future, must test the primers before going running them with expensive mutagenesis primers!

## Key Protocol Steps

### PCR

**Samples:**
- Template: Victoria PB2
  - Part 1:
    - Fw primer: EM-11, 64ºC
    - Re primer: EM-10, 62ºC
    - 1586 bp product size
  - Part 2:
    - Fw primer: EM-3, 63ºC
    - Re primer: EM-2, 62ºC
    - 806 bp product size
- PCR tube samples:
  - P1: Part 1
  - P2: Part 2
  - W: Water-only control
  - T: Template-only control

**Master Mix:**

Reaction volume: 50 µL

Reagent       | 1 rxn (µL)     | MM x4.4 (µL)
--------------|----------------|-------------
MyTaq Red Mix | 25             | 110
Water         | 22             | 96.8
Fw Primer     | 1              | N/A
Re Primer     | 1              | N/A
Template      | 1              | N/A
**Total:**    | **50**         | **206.8**

Note how the primer pairs are matched up:

Sample   | Fw   | Re   | Template
---------|------|------|----------
P1       | EM11 | EM10 | VicPB2
P2       | EM3  | EM2  | VicPB2
W        | H2O  | H2O  | H2O
T        | H2O  | H2O  | VicPB2

**PCR Protocol:**

Temperature (ºC)  |  Time (min, sec)  | Cycles  
------------------|-------------------|--------
95                | 1, 00             | 1
95                | 0, 15             | repeat
57                | 0, 15             | 35
72                | 1, 00             | cycles
72                | 10, 00            | 1
4                 | hold              | 1

Note: MyTaq Red uses 30s/kb. The longest PCR product is 1.6 kb, so we go for 1 min.

Let the PCR reaction go overnight.
