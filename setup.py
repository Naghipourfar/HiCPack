from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.readlines()[1]

setup(name='hicpack',
      version='1.0.0',
      description='An Integrated package for Hi-C Data Analysis',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Naghipourfar/HiCPack',
      author='Mohsen Naghipourfar',
      author_email='mn7697np@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      )
