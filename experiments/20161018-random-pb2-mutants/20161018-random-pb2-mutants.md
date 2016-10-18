## Background/Context

1. While we were able to get a small library of random mutants in the latter 800 bp of PB2 using the Agilent enzyme, we weren't able to get the Agilent enzyme to amplify the first 1600 bp of PB2.
1. "HackyTaq" looks like it might work, but we're still not sure.
1. Thought: maybe just "wing it" with manganese? Who knows, we may still get random mutants anyways?

## Goals

1. [ ] Use 0.5 mM Mn<sup>2+</sup> to create random mutants of PB2 (both parts).
1. [ ] Amplify the pol assay plasmid backbone off the VicPB2 plasmid.
1. [ ] CPEC assemble the PB2 and plasmid backbone.
1. [ ] Transform into E. coli cells, grow overnight, miniprep, and send for sequencing.

In a separate branch, I will outline the design of new sequencing primers for sequencing portions of the polymerases.

## PCR setup

For amplifying the PB2 protein:

| Reagent      | 1 Reaction (µL) |
|--------------|-----------------|
| 2x MyTaq Red | 25              |
| Water        | 17              |
| 5 mM Mn2+    | 5               |
| Fw primer    | 1               |
| Re primer    | 1               |
| Template     | 1               |
| Total        | 50              |

For amplifying the backbone:

| Reagent   | 1 Reaction (µL) |
|-----------|-----------------|
| 2X KAPA   | 25              |
| Water     | 22              |
| Fw primer | 1               |
| Re primer | 1               |
| Template  | 1               |
| Total     | 50              |

Reactions & primers:

| Tube | Reactions  | Fw    | Re    | Tm (ºC) |
|------|------------|-------|-------|---------|
| 1    | PB2 Part 1 | EM-30 | EM-29 | 68      |
| 2    | PB2 Part 2 | EM-28 | EM-27 | 58      |
| 3    | pCI Part 1 | EM-32 | EM-31 | 68      |
| 4    | pCI Part 2 | EM-26 | EM-25 | 68      |

PCR Program

| Temperature (ºC) | Time (min, sec) | Cycles |
|------------------|-----------------|--------|
| 95               | 1, 00           | 1      |
| 95               | 0, 15           | 40     |
| Tm               | 0, 15           | 40     |
| 72               | 2, 00           | 40     |
| 72               | 10, 00          | 1      |
| 4                | hold            | n/a    |
