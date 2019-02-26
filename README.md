# HiCPack [![PyPI version](https://badge.fury.io/py/hicpack.svg)](https://badge.fury.io/py/hicpack) [![Build Status](https://travis-ci.org/Naghipourfar/HiCPack.svg?branch=master)](https://travis-ci.org/Naghipourfar/HiCPack) [![Documentation Status](https://readthedocs.org/projects/hicpack/badge/?version=latest)](https://hicpack.readthedocs.io/en/latest/?badge=latest)

<img align="center" src="./logo/logo-main.png?raw=true">
An Integrated package for Hi-C Data Analysis

## Introduction
## Getting Started

## Installation

### Dependencies
- The bowtie2 mapper
- Python (>3.5) with pysam (>=0.8.3), bx-python(>=0.5.0), numpy(>=1.8.2), and scipy(>=0.15.1) libraries.
- Note that the current version does not support python 3
- R with the RColorBrewer and ggplot2 (>2.2.1) packages
- g++ compiler
- samtools (>1.1)
- Unix sort (which support -V option) is required ! For Mac OS user, please install the GNU core utilities !

### Install using pip
```bash
pip install hicpack
```

### Install using Anaconda
```bash
conda install hicpack
```

### Install the development version
```bash
pip install flit
git clone https://github.com/Naghipourfar/hicpack
cd hicpack
flit install
```


## File Illustration
This repo is divided into 3 directories.
 1. The `hicpack` directory contains all codes and jupyter notebooks.
 2. The `hicpack/data/` directory is place where data is in.
 3. The `hicpack/results/` directory contains all results plots, Logs and etc.


## Examples
