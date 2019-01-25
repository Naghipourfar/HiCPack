#!/usr/bin/env bash

## HiC-Pack
## Author(s): Mohsen Naghipourfar
## Contact: mn7697np@gmail.com or naghipourfar@ce.sharif.edu
## This software is distributed without any guarantee under the terms of the GNU General
## MIT License

dir=$(dirname $0)


usage(){
    echo "usage : ./bg_model.sh -c CONFIG"
    echo "Use option -h|--help for more information"
}

################### Initialization ###################

while [[ $# -gt 0 ]]
do
    case "$1" in
	(-c) conf_file=$2; shift;;
	(-h) usage;;
	(--) shift; break;;
	(-*) echo "$0: error - unrecognized option $1" 1>&2; exit 1;;
	(*)  break;;
    esac
    shift
done

################### Read the config file ###################
##read_config $conf_file
CONF=${conf_file} . ${dir}/hic.inc.sh

DATA_DIR=${MAPC_OUTPUT}/matrix/


BED_FILES=$(find -L $DATA_DIR -mindepth 1 -maxdepth 4 -name "*.matrix")

## Apply Background model
# echo 'Please choose background model:'
# echo '1. GOTHiC'
# echo '2. MaxHiC'
# echo '3. FitHiC'
# echo '4. Chicago'

#read input

#if [[ ${input} -gt 6 || ${input} -lt 1 ]]
#then
#    echo "Wrong choice!"
#    exit
#fi

mkdir -p ${BG_DIR}
OUTPUT_DIR=${BG_DIR}/

for BED_FILE in ${BED_FILES}
do
    python ${dir}/TADCalling.py -f ${BED_FILE} -o ${OUTPUT_DIR} -m ${TAD_ALGORITHM}
done