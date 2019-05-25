#!/usr/bin/env bash

## HiCPack
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
	(-s) SAMPLE_NAME=$2; shift;;
	(-b) BIN_SIZE=$2; shift;;
	(--) shift; break;;
	(-*) echo "$0: error - unrecognized option $1" 1>&2; exit 1;;
	(*)  break;;
    esac
    shift
done

################### Read the config file ###################
##read_config $conf_file
CONF=${conf_file} . ${dir}/hic.inc.sh

DATA_DIR=${MAPC_OUTPUT}/matrix


MAT_FILES=$(find -L $DATA_DIR -mindepth 1 -maxdepth 4 -name "*.matrix")
BED_FILES=$(find -L $DATA_DIR -mindepth 1 -maxdepth 4 -name "*.bed")


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

for i in ${!MAT_FILES[@]}
do
    if [[ ${BG_MODEL} -eq "FitHiC" ]]; then
        BED_FILE="${BED_FILES[$i]}"
        MAT_FILE="${MAT_FILES[$i]}"
        python ${dir}/utils/HiCPack2FitHiC.py -i ${MAT_FILE} -b ${BED_FILE} -o ${MAPC_OUTPUT}/matrix/${SAMPLE_NAME}/raw/${BIN_SIZE}/ -r ${BIN_SIZE}
    fi
done

for MAT_FILE in ${MAT_FILES}
do
    python ${dir}/BackgroundModel.py -f ${MAT_FILE} -o ${OUTPUT_DIR} -m ${BG_MODEL} -n ${SAMPLE_NAME} -b ${BIN_SIZE} -s ${dir}/ -a 0
done