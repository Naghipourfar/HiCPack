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
    def __init__(self, method, file, output="", rhome="", scripts=""):
        self.method = method
        self.file = file
        self.output = output
        self.r_home = rhome
        self.scripts = scripts
        self.check_validity()

    def check_validity(self):
        if self.method is None:
            raise Exception("Please Specify a method for Background model")
        if not self.file.endswith(".matrix"):
            raise Exception("Data path is not a valid path. (It must be in .matrix format)")
        if self.r_home == "":
            raise Exception("R home is not specified")

    def run(self):
        command = self.r_home + " " + self.scripts + "/" + self.method + ".R"
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

    required_group = parser.add_argument_group("Required Parameters")
    required_group.add_argument('-f', '--file', help='', metavar='', required=True)
    required_group.add_argument('-m', '--method', help='', metavar='', required=True)
    required_group.add_argument('-o', '--output', default='', metavar='', required=True)

    optional_group = parser.add_argument_group("Optional Parameters")
    optional_group.add_argument('-r', '--rhome', default='/usr/local/bin/R', metavar='', required=False)
    optional_group.add_argument('-s', '--scripts', default='/usr/local/bin/R', metavar='', required=False)

    args = vars(parser.parse_args())

    bg_model = BackgroundModel(**args)
    bg_model.run()
