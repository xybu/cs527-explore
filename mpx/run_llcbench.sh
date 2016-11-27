#!/bin/bash

for dir in `find . -maxdepth 1 -name "llcbench *" -type d` ; do
  cd $dir
  pwd
  rm -rf results
  mkdir -p results
  make cache-run > results/cache-run.log
  make cache-script > results/cache-script.log
  make cache-graph > results/cache-graph.log
  make blas-run > results/blas-run.log
  make blas-script > results/blas-script.log
  make blas-graph > results/blas-graph.log
  cd ..
done
