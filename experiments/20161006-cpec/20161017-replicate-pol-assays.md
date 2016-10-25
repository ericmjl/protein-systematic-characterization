## Goals

- perform two separate replicate experiments of previous [pol assay experiment](../20160805-mutagenesis/20160928-cpec-pol-assay.md)

## Protocol

- Started new culture of 293T cells as per [protocol](../../protocols/cell-culture.md)

### Gel Electrophoresis

- 1% w/v agar 150mL gel
- 10 ul loading dye, 1:10 loading dye
- 30 min @ 150V

**Analysis**
- warped nature of gel is likely due to problems during gel solidification
- pCI fragments are the appropriate sizes, so they will be extracted. For pCI part 1, there is some ambiguity in the bands - I extracted the bottom half of the mush.
- Very faint PB2 part 2 band, indiscernible part 1 band - will re-run both with 0.25mM instead, since previous gel showed that 0.50mM yields very few PCR products.

### Re-run PCR for PB2

| Reagent        | 1 rxn | 2.2x MM |
|----------------|-------|---------|
| Water          | 17    | 37.4    |
| 2x MyTaq       | 25    | 55      |
| MnCl2 (2.5mM)  | 5     | 11      |
| Template       | 1     | N/A     |
| Forward Primer | 1     | N/A     |
| Reverse Primer | 1     | N/A     |
| Total          | 50    | 103.4   |

### Gel Extraction

pCI part 1: 62mg
pCI part 2: 83mg
PB2 part 1: 170mg
PB2 part 2: 100mg

**Purified DNA**

| Fragment | [DNA] ng/ul | 260/280 |
|----------|-------------|---------|
| pCI pt1  | 94.4        | 2.02    |
| pCI pt2  | 277.5       | 1.93    |
| PB2 pt1  | 16.9        | 2.95    |
| PB2 pt2  | 6.4         | -49.58*    |

Despite discouraging results, we decided to proceed with CPEC anyway*

### CPEC Assembly

Followed same procedure as before.

CPEC product DNA concentration: 35.5 ng/ul with 260:280 of 2.12. This makes sense, since the limiting concentration was 6.4 and the corresponding fragment is about 1/5 of the plasmid.



### Replication 1

- seeded Passage 0 cells into 12-well plate at 75 ul cells in 1ml medium per well.
- After a day, cells appeared 100% confluent, but I decided to proceed with transfection anyway on 10/22/16. The cells were incubated for about 4.5 hours before changing medium instead of the 4 hours recommended by the protocol.
- I made a few errors in following the protocol, most grievous of which was forgetting to add the rest of the components of the polymerase till after already adding the lipofectamine to the PB2 plasmid mixture

Seeded wells:
[cell pic](./20161022-rep1-well.JPG)

- Medium is very much yellow as I store samples of the cells.

### Replication 2

- Split Passage 0 cells into plates with concentrations of 1:10, 1:20, and 1:40

Day 1 (1:10)
[cell pic 2](./20161022-293T-10x.JPG)

Day 2 (1:10)
[cell pic 3](./20161023-293T-10x.JPG)
Mostly looked healthy, except for this clump:
[cell pic 4](./20161023-293T-10x-clump.JPG)

- By Day 3, 1:10 was about 80% confluent, but I discarded it since the clump was indication of fungal contamination. Either 1:20 or 1:40 should be ready for seeding and splitting tomorrow.
