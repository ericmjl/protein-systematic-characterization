## Goals

Following up on Vivian's set of excellently-conducted prior experiments (date: [2016-09-20](../20160920-Taq-Mn-mutagenesis/20160912-mgcl2-taq-series.md)), I wanted to fill in the blanks w.r.t. the concentrations not yet tested and sequenced.

As such, the goals are below:

1. Produce replicate PCRs for a range of Mn<sup>2+</sup> concentrations.
1. Sequence them to count the number of mutations present.

## PCR Setup

### PCR

- Primers:
    - Fw: EM-28
    - Re: EM-27
- Template: VicPB2

### Reaction conditions

| [Mn] (mM) | Replicates | 96-well plate row |
|:---------:|:----------:|:-----------------:|
|    0.00   |      3     |         A         |
|    0.10   |      3     |         B         |
|    0.20   |      3     |         C         |
|    0.25   |      3     |         D         |
|    0.30   |      3     |         E         |
|    0.35   |      3     |         F         |
|    0.40   |      3     |         G         |
|    0.50   |      3     |         H         |

Total estimated cost @ $6/sequencing reaction: $144.

### PCR Master Mix

| Ingredient   | 1 Rxn Vol (µL) | MM x26.4 |
|--------------|:--------------:|:--------:|
| Water        |       17       |   448.8  |
| 2X MyTaq Red |       25       |    660   |
| 10X MnCl2    |        5       |    N/A   |
| Template     |        1       |   26.4   |
| Fw Primer    |        1       |   26.4   |
| Re Primer    |        1       |   26.4   |

### PCR Program

MyTaq Red

- 68ºC annealing
- 2 min extension @ 72ºC
- 40 cycles in total

## PCR Purification

Didn't bother with gel checking, as we know from prior experience that this PCR reaction works reliably.

Table below shows concentration of DNA (also available in [TSV](./20161006-hackytaq-pcr-purification.tsv) format.):

