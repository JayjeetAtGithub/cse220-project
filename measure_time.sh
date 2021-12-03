#!/bin/bash
set -e

make clean_all

#synth
START=$(date +%s.%N)
make synth
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "synth: ${DIFF}" >> result_openroad.log

#floorplan
START=$(date +%s.%N)
make floorplan
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "floorplan: ${DIFF}" >> result_openroad.log

#place
START=$(date +%s.%N)
make place
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "place: ${DIFF}" >> result_openroad.log

#cts
START=$(date +%s.%N)
make cts
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "cts: ${DIFF}" >> result_openroad.log

#route
START=$(date +%s.%N)
make route
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "route: ${DIFF}" >> result_openroad.log

#finish
START=$(date +%s.%N)
make finish
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "finish: ${DIFF}" >> result_openroad.log


