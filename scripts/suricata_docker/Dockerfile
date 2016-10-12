# Use latest ubuntu LTS
FROM ubuntu:latest

ARG SURICATA_VER=3.1.2
ARG AFL_VER=2.35b
ARG NPROC=4

ENV ac_cv_func_realloc_0_nonnull=yes
ENV ac_cv_func_malloc_0_nonnull=yes

# Install dependencies.
# https://redmine.openinfosecfoundation.org/projects/suricata/wiki/Ubuntu_Installation
RUN apt update
RUN apt upgrade -y
RUN apt install -y wget
RUN apt install -y libpcre3 libpcre3-dbg libpcre3-dev \
build-essential make autoconf automake libtool libpcap-dev libnet1-dev \
libyaml-0-2 libyaml-dev zlib1g zlib1g-dev libcap-ng-dev \
libjansson-dev pkg-config libgeoip-dev libnetfilter-queue-dev \
libnetfilter-queue-dev libnetfilter-queue1 libnfnetlink-dev libnfnetlink0 \
clang llvm g++ libtool-bin bison m4 git mercurial tmux

### Install AFL.
WORKDIR /root
RUN wget http://lcamtuf.coredump.cx/afl/releases/afl-$AFL_VER.tgz
RUN tar xvzf afl-$AFL_VER.tgz
WORKDIR afl-$AFL_VER
RUN make -j$NPROC
WORKDIR llvm_mode
RUN make -j$NPROC
WORKDIR /tmp/afl-$AFL_VER
RUN make install

### Install libmagic from source.
WORKDIR /root
RUN git clone git@github.com:xybu/file.git
WORKDIR file
ARG CC="afl-clang-fast"
ARG ASM="afl-clang-fast"
ARG CFLAGS="-g -O0 -fsanitize=address"
ARG CPPFLAGS=CFLAGS
RUN autoreconf -f -i
RUN ./configure --disable-silent-rules --enable-static
RUN make -j$NPROC
RUN make -C tests check
RUN make install

### Install Suricata with AFL enabled.
WORKDIR /root
RUN wget http://www.openinfosecfoundation.org/download/suricata-$SURICATA_VER.tar.gz
RUN tar xvzf suricata-$SURICATA_VER.tar.gz
WORKDIR suricata-$SURICATA_VER
ARG CC="afl-clang-fast"
ARG CFLAGS="-fsanitize=address -fno-omit-frame-pointer -g -O0"
ARG CPPFLAGS=CFLAGS
RUN ./configure --enable-nfqueue --enable-unittests --enable-profiling --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-afl --disable-shared  --with-libmagic-includes=/root/file/src --with-libmagic-libraries=/root/file/src/.libs
RUN make -j$NPROC
RUN make install-full
RUN ldconfig
RUN mkdir -p /var/log/suricata
RUN chmod u+s /usr/bin/suricata

ENTRYPOINT ["/bin/bash"]
