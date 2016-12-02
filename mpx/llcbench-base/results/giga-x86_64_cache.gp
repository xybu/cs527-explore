set logscale x 2
set grid
set term postscript
set title "Memory Hierarchy Performance of giga-x86_64"
set xlabel "Vector Length"
set ylabel "MB/Sec"
plot "giga-x86_64_cache_read.dat" title 'read' with linespoints \
, "giga-x86_64_cache_write.dat" title 'write' with linespoints \
, "giga-x86_64_cache_rmw.dat" title 'rmw' with linespoints \
, "giga-x86_64_cache_handread.dat" title 'handread' with linespoints \
, "giga-x86_64_cache_handwrite.dat" title 'handwrite' with linespoints \
, "giga-x86_64_cache_handrmw.dat" title 'handrmw' with linespoints \
, "giga-x86_64_cache_memset.dat" title 'memset' with linespoints \
, "giga-x86_64_cache_memcpy.dat" title 'memcpy' with linespoints \
