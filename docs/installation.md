## Installation

The easiest way to get HiCPack is through pip using the following command:
```bash
sudo pip install hicpack
```
If you are using a virtualenv, you may want to avoid using sudo:
```bash
pip install HiCPack
```
This should install all the dependencies in addition to the package.

- __Alternatively: install HiCPack from the GitHub source:__

You can also get SeqLearner from Github using the following steps:
First, clone SeqLearner using `git`:

```bash
git clone https://github.com/Naghipourfar/HiCPack
```

Then, `cd` to the SeqLearner folder and run the install command:
```bash
cd HiCPack
pip install -r requirements
python setup.py -q install
```

On Windows machines you may need to download a C++ compiler if you wish to build from source yourself. 

## Dependencies
The requirements for SeqLearner can be found in the requirements.txt file in the repository, and include numpy, pandas, tensorflow, keras, gensim, pomegranate, and matplotlib.

- [__numpy__](http://numpy.org): The fundamental package for scientific computing.

- [__pandas__](https://pandas.pydata.org): The library which provides high-performance, easy-to-use data structures and data analysis tools for the Python.

- [__matplotlib__](https://matplotlib.org): a Python 2D plotting library which produces publication quality figures

