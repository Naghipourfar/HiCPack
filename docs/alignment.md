# Alignment algorithms
In the first step after getting the fastq files. The alignment step begins to work. There are multiple alignment algorithms which you can use in HiCPack simply by setting the `ALIGNMENT_ALGORITHM` in HiCPack config. 

__NOTE__: for now, Bowtie2 is just supported by HiCPack. However, bwa after testing and debugging process will be supported ASAP. 

## Bowtie 2

Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s of characters to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index (based on the Burrows-Wheeler Transform or BWT) to keep its memory footprint small: for the human genome, its memory footprint is typically around 3.2 gigabytes of RAM. Bowtie 2 supports gapped, local, and paired-end alignment modes. Multiple processors can be used simultaneously to achieve greater alignment speed.

You can easily use bowtie2 in HiCPack by passing your optional arguments for global(`BOWTIE2_GLOBAL_OPTIONS`) and local(`BOWTIE2_LOCAL_OPTIONS`) alignment. Bowtie also needs the path to indexes of reference genome so you can set this by passing the __absolute__ path to `BOWTIE2_IDX_PATH` in HiCPack config.

## Burrows-Wheeler Aligner (BWA) 

BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM. The first algorithm is designed for Illumina sequence reads up to 100bp, while the rest two for longer sequences ranged from 70bp to 1Mbp. BWA-MEM and BWA-SW share similar features such as long-read support and split alignment, but BWA-MEM, which is the latest, is generally recommended for high-quality queries as it is faster and more accurate. BWA-MEM also has better performance than BWA-backtrack for 70-100bp Illumina reads.