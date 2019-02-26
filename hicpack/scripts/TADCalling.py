"""
    Created by Mohsen Naghipourfar on 2019-01-25.
    Email : mn7697np@gmail.com or naghipourfar@ce.sharif.edu
    Website: http://ce.sharif.edu/~naghipourfar
    Github: https://github.com/naghipourfar
    Skype: mn7697np
"""


class TADCalling(object):
    def __init__(self, method, file, output="../bin/Data/output/tad_results/", rhome="/usr/local/bin/Rscript",
                 scripts="./",
                 verbose=False):
        self.method = method
        self.file_path = file
        self.output = output
        self.r_home = rhome
        self.scripts = scripts
        self.verbose = verbose
        self.data = {}
        self.check_validity()
        self.prepare_data()

    def check_validity(self):
        return True

    def prepare_data(self):
        return

    def run(self):
        pass


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     usage='BackgroundModel.py -f file -m hicseg -r /usr/local/bin/Rscript -o output/tad_output/',
    #     add_help=False, formatter_class=argparse.RawDescriptionHelpFormatter)
    #
    # required_group = parser.add_argument_group("Required Parameters")
    # required_group.add_argument('-f', '--file', help='', metavar='', required=True)
    # required_group.add_argument('-m', '--method', help='', metavar='', required=True)
    # required_group.add_argument('-o', '--output', default='', metavar='', required=True)
    #
    # optional_group = parser.add_argument_group("Optional Parameters")
    # optional_group.add_argument('-r', '--rhome', default='/usr/local/bin/R', metavar='', required=False)
    # optional_group.add_argument('-s', '--scripts', default='/usr/local/bin/R', metavar='', required=False)
    #
    # args = vars(parser.parse_args())

    # bg_model = BackgroundModel(**args)
    tad_model = TADCalling(method="HiCSeg",  # Background model to be applied
                           file="../bin/Data/output/hic_results/matrix/SRR442155/raw/20000/",
                           # input BED and .matrix files (HiC-Pro contact maps)
                           output="../bin/Data/output/bg_results/",  # output path for BG model
                           rhome="/usr/local/bin/Rscript --vanilla",  # R home
                           scripts="./",  # Scripts path (in order to run FitHiC.R)
                           verbose=True)  # Print log or not?
    tad_model.run()
