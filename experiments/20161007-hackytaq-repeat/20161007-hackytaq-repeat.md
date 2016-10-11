## Goals

The [last hacky-taq experiment](../20161006-hackytaq-replicates/20161006-hackytaq-replicate.md) I ran showed results that were inconsistent with the results that Vivian had from [her run](../20160920-Taq-Mn-mutagenesis/20160912-mgcl2-taq-series.md). Briefly:

1. Vivian's experiments yielded PCR products that, when Sanger-sequenced, showed on the order of 1-10 mutations across the PCR product.
1. On the other hand, my PCR products showed on the order of 100s of mutations.
1. Additionally, my no-manganese control (which I expected to have 0 to few mutations) showed hundreds of mutations as well.

I repeated the experiment with the following modifications:

1. Instead of doing triplicates, only ran single PCR reactions per concentration of manganese.
1. I had Vivian observe my setting up of the experiments.
1. I tested the following concentrations:
    1. 0.0 mM
    1. 0.05 mM
    1. 0.1 mM
    1. 0.2 mM
    1. 0.25 mM
    1. 0.30 mM
    1. 0.35 mM
    1. 0.4 mM
    1. 0.5 mM

## Gel

One possible hypothesis as to why there were poor sequencing results was because of mixed PCR products. This was raised by the Genewiz staff last week on Friday (7 October 2016). As such, I will run a gel of this PCR set.

Gel composition:

- 1% (w/v) LE agarose in TBE
- 10 µL Ethidium bromide

Loaded 5 µL of PCR product and 5 µL of gel.

Gel order (from left to right):

- 100 bp ladder
- 0.0 mM
- 0.05 mM
- 0.1 mM
- 0.2 mM
- 0.25 mM
- 0.3 mM
- 0.35 mM
- 0.4 mM
- 0.5 mM
- 100 bp ladder

Gel Image:

![gel](./gel.jpg)

## Interpretation

One look at the gel and I realized what was going wrong. The melting temperature was incorrect. I had used 68ºC in this PCR round; in fact, it should have been 60ºC.

The next steps are clear: do a repeat run but with Tm at 60ºC.

I discarded the current PCR products.

## Re-run PCR

I re-ran the PCR, except this time making sure to set the Tm at 60ºC.

PCR master mix follows the composition of [previous experiment](../20161006-hackytaq-replicates/20161006-hackytaq-replicate.md), except master mix volumes are calculated for 9.9 reactions.

For convenience (for my future self), I am adding here what the exact PCR program was:

| Temperature (ºC) | Time (min, sec) | Cycles |
|------------------|-----------------|--------|
| 95               | 1, 00           | 1      |
| 95               | 0, 15           | 40     |
| 60               | 0, 15           | 40     |
| 72               | 2, 00           | 40     |
| 72               | 10, 00          | 1      |
| 4                | inf             | 1      |


## Gel

Here's a gel of the PCR reaction at 60ºC.

![gel-run-2](./gel-run-2.jpg)

They are all correct, so I will PCR purify the reactions and send them in for sequencing.

PCR purification concentrations are linked [here](./20161010-hackytaq-pcr-purification.tsv).

## Sequencing

Sequencing order is linked [here](./20161010-Sequencing_order.pdf). Standard composition: 10 µL of sample + 5 µL of primer.

## Alignment

I created a script (`sequencing-results/align.py`) that can be used to align the sequencing traces using Clustal Omega (v1.2.3, Mac OS X) locally.

## Results & Discussion

The sequencing results really don't look good. There shouldn't be large gaps in the middle portion of the alignment. My first gut feeling tells me that there is an error with the sequencing results, and it's likely because I'm using purified PCR products that still contain a mixture of DNA.

Let me do some meta-thinking here. We are most interested in how many mutations will show up in the final clones. However, right now with PCRs, we aren't measuring that. We are measuring (only very crudely) the number of positions in a PCR product that show up as different from the original. This may not necessarily be the number of mutations that end up in a final clone; it may well be an under-estimate, as mutations that show up in lower frequencies amongst the PCR product pool are not likely to show up as the consensus PCR product sequence.

Right now, I'm not sure if there's any more value in trying to repeat this experiment in its current state (PCR purify + sequencing), as I'm unable to replicate the results. I think the most I'm willing to do as a last attempt is to gel purify the PCR product and send it in for sequencing.

I'm also starting to think that a more sure way to measure the number of mutations that we expect to show up is to clone the PCR fragments and sequence multiple clones.

I think this should be done, but not merely for the sake of getting sequences. Perhaps the experiments can be a by-product of testing the polymerases. For example, since we have to sequence the clones that are tested anyways, might as well try doing random mutagenesis using anywhere between 0 to 0.30 mM manganese + PacBio sequencing with barcoding (oh yes! still haven't done barcoding!). May still want to Sanger sequence some of these clones anyways to confirm that the PacBio sequencing is at least consistent with the Sanger sequence.
