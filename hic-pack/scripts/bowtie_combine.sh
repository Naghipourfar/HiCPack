#!/bin/bash

## HiCPack
## Author(s): Mohsen Naghipourfar
## Contact: mn7697np@gmail.com or naghipourfar@ce.sharif.edu
## MIT Licence

##
## Combine two steps alignment files
##

dir=$(dirname $0)

while [ $# -gt 0 ]
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

CONF=$conf_file . $dir/hic.inc.sh

##
## Combine both Bowtie2 mapping
##
mapping_combine()
{
    local sample_dir="$1"
    local file="$2"
    local prefix=$(echo ${sample_dir}/$(basename $file) | sed -e 's/.bwt2glob.bam//')
    local tmp_prefix=$(basename $prefix)

    mkdir -p ${BOWTIE2_FINAL_OUTPUT_DIR}/${sample_dir}

    ## Merge local and global alignment
    if [[ -e ${BOWTIE2_GLOBAL_OUTPUT_DIR}/${prefix}.bwt2glob.bam && -e ${BOWTIE2_LOCAL_OUTPUT_DIR}/${prefix}.bwt2glob.unmap_bwt2loc.bam ]]; then

	cmd="${SAMTOOLS_PATH}/samtools merge -@ ${N_CPU} -n -f ${BOWTIE2_FINAL_OUTPUT_DIR}/${prefix}.bwt2merged.bam ${BOWTIE2_GLOBAL_OUTPUT_DIR}/${prefix}.bwt2glob.bam ${BOWTIE2_LOCAL_OUTPUT_DIR}/${prefix}.bwt2glob.unmap_bwt2loc.bam"
	exec_cmd $cmd 2>&1

        ## Sort merge file. In theory, should be perform by "merge -n", but do not work in some cases ... depending on read name ?
	cmd="${SAMTOOLS_PATH}/samtools sort -@ ${N_CPU} -n -T ${TMP_DIR}/$tmp_prefix -o ${BOWTIE2_FINAL_OUTPUT_DIR}/${prefix}.bwt2merged.sorted.bam ${BOWTIE2_FINAL_OUTPUT_DIR}/${prefix}.bwt2merged.bam"
        exec_cmd $cmd 2>&1

	cmd="mv ${BOWTIE2_FINAL_OUTPUT_DIR}/${prefix}.bwt2merged.sorted.bam ${BOWTIE2_FINAL_OUTPUT_DIR}/${prefix}.bwt2merged.bam"
        exec_cmd $cmd 2>&1

    elif [[ ${LIGATTION_SITE} == "" ]]; then

	cmd="ln -f -s ../../bwt2_global/${prefix}.bwt2glob.bam ${BOWTIE2_FINAL_OUTPUT_DIR}/${prefix}.bwt2merged.bam "
	exec_cmd $cmd 2>&1
    else
	die "Error - Mapping files not found"
    fi
}

## Combine local and global alignments
for r in $(get_sam_for_combine)
do
    R1=$r
    R2=$(echo $r | get_R2)
    sample_dir=$(get_sample_dir $r)

    ## Logs
    ldir=${LOGS_DIR}/${sample_dir}
    echo "Logs: $ldir/mapping_combine.log"

    mapping_combine $sample_dir $R1 >> ${ldir}/mapping_combine.log &
    mapping_combine $sample_dir $R2 >> ${ldir}/mapping_combine.log &

    wait
done
