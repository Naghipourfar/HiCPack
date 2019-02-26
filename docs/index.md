# HiC-Pack
[![PyPI version](https://badge.fury.io/py/hic-pack.svg)](https://badge.fury.io/py/hic-pack) [![Build Status](https://travis-ci.org/Naghipourfar/HiC-Pack.svg?branch=master)](https://travis-ci.org/Naghipourfar/HiC-Pack) [![Documentation Status](https://readthedocs.org/projects/hic-pack/badge/?version=latest)](https://hic-pack.readthedocs.io/en/latest/?badge=latest)

![](./logo/logo-main.png)
## Introduction
HiC-Pack is an Integrated package for Hi-C Data Analysis
HiC-Pack is a high-level API, written in Python.
It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

HiC-Pack is compatible with: Python 3.6-3.7.

## Main Principles
HiC-Pack has some main principles:
  
- __User Friendly__: HiC-Pack is an API designed for human beings, not machines. HiC-Pack offers consistent & simple APIs, it minimizes the number of user actions required for a common use case, and it provides clear feedback upon user error.

- __Modularity__: A model is understood as a sequence or a graph of standalone modules that can be plugged together with as few restrictions as possible. In particular, embedding methods, semi-supervised algorithms schemes are all standalone modules that you can combine to create your own new model.

- __extensibility__: It's very simple to add new modules, and existing modules provide examples. To be able to easily create new modules allows HiC-Pack suitable for advanced research.

- __Python Implementation__: All models are described in Python code, which is compact, easier to debug, and allows for ease of extensibility.

## Getting Started: A Simple Example
```bash

./HiC-Pack.bash -i ./data/input/ -o ./data/output -c ../config-hicpack.txt [-s ANALYSIS_STEP] [-p] [-h] [-v]
```
## Support
Please feel free to ask questions:

- [Mohsen Naghipourfar](mailto:mn7697np@gmail.com)

You can also post bug reports and feature requests in [GitHub issues](https://github.com/Naghipourfar/HiC-Pack/issues). Please Make sure to read our guidelines first.

