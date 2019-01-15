import argparse
import subprocess

"""
    Created by Mohsen Naghipourfar on 2019-01-18.
    Email : mn7697np@gmail.com or naghipourfar@ce.sharif.edu
    Website: http://ce.sharif.edu/~naghipourfar
    Github: https://github.com/naghipourfar
    Skype: mn7697np
"""


class BackgroundModel(object):
    def __init__(self, method, data_path, output="", r_home=""):
        self.method = method
        self.data_path = data_path
        self.output = output
        self.r_home = r_home

    def check_validity(self):
        if self.method is None:
            raise Exception("Please Specify a method for Background model")
        if not self.data_path.endswith(".matrix"):
            raise Exception("Data path is not a valid path. (It must be in .matrix format)")
        if self.r_home == "":
            raise Exception("R home is not specified")

    def run(self):
        command = self.r_home + " " + self.method + ".R"
        if self.method.lower() == "gothic":
            subprocess.call(command)
        elif self.method.lower() == "maxhic":  # TODO: maxHiC is in python
            pass
        elif self.method.lower() == "fithic":
            subprocess.call(command)
        elif self.method.lower() == "chicago":
            subprocess.call(command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='BackgroundModel.py -f file -m gothic -r /usr/local/bin/R -o output/bg_output/',
        add_help=False, formatter_class=argparse.RawDescriptionHelpFormatter)

    group = parser.add_argument_group("Required Parameters")
    group.add_argument('-f', '--file', nargs='+', help='', metavar='', required=True)
    group.add_argument('-m', '--method', nargs='+', help='', metavar='', required=True)
    group.add_argument('-r', '--rhome', default='r', metavar='', required=True)
    group.add_argument('-o', '--output', default='', metavar='', required=True)

    args = vars(parser.parse_args())

    bg_model = BackgroundModel(**args)
    bg_model.run()
