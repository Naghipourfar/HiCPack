
library(GOTHiC)
## data(lymphoid_chr20_paired_filtered)



dirPath <- system.file("extdata", package="HiCDataLymphoblast")
fileName <- list.files(dirPath, full.names=TRUE)[4]
restrictionFile <- list.files(dirPath, full.names=TRUE)[3]
binom=GOTHiChicup(fileName, sampleName='lymphoid_chr20', res=1000000,
restrictionFile, cistrans='all', parallel=FALSE, cores=NULL)