| #  | Sample ID | User name        | Date and Time        | Nucleic Acid Conc. |  Unit | A260  | A280  | 260/280 | 260/230 | Sample Type | Factor | [Mn2+] (mM) |
|----|:---------:|------------------|----------------------|--------------------|:-----:|-------|-------|---------|---------|:-----------:|:------:|:-----------:|
| 1  |   IH-01   | Eric Jinglong Ma | 10/6/2016 2:45:46 PM | 123.3              | ng/µl | 2.465 | 1.14  | 2.16    | 2.72    |     DNA     |   50   |     0.00    |
| 2  |   IH-02   | Eric Jinglong Ma | 10/6/2016 2:46:42 PM | 136.1              | ng/µl | 2.721 | 1.319 | 2.06    | 2.51    |     DNA     |   50   |     0.00    |
| 3  |   IH-03   | Eric Jinglong Ma | 10/6/2016 2:47:06 PM | 141.9              | ng/µl | 2.838 | 1.35  | 2.1     | 2.67    |     DNA     |   50   |     0.00    |
| 4  |   IH-04   | Eric Jinglong Ma | 10/6/2016 2:47:28 PM | 122.2              | ng/µl | 2.443 | 1.142 | 2.14    | 2.71    |     DNA     |   50   |     0.10    |
| 5  |   IH-05   | Eric Jinglong Ma | 10/6/2016 2:47:51 PM | 100.9              | ng/µl | 2.017 | 1.013 | 1.99    | 2.36    |     DNA     |   50   |     0.10    |
| 6  |   IH-06   | Eric Jinglong Ma | 10/6/2016 2:48:13 PM | 108.3              | ng/µl | 2.165 | 1.067 | 2.03    | 2.43    |     DNA     |   50   |     0.10    |
| 7  |   IH-07   | Eric Jinglong Ma | 10/6/2016 2:48:34 PM | 106.5              | ng/µl | 2.13  | 1.017 | 2.09    | 2.46    |     DNA     |   50   |     0.20    |
| 8  |   IH-08   | Eric Jinglong Ma | 10/6/2016 2:48:56 PM | 99.9               | ng/µl | 1.998 | 0.979 | 2.04    | 2.54    |     DNA     |   50   |     0.20    |
| 9  |   IH-09   | Eric Jinglong Ma | 10/6/2016 2:49:18 PM | 117.5              | ng/µl | 2.35  | 1.127 | 2.08    | 2.46    |     DNA     |   50   |     0.20    |
| 10 |   IH-10   | Eric Jinglong Ma | 10/6/2016 2:49:41 PM | 101                | ng/µl | 2.02  | 0.974 | 2.07    | 2.51    |     DNA     |   50   |     0.25    |
| 11 |   IH-11   | Eric Jinglong Ma | 10/6/2016 2:50:01 PM | 96.4               | ng/µl | 1.928 | 0.91  | 2.12    | 2.43    |     DNA     |   50   |     0.25    |
| 12 |   IH-12   | Eric Jinglong Ma | 10/6/2016 2:50:22 PM | 99.2               | ng/µl | 1.983 | 0.959 | 2.07    | 2.39    |     DNA     |   50   |     0.25    |
| 13 |   IH-13   | Eric Jinglong Ma | 10/6/2016 2:50:43 PM | 75.8               | ng/µl | 1.515 | 0.74  | 2.05    | 2.42    |     DNA     |   50   |     0.30    |
| 14 |   IH-14   | Eric Jinglong Ma | 10/6/2016 2:51:03 PM | 89.5               | ng/µl | 1.789 | 0.828 | 2.16    | 2.72    |     DNA     |   50   |     0.30    |
| 15 |   IH-15   | Eric Jinglong Ma | 10/6/2016 2:51:23 PM | 92.6               | ng/µl | 1.852 | 0.828 | 2.24    | 2.63    |     DNA     |   50   |     0.30    |
| 16 |   IH-16   | Eric Jinglong Ma | 10/6/2016 2:51:42 PM | 84.5               | ng/µl | 1.69  | 0.825 | 2.05    | 2.47    |     DNA     |   50   |     0.35    |
| 17 |   IH-17   | Eric Jinglong Ma | 10/6/2016 2:52:00 PM | 81.4               | ng/µl | 1.628 | 0.81  | 2.01    | 2.4     |     DNA     |   50   |     0.35    |
| 18 |   IH-18   | Eric Jinglong Ma | 10/6/2016 2:52:19 PM | 87.6               | ng/µl | 1.751 | 0.806 | 2.17    | 2.5     |     DNA     |   50   |     0.35    |
| 19 |   IH-19   | Eric Jinglong Ma | 10/6/2016 2:52:41 PM | 93                 | ng/µl | 1.859 | 0.874 | 2.13    | 2.38    |     DNA     |   50   |     0.40    |
| 20 |   IH-20   | Eric Jinglong Ma | 10/6/2016 2:53:02 PM | 84.7               | ng/µl | 1.695 | 0.842 | 2.01    | 2.34    |     DNA     |   50   |     0.40    |
| 21 |   IH-21   | Eric Jinglong Ma | 10/6/2016 2:53:21 PM | 84.2               | ng/µl | 1.684 | 0.74  | 2.27    | 2.79    |     DNA     |   50   |     0.40    |
| 22 |   IH-22   | Eric Jinglong Ma | 10/6/2016 2:54:23 PM | 77.4               | ng/µl | 1.548 | 0.693 | 2.23    | 2.54    |     DNA     |   50   |     0.50    |
| 23 |   IH-23   | Eric Jinglong Ma | 10/6/2016 2:54:44 PM | 67.4               | ng/µl | 1.347 | 0.593 | 2.27    | 2.76    |     DNA     |   50   |     0.50    |
| 24 |   IH-24   | Eric Jinglong Ma | 10/6/2016 2:55:04 PM | 72.5               | ng/µl | 1.45  | 0.606 | 2.39    | 2.79    |     DNA     |   50   |     0.50    |

## Sequencing

All samples were sent for Sanger sequencing. ([Order](./20161006-hackytaq-sequencing-order.pdf))


## Results

I very "hackily" created a multiple sequence alignment of this round's sequence data by combining it with the data in the [temp-hackytaq](../temp-20160927-hackytaq) data. Viewing it [online](./alignment.png) showed that the 0 mM Mn<sup>2+</sup> controls all showed high mutation rates relative to the gold standard Victoria PB2 sequence.

I think there may have been an error in my sample preparation. I will get Vivian to observe how I set up the PCR to see whether I'm doing something differently from what she did.
