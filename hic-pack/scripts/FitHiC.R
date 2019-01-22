library("FitHiC")
library("optparse") # TODO: add optparse package to dependencies

option_list = list(
  make_option(c("-f", "--frags"), type="character", default="../bin/Data/output/bg_results/FitHiC_Fragments.bed", 
              help="Fragments BED File", metavar="character"),
  make_option(c("-i", "--inters"), type="character", default="../bin/Data/output/bg_results/FitHiC_Interactions.bed", 
              help="Interactions BED File", metavar="character"),
  make_option(c("-o", "--out"), type="character", default="../bin/Data/output/bg_results/", 
              help="output files", metavar="character"),
  make_option(c("-p", "--noOfPasses"), type="integer", default=1, 
              help="number of Passes after initial fit", metavar="character"),
  make_option(c("-m", "--mappabilityThreshold"), type="integer", default=1, 
              help="Minimum number of hits per locus that has to exist to call it mappable", metavar="character"),
  make_option(c("-n", "--libname"), type="character", default="SAMPLE", 
              help="Name of the library that is analyzed to be used for plots", metavar="character"),
  make_option(c("-u", "--distUpThres"), type="integer", default=250000, 
              help="Upper bound on the intra-chromosomal distance range", metavar="character"),
  make_option(c("-l", "--distLowThres"), type="integer", default=10000, 
              help="Lower bound on the intra-chromosomal distance range", metavar="character")
); 

current.directory <- dirname(parent.frame(2))
setwd(current.directory)

FitHiC(option_list$frags, 
       option_list$inters, 
       option_list$out,
       option_list$noOfPasses,
       option_list$mappabilityThreshold,
       option_list$libname,
       option_list$distUpThres, 
       option_list$distLowThres)
