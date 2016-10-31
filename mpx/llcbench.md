LLCbench
========

[LLCbench (Low-Level Characterization Benchmarks)](http://icl.cs.utk.edu/llcbench/index.htm)

## Modifications

1. Modified `blasbench/bb.c` to get rid of linking issue with gfortran.

2. Modified `conf/sys.linux-mpich` to use `gcc` rather than `g77` and to link with `libm`.

## Cachebench

Benchmark memory subsystem.

```
Usage: cachebench -rwbtsp [-x #] [-m #] [-d #] [-e #]
         -r Read benchmark
         -w Write benchmark
         -b Read/Modify/Write benchmark
         -t Use hand tuned versions of the above
         -s memset() benchmark
         -p memcpy() benchmark
         -x Number of measurements between powers of 2.
         -m Specify the log2(available physical memory)
         -d Number of seconds per iteration
         -e Repeat count per cache size

Datatype used is double, 8 bytes.
Defaults if  tty: -rwbsp -x1 -m24 -d5 -e2
Defaults if file: -b   -x1 -m24 -d5 -e1
```

## MPIbench

Benchmark critical MPI routines.

```
Usage: (MPI implementation dependent portion) mpi_bench -blracyz [-i #] [-x #] [-m #] [-d #] [-e #]
         -b Do bandwidth benchmark
         -d Do bidirectional bandwidth benchmark
         -l Do latency benchmark
         -r Do roundtrip benchmark
         -a Do all-to-all benchmark
         -c Do broadcast benchmark
         -y Do reduce benchmark
         -z Do allreduce benchmark
         -i Specify the iterations over which to average. 
         -x Specify the number of measurements between powers of 2.  
         -m Specify the log base 2 of the maximum message size.
         -e Specify the repeat count per message size. 
         -f Flush the cache between message sizes.
         -F Flush the cache between repeats.
         -X Flush the cache between iterations.
         -M num[bBkKmM],num[bBkKmM]...Fix message sizes in B (default), kB or MB (base 2) to use. 

Defaults in make.def: -bdlracyz -i100 -x2 -m16 -e1    (with 16 MPI processes) 
```

## BLASbench

Benchmark Fortran77 BLAS library.

```
Usage: blasbench [-vatcs -x # -m # -e # -i #]
         -v AXPY dot product benchmark
         -a GEMV matrix-vector multiply benchmark
         -t GEMM matrix-matrix multiply benchmark
         -s Use single precision floating point data
         -c Use constant number of iterations
         -o Report Mflops/sec instead of MB/sec
         -e Repeat count per problem size
         -l Hold LDA and loop over sizes of square submatrices
         -i Maximum iteration count
         -x Number of measurements between powers of 2.
         -m Specify the log2(maximum problem size) in bytes
         -d Report/use dimension statistics instead of bytes

Default datatype   : double, 8 bytes
Default datatype   : float, 4 bytes
Defaults if to tty : -vat -x1 -m24 -e2 -i100000
Defaults if to file: -t   -x1 -m24 -e1 -i100000
```
