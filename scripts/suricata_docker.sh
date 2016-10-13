#!/bin/bash

cd suricata_docker
sudo docker build --force-rm --tag xybu:suricata_afl --build-arg NPROC=`nproc` .
docker create -it -w /root --name suricata_afl xybu:suricata_afl --net host -v /home/xb:/host
