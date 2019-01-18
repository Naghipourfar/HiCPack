import os
import subprocess

import pandas as pd

"""
    Created by Mohsen Naghipourfar on 2019-01-18.
    Email : mn7697np@gmail.com or naghipourfar@ce.sharif.edu
    Website: http://ce.sharif.edu/~naghipourfar
    Github: https://github.com/naghipourfar
    Skype: mn7697np
"""


class BackgroundModel(object):
    def __init__(self, method, file, output="../bin/Data/output/bg_results/", rhome="/usr/local/bin/R", scripts=""):
        self.method = method
        self.file_path = file
        self.output = output
        self.r_home = rhome
        self.scripts = scripts
        self.data = {}
        self.check_validity()
        self.prepare_data()

    def check_files(self):
        id_matrix = None
        interaction_matrix = None
        for file in os.listdir(self.file_path):
            if file.endswith(".bed"):
                id_matrix = pd.read_csv(self.file_path + file, delimiter="\t", header=None)
            elif file.endswith(".matrix"):
                interaction_matrix = pd.read_csv(self.file_path + file, delimiter="\t", header=None)
        if id_matrix is None or interaction_matrix is None:
            raise Exception("id matrix or interaction matrix not found!")
        self.data["id"] = id_matrix
        self.data["interaction"] = interaction_matrix

    def check_validity(self):
        if self.method is None:
            raise Exception("Please Specify a method for Background model")
        if self.r_home == "":
            raise Exception("R home is not specified")
        self.check_files()

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

    def prepare_data(self):
        if self.method.lower() == "fithic":
            chr_name_map = pd.DataFrame()
            chr_name_map['Chromosome.Name'] = self.data['id'].iloc[:, 0]
            chr_name_map["ID"] = self.data['id'].iloc[:, 3]

            id_name_map = chr_name_map.set_index("ID")['Chromosome.Name'].T.to_dict()

            self.frags_df = pd.DataFrame()
            self.frags_df['Chromosome.Name'] = self.data['id'].iloc[:, 0]
            self.frags_df['Column.2'] = 0
            self.frags_df['Mid.Point'] = (self.data['id'].iloc[:, 1] + self.data['id'].iloc[:, 2]) // 2
            self.frags_df['Hit.Count'] = 1
            self.frags_df['Column.5'] = 0
            self.frags_df.to_csv(self.output + self.method + "_Fragments.bed", index=None, sep="\t", header=False)

            self.frags_df["ID"] = self.data["id"].iloc[:, 3]
            name_midpoint_map = self.frags_df.set_index("ID")["Mid.Point"].to_dict()

            self.inters_df = pd.DataFrame()
            self.inters_df["Chromosome1.Name"] = self.data['interaction'].iloc[:, 0].map(id_name_map)
            self.inters_df["Mid.Point.1"] = self.data['interaction'].iloc[:, 0].map(name_midpoint_map)
            self.inters_df["Chromosome2.Name"] = self.data['interaction'].iloc[:, 1].map(id_name_map)
            self.inters_df["Mid.Point.2"] = self.data['interaction'].iloc[:, 1].map(name_midpoint_map)
            self.inters_df["Hit.Count"] = self.data['interaction'].iloc[:, 2]
            self.inters_df.to_csv(self.output + self.method + "_Interactions.bed", index=None, sep="\t", header=False)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     usage='BackgroundModel.py -f file -m gothic -r /usr/local/bin/R -o output/bg_output/',
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
    #
    # bg_model = BackgroundModel(**args)
    bg_model = BackgroundModel(method="FitHiC", file="../bin/Data/output/hic_results/matrix/SRR442155/raw/20000/")
