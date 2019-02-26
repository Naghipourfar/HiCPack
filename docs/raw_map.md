# Raw Contact Maps

In this step HiCPack will generate binned matrix files via C++ Executable file `build_matrix`.

Additional quality controls such as fragment size distribution can be extracted from the list of valid interaction products. We usually expect to see a distribution centered around 300 pb which correspond to the paired-end insert size commonly used.
The fraction of duplicates is also presented. A high level of duplication indicates a poor molecular complexity and a potential PCR bias.
Finally, an important metric is to look at the fraction of intra and inter-chromosomal interactions, as well as long range (>20kb) versus short range (<20kb) intra-chromosomal interactions.

The contact maps are then available in the `hic_results/matrix` folder. Raw contact maps are in the `raw` folder. Note that Normalization methods are not supported in HiCPack.
The contact maps are generated for all specified resolution (available in HiCPack config file)
A contact map is defined by:

- __BED File__: A list of genomic intervals related to the specified resolution (BED format).
Here's a sample of a BED file:

```text
chr1	0	20000	1
chr1	20000	40000	2
chr1	40000	60000	3
chr1	60000	80000	4
chr1	80000	100000	5
chr1	100000	120000	6
chr1	120000	140000	7
```
- __Matrix of Interactions File__: A matrix, stored as standard triplet sparse format (i.e. list format). Based on the observation that a contact map is symmetric and usually sparse, only non-zero values are stored for half of the matrix. The user can specified if the 'upper', 'lower' or 'complete' matrix has to be stored.

Here's a sample of an interaction matrix file: 

```text
1	34467	10
3	501	2
3	72	19
3	7516	11
...
```