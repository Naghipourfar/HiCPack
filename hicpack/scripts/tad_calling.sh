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
	(-n) SAMPLE_NAME=$2; shift;;
	(-b) BIN_SIZE=$2; shift;;
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

mkdir -p "${TAD_DIR}"
OUTPUT_DIR="${TAD_DIR}/"

for i in ${!MAT_FILES[@]}
do
    BED_FILE="${BED_FILES[$i]}"
    MAT_FILE="${MAT_FILES[$i]}"
    python ${dir}/utils/sparseToDense.py ${MAT_FILE} -b ${BED_FILE} -o ${MAPC_OUTPUT}/matrix/${SAMPLE_NAME}/raw/${BIN_SIZE}/
done
MAT_DENSE_FILES=$(find -L $DATA_DIR -mindepth 1 -maxdepth 4 -name "*_dense.matrix")
for i in ${!MAT_DENSE_FILES[@]}
do
    MAT_DENSE_FILE="${MAT_DENSE_FILES[$i]}"
    python ${dir}/TADCalling.py -f ${MAT_DENSE_FILE} -o ${OUTPUT_DIR} -m ${TAD_ALGORITHM} -n ${SAMPLE_NAME} -b ${BIN_SIZE} -s ${dir}/
done