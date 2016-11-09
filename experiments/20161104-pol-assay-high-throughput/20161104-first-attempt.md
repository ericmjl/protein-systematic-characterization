## Goals
- Plan out the adaption of pol assay protocol to 96-well plate

### New Equipment
- a multi-channel aspirator is in the works, but for now I will use a multi-channel pipette to efficiently remove medium from wells

### Plate Seeding

How long to achieve 80% confluence? To start with, I will try seeding ~140K cells per well with the expectation, based on previous experiments with 12-well plates, that the cell count will quadruple in one day to 560K. ~80% confluence for a 12-well plate represented about 4.5 million cells per well, and we are estimating the area of a 96-well plate well to be 1/8 that of a 12-well plate well.

### Transfection

| Reagent                   | 12-well Volume (ul/well) | 96-well Volume (ul/well) | Dilution |
|---------------------------|--------------------------|--------------------------|----------|
| Plasmids                  | 1                        | 1                        | 1:8      |
| PHH                       | 1.5                      | 1.5                      | 1:8      |
| pCD                       | 0.67                     | 0.67                     | 1:8      |
| OPTIMEM + Lipofectamine MM | 252.5                    | 31.56                    | 1:1      |



### Plate layout
|  1                |   2   |  3   |  4   |  5   |   6  |  7   |  8   | 9 | 10 | 11| 12|
|------------------|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Mock             | Mock | PHH | PHH | pCD | pCD | Vic | Vic |
| Re-run pt2 replicate |      |     |     |     |     |     |     |
| Re-run pt2 replicate |      |     |     |     |     |     |     |
| Full-PB2 1    |      |     |     |     |     |     |     |
| Full-PB2 2    |      |     |     |     |     |     |     |
| 10x     |   10x  |  20x   |   20x  |  40x   |  40x   |  80x   |  80x   |
|      |      |     |     |     |     |     |     |
|      |      |     |     |     |     |     |     |
|                  |      |     |     |     |     |     |     |
|                  |      |     |     |     |     |     |     |
|                  |      |     |     |     |     |     |     |


### Seeding

Passage 5

| 1      | 2       | 3      | 4      | 5      | 6      | 7      | 8      | 9      | 10     | 11     | 12     |
|--------|---------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 58600 | 58600  | 58600 | 58600 | 58600 | 58600 | 58600 | 58600  | 58600 | 58600 | 58600 | 58600 |
| -      | -       | -      | -      | -      | -      | -      | -      | -      | -      | -      | -      |
| -      | -       | -      | -      | -      | -      | -      | -      | -      | -      | -      | -      |
| -      | -       | -      | -      | -      | -      | -      | -      | -      | -      | -      | -      |
| -      | -       | -      | -      | -      | -      | -      | -      | -      | -      | -      | -      |
|  |  | 29300  | 29300   | 14650  | 14650  | 7325  | 7325  | 3663   | 3663   | 1831 | 1831 |
|  29300      |     29300    |    29300    |   29300     |   29300     |    29300    |  29300      |     29300    |    29300    |   29300     |   29300     |    29300    |

Cell-count: 284E4 cells/mL. To seed 150000 cells per well, would need 50 ul/well. Decided to lower it to 20ul of cells in 180ul of DMEM.

2016-11-09 Notes:

There were some difficulties in working with the tray for multi-channel pipetting. It is necessary to mix the DMEM with the cell solution before seeding, or else there's not enough liquid volume to successfully use multi-channel pipette. I had to draw back up cells that I had already dispensed in the first row to resuspend them in greater quantities of DMEM. Thus the first row has a much higher cell density than rows 2-5. However, the relative cell count in wells in row 6 is consistent with rows 2-5.

2016-11-10 Notes:

The first row wells have uneven cell coverage, and are about 80% confluent. I've decided not to transfect them because the results would not be comparable the rest of the samples. An online guide (https://www.qiagen.com/us/resources/molecular-biology-methods/transfection/) recommends seeding a max of 30000 cells for next-day transfection at 40-80% confluence, and that seems a reasonable guideline to go by in the future.
