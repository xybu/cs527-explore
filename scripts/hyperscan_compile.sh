$!/bin/bash

CC=afl-clang-fast CXX=afl-clang-fast++ AFL_CC=clang-3.9 AFL_CXX=clang++-3.9 cmake -DCMAKE_CXX_COMPILER_ID=clang -DCMAKE_C_COMPILER_ID=clang -DCMAKE_C_COMPILER=afl-clang-fast -DCMAKE_CXX_COMPILER=afl-clang-fast++ -DCMAKE_C_FLAGS="-g -O0 -fsanitize=address -fno-omit-frame-pointer" -DCMAKE_CXX_FLAGS="-g -O0 -fsanitize=address -fno-omit-frame-pointer" ..
