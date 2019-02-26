# Alignment algorithms
In the first step after getting the fastq files. The alignment step begins to work. There are multiple alignment algorithms which you can use in HiCPack simply by setting the `ALIGNMENT_ALGORITHM` in HiCPack config. 

__NOTE__: for now, Bowtie2 is just supported by HiCPack. However, bwa after testing and debugging process will be supported ASAP. 

## Bowtie 2

Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s of characters to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index (based on the Burrows-Wheeler Transform or BWT) to keep its memory footprint small: for the human genome, its memory footprint is typically around 3.2 gigabytes of RAM. Bowtie 2 supports gapped, local, and paired-end alignment modes. Multiple processors can be used simultaneously to achieve greater alignment speed.

You can easily use bowtie2 in HiCPack by passing your optional arguments for global(`BOWTIE2_GLOBAL_OPTIONS`) and local(`BOWTIE2_LOCAL_OPTIONS`) alignment. Bowtie also needs the path to indexes of reference genome so you can set this by passing the __absolute__ path to `BOWTIE2_IDX_PATH` in HiCPack config.

## Burrows-Wheeler Aligner (BWA) 

BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM. The first algorithm is designed for Illumina sequence reads up to 100bp, while the rest two for longer sequences ranged from 70bp to 1Mbp. BWA-MEM and BWA-SW share similar features such as long-read support and split alignment, but BWA-MEM, which is the latest, is generally recommended for high-quality queries as it is faster and more accurate. BWA-MEM also has better performance than BWA-backtrack for 70-100bp Illumina reads.

## Alignment Results

The `bowtie_results` folder contains the results of the reads mapping. The results of first mapping step are available in the `bwt2_glob` folder, and the 2nd step in the `bwt2_loc` folder. Final BAM files, reads pairing, and mapping statistics are available on the `bwt2` folder.
Mapping statistics are available in the `.mapstat` files. The total mapping statistics per sample are available in the `'SAMPLE_NAME'.mmapstat` file.
Usually, a high fraction of reads is expected to be aligned on the genome (80-90%). Among them, we usually observed a few percent (around 10%) of step 2 aligned reads. Those reads are chimeric fragments for which we detect a ligation junction. An abnormal level of chimeric reads can reflect a ligation issue during the library preparation.
Once R1 and R2 reads are aligned on the genome, HiCPack reconstruct the pairs information. The pairing statistics are available in the `.pairstat` files. The combined pairing statistics per sample are available in the `'SAMPLE_NAME'.mpairstat` file.
The fraction of singleton or multi-hits depends on the genome complexity and the fraction of unmapped reads. The fraction of singleton is usually close to the sum of unmapped R1 and R2 reads, as it is unlikely that both mates from the same pair were unmapped.

The `hic_results` folder contains all Hi-C processed data, and is further divided in several sub-folders. The `hic_results/data` folder is used to store the valid interaction products (`.validPairs`), as well as other statisics files.
The validPairs are stored using a simple tab-delimited text format. One validPairs file is generated per reads chunk. These files are then merged in the allValidPairs, and duplicates are removed if specified in the configuration file.

### Statistics Results
Statistics about read pairs filtering are available in the `hic_results/stat/` folder. This folder has a sub-folder for each sample and each sub-folder consists of `'SAMPLE_NAME'.mRSstat` file and `.mmapstat` files. The ligation efficiency can be assessed using the filtering of valid and invalid pairs. As the ligation is a random process, 25% of each valid ligation class is expected. In the same way, a high level of dangling-end or self-circle read pairs is associated with a low quality experiment, and reveals a problem during the digestion, fill-in or ligation steps.
In case of allele specific analysis, an additional statistics file `assplit.stat` is available with the fraction of read pairs assigned to the parental genomes. Note that allele specific assignment is also available from the `.RSstat` files. Statistics from the `assplit.stat` are usually different from the ones in the `.RSstat` as they are calculated on the valid pairs after duplicates removal, whereas statistics on the `.RSstat` files are calculated for each read chunk before duplicates removal.
