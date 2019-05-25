library("FitHiC")
library("optparse") 

option_list = list(
  make_option(c("-f", "--frags"), type="character", default="../bin/Data/output/bg_results/FitHiC_Fragments.bed", 
              help="Fragments BED File", metavar="character"),
  make_option(c("-i", "--inters"), type="character", default="../bin/Data/output/bg_results/FitHiC_Interactions.bed", 
              help="Interactions BED File", metavar="character"),
  make_option(c("-o", "--out"), type="character", default="../bin/Data/output/bg_results/", 
              help="output files", metavar="character"),
  make_option(c("-p", "--noOfPasses"), type="integer", default=1, 
              help="number of Passes after initial fit", metavar="character"),
  make_option(c("-a", "--bias"), type="character", default="none", 
              help="Bias file", metavar="character"),
  make_option(c("-m", "--mappabilityThreshold"), type="integer", default=1, 
              help="Minimum number of hits per locus that has to exist to call it mappable", metavar="character"),
  make_option(c("-n", "--libname"), type="character", default="SAMPLE", 
              help="Name of the library that is analyzed to be used for plots", metavar="character"),
  make_option(c("-u", "--distUpThres"), type="integer", default=250000, 
              help="Upper bound on the intra-chromosomal distance range", metavar="character"),
  make_option(c("-l", "--distLowThres"), type="integer", default=10000, 
              help="Lower bound on the intra-chromosomal distance range", metavar="character"),
  make_option(c("-b", "--binsize"), type="integer", default=100000, 
              help="Lower bound on the intra-chromosomal distance range", metavar="character")
); 
opt <- parse_args(OptionParser(option_list=option_list))
# current.directory <- dirname(parent.frame(2))
# setwd(current.directory)
FitHiC(fragsfile = opt$frags,
       intersfile = opt$inters, 
       biasfile = opt$bias,
       outdir = opt$out,
       noOfPasses = opt$noOfPasses,
       mappabilityThreshold = opt$mappabilityThreshold,
       libname = opt$libname,
       distUpThres = opt$distUpThres, 
       distLowThres = opt$distLowThres
       )
 # TODO: change to python