## Goals

- Identify the right annealing temperature for the primers.
  - pCI: what is the right Tm for the primers when amplified using Phusion?
  - PB2: same question, except using MyTaq (proxy for agilent enzyme)

## Setup

We do the following reactions:

1. PB2 Part 1
1. PB2 Part 2
1. pCI Part 1
1. pCI Part 2
1. MyTaq Water-only control
1. MyTaq template-only control
1. Phusion water-only control
1. Phusion template-only control

Note to future self: though the reactions use up a lot of enzyme, it's the surest way to check for contaminations and the like, as I'm ensuring that the reactions I'm interested in are set up exactly the same as the controls.

## PCR Layout

In this case, I'm using a 96-well plate.

| Col: Temp/ºC Row: Sample ID | 62 | N/A | 64 | N/A | 66 | N/A | 68 | N/A | 70 | N/A | 72 | N/A |
|:---------------------------:|:--:|:---:|:--:|:---:|:--:|:---:|:--:|:---:|----|-----|----|-----|
|        A: PB2 Part 1        |    |     |    |     |    |     |    |     |    |     |    |     |
|        B: PB2 Part 2        |    |     |    |     |    |     |    |     |    |     |    |     |
|        C: pCI Part 1        |    |     |    |     |    |     |    |     |    |     |    |     |
|        D: pCI Part 2        |    |     |    |     |    |     |    |     |    |     |    |     |
|     E: MyTaq water-only     |    |     |    |     |    |     |    |     |    |     |    |     |
|    F: MyTaq template-only   |    |     |    |     |    |     |    |     |    |     |    |     |
|    G: Phusion water-only    |    |     |    |     |    |     |    |     |    |     |    |     |
|   H: Phusion template-only  |    |     |    |     |    |     |    |     |    |     |    |     | |

## PCR Setup

I have to make a total of 8 master mixes, one for each row in the sample layout.

| Reagent                      | 1 rxn | MM x6.6 |
|------------------------------|-------|---------|
| 2X MyTaq or Phusion GC       | 10    | 66      |
| Water                        | 7     | 46.2    |
| Fw (or H2O for W &T ctrls)   | 1     | 6.6     |
| Re (or H2O for W &T ctrls)   | 1     | 6.6     |
| Template (or H2O for T ctrl) | 1     | 6.6     |
| Total                        | 20    | 132     |

## Primer Table

| PCR Rxn       | Fw/Re  | expected size |
|---------------|--------|---------------|
| 1: PB2 Part 1 | 30, 29 | 1600          |
| 2: PB2 Part 2 | 28, 27 | 820           |
| 3: pCI Part 1 | 32, 31 | 2707          |
| 4: pCI Part 2 | 26, 25 | 1374          |

Note to self: Fw/Re numbers refer to primers in my catalogue, EM-25 to EM-30.

Note to self: All of the controls - I don't expect a band to be present.

## PCR Program

Temperature (ºC)  |  Time (min, sec)  | Cycles  
------------------|-------------------|--------
95                | 1, 00             | 1
95                | 0, 15             | repeat
60-72             | 0, 15             | 40
72                | 2, 00             | cycles
72                | 10, 00            | 1
4                 | hold              | 1

## Gel

I made a 100 mL 1% gel (w/v) with 10 µL EtBr added. Three gels are needed in total.

- Gel 1 contains rows A-C. Samples are loaded from left to right.
- Gel 2 contains rows D-H. Samples are loaded from left to right.


Gel 1:

- Row 1:
  - Lanes 1-6: PB2 Part 1, 60ºC-72ºC
  - Lanes 7-10: PB2 Part 2, 60ºC-66ºC
- Row 2:
  - Lanes 1-2: PB2 Part 2, 68ºC-72ºC
  - Lanes 3-8: pCI Part 1, 60ºC-72ºC

![gel1](./20160831-gradient-pcr-gel-1.jpg)

Gel 2:
- Row 1:
  - Lanes 1-6: pCI Part 2, 60ºC-72ºC
  - Lanes 7-12: MyTaq water-control, 60ºC-72ºC
  - Lanes 13-18: MyTaq template-only, 60ºC-72ºC
- Row 2:
  - Lanes 1-6: Phusion water-control, 60ºC-72ºC
  - Lanes 7-12: Phusion template-only, 60ºC-72ºC

![gel2](./20160831-gradient-pcr-gel-2.jpg)

Interpretation of both gels: let's take a look at whether there's an optimal temperature for each PCR reaction.

- PB2 Part 1: 68ºC
- PB2 Part 2: <60ºC. For future use, punt it and just use 56ºC.
- pCI Part 1: All work, use 68ºC.
- pCI Part 2: All work, use 68ºC
- Water controls: all empty
- Template-only controls: only large bands
