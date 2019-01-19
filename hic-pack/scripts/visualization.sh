#!/usr/bin/env bash

## HiC-Pack
## Author(s): Mohsen Naghipourfar
## Contact: mn7697np@gmail.com or naghipourfar@ce.sharif.edu
## This software is distributed without any guarantee under the terms of the GNU General
## MIT License

dir=$(dirname $0)


usage(){
    echo "usage : ./visualization.sh -c CONFIG -s chr6 -n YOUR_SAMPLE_NAME -r 100000"
    echo "Use option -h|--help for more information"
}

################### Initialization ###################

while [[ $# -gt 0 ]]
do
    case "$1" in
	(-c) conf_file=$2; shift;;
	(-h) usage;;
	(-s) CHR=$2; shift;;
	(-n) SAMPLE_NAME=$2; shift;;
	(-r) RESOLUTION=$2; shift;;
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

OUTPUT_DIR=${VIS_DIR}/${SAMPLE_NAME}/
INPUT_DIR=${MAPC_OUTPUT}/matrix/

mkdir -p ${OUTPUT_DIR}

MAT_FILE=$(find -L ${DATA_DIR} -mindepth 1 -maxdepth 4 -name "${SAMPLE_NAME}_${RESOLUTION}.matrix")
BED_FILE=$(find -L ${DATA_DIR} -mindepth 1 -maxdepth 4 -name "${SAMPLE_NAME}_${RESOLUTION}_abs.bed")

python ${dir}/Visualization/HiCPlotter.py -f ${INPUT_DIR}/${SAMPLE_NAME}/raw/${RESOLUTION}/${SAMPLE_NAME}_${RESOLUTION}.matrix -n ${SAMPLE_NAME} -chr ${CHR} -o ${OUTPUT_DIR}/${SAMPLE_NAME} -tri 1 -ext pdf -bed ${INPUT_DIR}/${SAMPLE_NAME}/raw/${RESOLUTION}/${SAMPLE_NAME}_${RESOLUTION}_abs.bed
