#!/bin/bash

for dir in `find . -maxdepth 1 -name "llcbench*" -type d` ; do
  cd $dir
  pwd
  mkdir -p results
  make cache-run > results/cache-run.log
  cd ..
done
