import os

from setuptools import setup, find_packages

def get_long_description():
    with open(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'README.md'
    ), encoding='utf8') as fp:
        return fp.read()


setup(name='hicpack',
      version='1.0.4',
      description='An Integrated package for Hi-C Data Analysis',
      long_description=get_long_description(),
      long_description_content_type="text/markdown",
      url='https://github.com/Naghipourfar/HiC-Pack.bash.bash',
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
