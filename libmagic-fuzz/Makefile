AFL_CC=/usr/bin/clang-3.9
AFL_CXX=/usr/bin/clang++-3.9
LLVM_CONFIG=/usr/bin/llvm-config-3.9
CC=afl-clang-fast
CFLAGS=-fsanitize=address -fno-omit-frame-pointer -g -O0

export AFL_CC
export AFL_CXX
export LLVM_CONFIG

all: test_magic

test_magic: test_magic.c
	$(CC) $(CFLAGS) -o $@ $< -lmagic

clean:
	rm -rf test_magic *.o
