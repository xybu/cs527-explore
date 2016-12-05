#!/bin/bash

# for tag in base asan mpx ; do
for tag in mpx ; do
    mkdir -p result
    for test_suite in fp all_cpp int all_c ; do
        for size in test train ref ; do
            echo "[`date`] Execute ./run_spec_$tag.sh $tag $size $test_suite..."
            CC=gcc CXX=g++ OPT_LEVEL=-O3 NUM_RUNS=1 ./run_spec_$tag.sh $tag $size $test_suite
        done
    done
    mv result result_$tag
done
