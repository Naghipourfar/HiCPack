"""
    Created by Mohsen Naghipourfar on 2019-01-25.
    Email : mn7697np@gmail.com or naghipourfar@ce.sharif.edu
    Website: http://ce.sharif.edu/~naghipourfar
    Github: https://github.com/naghipourfar
    Skype: mn7697np
"""
import argparse
import os
import subprocess

control_file = """S = 50										# max. size of TAD (in bins)\nM = 25										# max. number of TADs in each tad-tree\np = 3										# boundary index parameter\nq = 12										# boundary index parameter\n\ngamma = 500									# balance between boundary index and squared error in score function\ncontact_map_path = chr12.txt,chr13.txt		# comma separated (no spaces!!) list of paths to input contact matrices, formatted as matrix of numbers without column or row labels\ncontact_map_name = chr12,chr13				# comma separated (no spaces!!) list of names of contact matrices\nN = 400,400									# comma separated (no spaces!!) list of numbers of TADs to use, one for each contact map in previous line\noutput_directory = ./output					# directory to output TAD annotations as BED files"""


class TADCalling(object):
    def __init__(self, method, file, output="../bin/Data/output/tad_results/", rhome="/usr/local/bin/Rscript",
                 scripts="./", verbose=False, samplename="SAMPLENAME", binsize=100000):
        self.method = method.lower()
        self.matrix_path = file
        self.output = output
        self.r_home = rhome
        self.scripts = scripts
        self.verbose = verbose
        self.sample_name = samplename
        self.bin_size = binsize
        self.data = {}
        self.check_validity()
        self.get_tad_options()
        self.prepare_data()

    def check_validity(self):
        return True

    def get_tad_options(self):
        with open("config-hicpack.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.__contains__("TAD_OPTIONS"):
                    self.options = line[14:]

    def prepare_data(self):
        self.save_path = f"tad_results/{self.method}/{self.sample_name}_{self.bin_size}/"
        os.makedirs(self.save_path, exist_ok=True)
        if self.method == "tadtree":
            with open(f"tad_results/{self.sample_name}/control_file.txt", "w") as f:
                f.write(control_file)

    def run(self):
        command = self.r_home + " " + self.scripts + self.method + ".R "
        if self.method == "hicseg":
            command += f" -i {self.matrix_path} -s {self.sample_name} -b {self.bin_size} {self.options}"
            print(command)
            subprocess.call([command], shell=True)
        elif self.method == "tadtree":
            command = f"python {self.scripts}{self.method}.py"
            command += f"{self.save_path}"
            print(command)
            subprocess.call([command], shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='TADCalling.py -f file -m hicseg -r /usr/local/bin/Rscript -o output/tad_output/',
        add_help=False, formatter_class=argparse.RawDescriptionHelpFormatter)

    required_group = parser.add_argument_group("Required Parameters")
    required_group.add_argument('-f', '--file', help='', metavar='', required=True)
    required_group.add_argument('-m', '--method', help='', metavar='', required=True)
    required_group.add_argument('-o', '--output', default='', metavar='', required=True)
    required_group.add_argument('-n', '--samplename', default='SAMPLENAME', metavar='', required=True)
    required_group.add_argument('-b', '--binsize', default=1000000, metavar='', required=True)

    optional_group = parser.add_argument_group("Optional Parameters")
    optional_group.add_argument('-r', '--rhome', default='/usr/local/bin/Rscript --vanilla', metavar='', required=False)
    optional_group.add_argument('-s', '--scripts', default='./', metavar='', required=False)

    args = vars(parser.parse_args())

    tad_model = TADCalling(**args)  # Print log or not?
    tad_model.run()
