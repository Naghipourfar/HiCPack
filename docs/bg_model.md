# Background Models
Background models are tools for statistical confidence estimates to chromosomal contact maps produced by genome-wide genome architecture assays such as Hi-C.
There is a wrapper python class for all background models which called `BackgroundModel`. You can find the usage and its API later on this web-page.
Here is some introduction about the methods which are supported in HiCPack.

## FitHiC

Fit-Hi-C was initially developed by Ferhat Ay, Timothy Bailey, and William Noble January 19th, 2014. It is currently maintained and updated by Ferhat Ay (ferhatay@lji.org) and Arya Kaul (akaul@lji.org) at the Ay Lab in the La Jolla Institute for Allergy and Immunology.

### FitHiC usage
This method will accept some arguments such as fragments file, interaction file and a bias file(Optional).

- __Fragments File__: This file stores the information about midpoints (or start indices) of the fragments. It should consist of 5 columns: first column stands for chromosome name; third column stands for the midPoint; fourth column stands for the hitCount; second column and fifth column will be ignored so you can set them to 0. HitCount (4th column) is only used for filtering in conjuction with the “mappabilityThreshold” option. By default setting bins that need to be filtered to “0” and others to “1” and leaving the mappabilityThreshold option to its default value of 1 is enough. You do not need to compute hitCount (4th column) unless you will explicitly filter using a custom threshold on marginal counts set by the “mappabilityThreshold” option.
Here is a sample table:

| Chromosome.Name | Column.2 | Mid.Point | Hit.Count | Column.5 |
|-----------------|----------|-----------|-----------|----------|
| chr1            | 0        | 20000     | 1         | 0        |
| chr1            | 0        | 60000     | 1         | 0        |
| chr1            | 0        | 100000    | 1         | 0        |


- __Interactions File__: This file stores the information about interactions between fragment pairs. It should consist of 5 columns: first column and third column stand for the chromosome names of the fragment pair; second column and fourth column stand for midPoints of the fragment pair; fifth column stands for contact count between the two bins. Make sure that midpoints in this file match those in fragsfile and in biasfile (when normalization is applied). Make sure to use RAW contact counts and NOT the normalized counts. Use BIASFILE if normalization is to be taken into account (Highly suggested). 
Here's a sample table:

| Chromosome1.Name | Mid.Point.1 | Chromosome2.Name | Mid.Point.2 | Hit.Count |
|-----------------|----------|-----------|-----------|----------|
| chr1            | 100020000        | chr1     | 100100000         | 201        |
| chr1            | 100020000        | chr1     | 100140000         | 232        |
| chr1            | 100020000        | chr1    | 100180000         | 178        |

- __Bias File__:FitHiC works with matrix balancing-based normalization methods such as (ICE, KR or Vanilla Coverage). These methods provide a bias value per bin/locus, the vector of which should be centered on 1 so that:
bias = 1 (expected amount of count/visibility) bias > 1 (higher than expected count) bias < 1 (lower than expected count)

| Chromosome.Name | Mid.Point | Bias |
|-----------------|-----------|------|
| chr1            | 20000     | 1    |
| chr1            | 60000     | 1    |
| chr1            | 100000    | 1    |

You can easily use FitHiC in background model step by setting the `BG_MODEL` parameter in HiCPack config file.

## GOTHiC
 
GOTHiC is a Hi-C analysis package using a cumulative binomial test to detect interactions between distal genomic loci that have significantly more reads than expected by chance in Hi-C experiments. It takes mapped paired NGS reads as input and gives back the list of significant interactions for a given bin size in the genome.

You can easily use GOTHiC in background model step by setting the `BG_MODEL` parameter in HiCPack config file.

## MaxHiC

MaxHiC is another tool for using in background model step.
You can easily use MaxHiC in background model step by setting the `BG_MODEL` parameter in HiCPack config file.

