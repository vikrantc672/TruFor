#!/usr/bin/env bash
INPUT_DIR=./Scanned_Photoshop_Morphs
OUTPUT_DIR=./output

mkdir -p ${OUTPUT_DIR}
# docker run --runtime=nvidia --gpus all -v $(realpath ${INPUT_DIR}):/data -v $(realpath ${OUTPUT_DIR}):/data_out trufor -gpu 0 -in data/ -out data_out/
docker run -v $(realpath ${INPUT_DIR}):/data -v $(realpath ${OUTPUT_DIR}):/data_out trufor -gpu -1 -in data/ -out data_out/
