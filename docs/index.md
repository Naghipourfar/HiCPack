# HiCPack
[![PyPI version](https://badge.fury.io/py/hicpack.svg)](https://badge.fury.io/py/hicpack) [![Build Status](https://travis-ci.org/Naghipourfar/HiCPack.svg?branch=master)](https://travis-ci.org/Naghipourfar/HiCPack) [![Documentation Status](https://readthedocs.org/projects/hicpack/badge/?version=latest)](https://hicpack.readthedocs.io/en/latest/?badge=latest)

![](./logo/logo-main.png)
## Introduction
HiCPack is an Integrated package for Hi-C Data Analysis
HiCPack is a high-level API, written in Python.
It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

HiCPack is compatible with: Python 3.6-3.7.

## Main Principles
HiCPack has some main principles:
  
- __User Friendly__: HiCPack is an API designed for human beings, not machines. HiCPack offers consistent & simple APIs, it minimizes the number of user actions required for a common use case, and it provides clear feedback upon user error.

- __Modularity__: A model is understood as a sequence or a graph of standalone modules that can be plugged together with as few restrictions as possible. In particular, embedding methods, semi-supervised algorithms schemes are all standalone modules that you can combine to create your own new model.

- __extensibility__: It's very simple to add new modules, and existing modules provide examples. To be able to easily create new modules allows HiCPack suitable for advanced research.

- __Python Implementation__: All models are described in Python code, which is compact, easier to debug, and allows for ease of extensibility.

## Getting Started: HiCPack Usage
```text
HiCPack --help
  usage : HiC-Pack -i INPUT -o OUTPUT -c CONFIG [-s ANALYSIS_STEP] [-p] [-h] [-v]
  Use option -h|--help for more information

  HiC-Pack 1.0.10
  ---------------
  OPTIONS

   -i|--input INPUT : input data folder; Must contains a folder per sample with input files
   -o|--output OUTPUT : output folder
   -c|--conf CONFIG : configuration file for Hi-C processing
   [-p|--parallel] : if specified run HiC-Pro on a cluster
   [-s|--step ANALYSIS_STEP] : run only a subset of the HiC-Pro workflow; if not specified the complete workflow is run
      mapping: perform reads alignment
      proc_hic: perform Hi-C filtering
      quality_checks: run Hi-C quality control plots
      build_contact_maps: build raw inter/intrachromosomal contact maps
      bg_model: Applies a specific background model to raw contact maps
      visualization: Provide some visualizations for contact maps
      tadcalling: Runs a specific TAD Calling algorithm on significant interactions
   [-h|--help]: help
   [-v|--version]: version
```
## Support
Please feel free to ask questions:

- [Mohsen Naghipourfar](mailto:mn7697np@gmail.com)

You can also post bug reports and feature requests in [GitHub issues](https://github.com/Naghipourfar/HiCPack/issues). Please Make sure to read our guidelines first.

