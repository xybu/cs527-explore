
For libmagic (https://github.com/file/file), if you compile with ASAN

```
CC=/usr/local/bin/afl-clang-fast CFLAGS="-fsanitize=address -g -O0" ./configure --disable-silent-rules --disable-shared
make -j4
make -C tests check
```

ASAN will report memory leak when the program runs:

```
root@ffd44e7d4dd4:~/file_asan/tests# ./test 
ERROR loading with NULL file: could not find any valid magic files!

=================================================================
==3217==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 232 byte(s) in 1 object(s) allocated from:
    #0 0x4b9890  (/root/file_asan/tests/test+0x4b9890)
    #1 0x4ee344  (/root/file_asan/tests/test+0x4ee344)

Indirect leak of 160 byte(s) in 1 object(s) allocated from:
    #0 0x4b9708  (/root/file_asan/tests/test+0x4b9708)
    #1 0x4ee3ef  (/root/file_asan/tests/test+0x4ee3ef)

Indirect leak of 38 byte(s) in 1 object(s) allocated from:
    #0 0x4b9708  (/root/file_asan/tests/test+0x4b9708)
    #1 0x7f4030a26717  (/lib/x86_64-linux-gnu/libc.so.6+0x76717)

SUMMARY: AddressSanitizer: 430 byte(s) leaked in 3 allocation(s).
```

Compile with clang without ASAN:

```
CC=/usr/local/bin/afl-clang-fast CFLAGS="-g -O0" ./configure --disable-silent-rules --disable-shared
make -j4
make -C tests check
```

and it can be verified with valgrind:

```
$ valgrind --leak-check=full -v ./test CVE-2014-1943.testfile
==26635== Memcheck, a memory error detector
==26635== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==26635== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==26635== Command: ./test CVE-2014-1943.testfile
==26635== 
--26635-- Valgrind options:
--26635--    --leak-check=full
--26635--    -v
--26635-- Contents of /proc/version:
--26635--   Linux version 4.8.0-21-generic (buildd@lcy01-36) (gcc version 6.2.0 20160927 (Ubuntu 6.2.0-5ubuntu11) ) #23-Ubuntu SMP Tue Oct 4 18:27:2
5 UTC 2016
--26635-- 
--26635-- Arch and hwcaps: AMD64, LittleEndian, amd64-cx16-lzcnt-rdtscp-sse3-avx-avx2-bmi
--26635-- Page sizes: currently 4096, max supported 4096
--26635-- Valgrind library directory: /usr/lib/valgrind
--26635-- Reading syms from /root/file_asan/tests/test
--26635-- Reading syms from /lib/x86_64-linux-gnu/ld-2.23.so
--26635--   Considering /lib/x86_64-linux-gnu/ld-2.23.so ..
--26635--   .. CRC mismatch (computed d3da0723 wanted a1c29704)
--26635--   Considering /usr/lib/debug/lib/x86_64-linux-gnu/ld-2.23.so ..
--26635--   .. CRC is valid
--26635-- Reading syms from /usr/lib/valgrind/memcheck-amd64-linux
--26635--   Considering /usr/lib/valgrind/memcheck-amd64-linux ..
--26635--   .. CRC mismatch (computed 5529a2c7 wanted 5bd23904)
--26635--    object doesn't have a symbol table
--26635--    object doesn't have a dynamic symbol table
--26635-- Scheduler: using generic scheduler lock implementation.
--26635-- Reading suppressions file: /usr/lib/valgrind/default.supp
==26635== embedded gdbserver: reading from /tmp/vgdb-pipe-from-vgdb-to-26635-by-???-on-ffd44e7d4dd4
==26635== embedded gdbserver: writing to   /tmp/vgdb-pipe-to-vgdb-from-26635-by-???-on-ffd44e7d4dd4
==26635== embedded gdbserver: shared mem   /tmp/vgdb-pipe-shared-mem-vgdb-26635-by-???-on-ffd44e7d4dd4
==26635== 
==26635== TO CONTROL THIS PROCESS USING vgdb (which you probably
==26635== don't want to do, unless you know exactly what you're doing,
==26635== or are doing some strange experiment):
==26635==   /usr/lib/valgrind/../../bin/vgdb --pid=26635 ...command...
==26635== 
==26635== TO DEBUG THIS PROCESS USING GDB: start GDB like this
==26635==   /path/to/gdb ./test
==26635== and then give GDB the following command
==26635==   target remote | /usr/lib/valgrind/../../bin/vgdb --pid=26635
==26635== --pid is optional if only one valgrind process is running
==26635== 
--26635-- REDIR: 0x401cdc0 (ld-linux-x86-64.so.2:strlen) redirected to 0x3809e181 (???)
--26635-- Reading syms from /usr/lib/valgrind/vgpreload_core-amd64-linux.so
--26635--   Considering /usr/lib/valgrind/vgpreload_core-amd64-linux.so ..
--26635--   .. CRC mismatch (computed a30c8eaa wanted 7ae2fed4)
--26635--    object doesn't have a symbol table
--26635-- Reading syms from /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so
--26635--   Considering /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so ..
--26635--   .. CRC mismatch (computed 402c2ab5 wanted 745f25ae)
--26635--    object doesn't have a symbol table
==26635== WARNING: new redirection conflicts with existing -- ignoring it
--26635--     old: 0x0401cdc0 (strlen              ) R-> (0000.0) 0x3809e181 ???
--26635--     new: 0x0401cdc0 (strlen              ) R-> (2007.0) 0x04c31020 strlen
--26635-- REDIR: 0x401b710 (ld-linux-x86-64.so.2:index) redirected to 0x4c30bc0 (index)
--26635-- REDIR: 0x401b930 (ld-linux-x86-64.so.2:strcmp) redirected to 0x4c320d0 (strcmp)
--26635-- REDIR: 0x401db20 (ld-linux-x86-64.so.2:mempcpy) redirected to 0x4c35270 (mempcpy)
--26635-- Reading syms from /lib/x86_64-linux-gnu/libz.so.1.2.8
--26635--    object doesn't have a symbol table
--26635-- Reading syms from /lib/x86_64-linux-gnu/libc-2.23.so
--26635--   Considering /lib/x86_64-linux-gnu/libc-2.23.so ..
--26635--   .. CRC mismatch (computed 2adb2e50 wanted 9b73f606)
--26635--   Considering /usr/lib/debug/lib/x86_64-linux-gnu/libc-2.23.so ..
--26635--   .. CRC is valid
--26635-- REDIR: 0x50e2fd0 (libc.so.6:strcasecmp) redirected to 0x4a286f0 (_vgnU_ifunc_wrapper)
--26635-- REDIR: 0x50de850 (libc.so.6:strcspn) redirected to 0x4a286f0 (_vgnU_ifunc_wrapper)
--26635-- REDIR: 0x50e52c0 (libc.so.6:strncasecmp) redirected to 0x4a286f0 (_vgnU_ifunc_wrapper)
--26635-- REDIR: 0x50e0cc0 (libc.so.6:strpbrk) redirected to 0x4a286f0 (_vgnU_ifunc_wrapper)
--26635-- REDIR: 0x50e1050 (libc.so.6:strspn) redirected to 0x4a286f0 (_vgnU_ifunc_wrapper)
--26635-- REDIR: 0x50e271b (libc.so.6:memcpy@GLIBC_2.2.5) redirected to 0x4a286f0 (_vgnU_ifunc_wrapper)
--26635-- REDIR: 0x50e09d0 (libc.so.6:rindex) redirected to 0x4c308a0 (rindex)
--26635-- REDIR: 0x50decf0 (libc.so.6:strlen) redirected to 0x4c30f60 (strlen)
--26635-- REDIR: 0x50d8290 (libc.so.6:calloc) redirected to 0x4c2faa0 (calloc)
--26635-- REDIR: 0x50d7550 (libc.so.6:malloc) redirected to 0x4c2db20 (malloc)
--26635-- REDIR: 0x50df140 (libc.so.6:__GI_strncmp) redirected to 0x4c31710 (__GI_strncmp)
--26635-- REDIR: 0x50e9d30 (libc.so.6:strchrnul) redirected to 0x4c34da0 (strchrnul)
--26635-- REDIR: 0x50e7a40 (libc.so.6:__GI_memcpy) redirected to 0x4c32b00 (__GI_memcpy)
--26635-- REDIR: 0x50d7a70 (libc.so.6:free) redirected to 0x4c2ed80 (free)
--26635-- REDIR: 0x50dd050 (libc.so.6:index) redirected to 0x4a286f0 (_vgnU_ifunc_wrapper)
--26635-- REDIR: 0x50dd080 (libc.so.6:__GI_strchr) redirected to 0x4c30a00 (__GI_strchr)
--26635-- REDIR: 0x50dee90 (libc.so.6:strnlen) redirected to 0x4c30ee0 (strnlen)
--26635-- REDIR: 0x50e2980 (libc.so.6:__GI_mempcpy) redirected to 0x4c34fa0 (__GI_mempcpy)
--26635-- REDIR: 0x50e1c00 (libc.so.6:strstr) redirected to 0x4a286f0 (_vgnU_ifunc_wrapper)
--26635-- REDIR: 0x50fd640 (libc.so.6:__strstr_sse2_unaligned) redirected to 0x4c35460 (strstr)
ERROR loading with NULL file: could not find any valid magic files!
==26635== 
==26635== HEAP SUMMARY:
==26635==     in use at exit: 430 bytes in 3 blocks
==26635==   total heap usage: 16 allocs, 13 frees, 1,648 bytes allocated
==26635== 
==26635== Searching for pointers to 3 not-freed blocks
==26635== Checked 137,952 bytes
==26635== 
==26635== 430 (232 direct, 198 indirect) bytes in 1 blocks are definitely lost in loss record 3 of 3
==26635==    at 0x4C2FB55: calloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==26635==    by 0x404C55: file_ms_alloc (apprentice.c:512)
==26635==    by 0x4024FE: main (test.c:77)
==26635== 
==26635== LEAK SUMMARY:
==26635==    definitely lost: 232 bytes in 1 blocks
==26635==    indirectly lost: 198 bytes in 2 blocks
==26635==      possibly lost: 0 bytes in 0 blocks
==26635==    still reachable: 0 bytes in 0 blocks
==26635==         suppressed: 0 bytes in 0 blocks
==26635== 
==26635== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
==26635== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

But if you compile the program with GCC

```
CC=/usr/local/bin/afl-gcc ASM=afl-gcc CFLAGS="-g -O0" ./configure --disable-silent-rules --disable-shared
make -j4
make -C tests check
```

and run the same program with valgrind, it says no memory leak is possible.
