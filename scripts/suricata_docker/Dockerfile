# Use latest ubuntu LTS
FROM ubuntu:latest

ARG SURICATA_VER=3.1.2
ARG AFL_VER=2.35b
ARG NPROC=4

# Install dependencies.
# https://redmine.openinfosecfoundation.org/projects/suricata/wiki/Ubuntu_Installation
RUN apt update
RUN apt upgrade -y
RUN apt install -y wget
RUN apt install -y libpcre3 libpcre3-dbg libpcre3-dev \
build-essential make autoconf automake libtool libpcap-dev libnet1-dev \
libyaml-0-2 libyaml-dev zlib1g zlib1g-dev libmagic-dev libcap-ng-dev \
libjansson-dev pkg-config libgeoip-dev libnetfilter-queue-dev \
libnetfilter-queue-dev libnetfilter-queue1 libnfnetlink-dev libnfnetlink0 \
clang llvm g++ libtool-bin bison m4

### Install AFL.
WORKDIR /tmp
RUN wget http://lcamtuf.coredump.cx/afl/releases/afl-$AFL_VER.tgz
RUN tar xvzf afl-$AFL_VER.tgz
WORKDIR afl-$AFL_VER
RUN make -j$NPROC
WORKDIR llvm_mode
RUN make -j$NPROC
WORKDIR /tmp/afl-$AFL_VER
RUN make install

### Install Suricata with AFL enabled.
WORKDIR /tmp
RUN wget http://www.openinfosecfoundation.org/download/suricata-$SURICATA_VER.tar.gz
RUN tar xvzf suricata-$SURICATA_VER.tar.gz
WORKDIR suricata-$SURICATA_VER
ARG ac_cv_func_realloc_0_nonnull=yes
ARG ac_cv_func_malloc_0_nonnull=yes
ARG CC="afl-clang-fast"
ARG CFLAGS="-fsanitize=address -fno-omit-frame-pointer"
RUN ./configure --enable-nfqueue --enable-unittests --enable-profiling --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-afl --disable-shared
RUN make -j$NPROC
RUN make install-full
RUN ldconfig
RUN mkdir -p /var/log/suricata
RUN chmod u+s /usr/bin/suricata

ENTRYPOINT ["/bin/bash"]
