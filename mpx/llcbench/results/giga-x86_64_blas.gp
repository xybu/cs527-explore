set logscale x 2
set grid
set term postscript
set title "Reference BLAS performance of giga-x86_64"
set xlabel "Problem Size"
set ylabel "Mflops/Sec"
plot "giga-x86_64_blas_vdaxpy.dat" title 'daxpy' with linespoints \
, "giga-x86_64_blas_vdgemv.dat" title 'dgemv' with linespoints \
, "giga-x86_64_blas_vdgemm.dat" title 'dgemm' with linespoints \
