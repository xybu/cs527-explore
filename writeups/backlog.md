Suricata's dependency library libmagic has memory leak issues, preventing the program to run with ASAN.

```
root@ffd44e7d4dd4:~# suricata -r sample_traces/dns/zlip-1.pcap 
11/10/2016 -- 05:00:43 - <Notice> - This is Suricata version 3.1.2 RELEASE
11/10/2016 -- 05:00:49 - <Notice> - AFL mode starting
11/10/2016 -- 05:00:49 - <Notice> - Pcap-file module read 1 packets, 77 bytes
11/10/2016 -- 05:00:49 - <Error> - [ERRCODE: SC_ERR_THREAD_INIT(49)] - thread "RX#01" closed on initialization.
11/10/2016 -- 05:00:49 - <Error> - [ERRCODE: SC_ERR_INITIALIZATION(45)] - Engine initialization failed, aborting...

=================================================================
==29878==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 48 byte(s) in 1 object(s) allocated from:
    #0 0x4bccc0  (/usr/bin/suricata+0x4bccc0)
    #1 0x7fceace86d3d  (/usr/lib/x86_64-linux-gnu/libmagic.so.1+0x9d3d)

SUMMARY: AddressSanitizer: 48 byte(s) leaked in 1 allocation(s).
root@ffd44e7d4dd4:~# suricata -i eth0
11/10/2016 -- 05:01:21 - <Notice> - This is Suricata version 3.1.2 RELEASE
11/10/2016 -- 05:01:28 - <Warning> - [ERRCODE: SC_ERR_NIC_OFFLOADING(284)] - NIC offloading on eth0: SG: SET,  GRO: SET, LRO: unset, TSO: SET, GSO: SET. Run: ethtool -K eth0 sg off gro off lro off tso off gso off
11/10/2016 -- 05:01:28 - <Warning> - [ERRCODE: SC_ERR_AFP_CREATE(190)] - Using AF_PACKET with offloading activated leads to capture problems
11/10/2016 -- 05:01:28 - <Notice> - AFL mode starting
11/10/2016 -- 05:01:28 - <Notice> - AFL mode starting
11/10/2016 -- 05:01:28 - <Notice> - AFL mode starting
11/10/2016 -- 05:01:28 - <Notice> - AFL mode starting
11/10/2016 -- 05:01:28 - <Notice> - AFL mode starting
11/10/2016 -- 05:01:28 - <Notice> - AFL mode starting
11/10/2016 -- 05:01:28 - <Notice> - AFL mode starting
11/10/2016 -- 05:01:28 - <Notice> - AFL mode starting
11/10/2016 -- 05:01:28 - <Notice> - all 8 packet processing threads, 0 management threads initialized, engine started.
^C11/10/2016 -- 05:01:40 - <Notice> - Signal Received.  Stopping engine.
11/10/2016 -- 05:01:40 - <Notice> - Stats for 'eth0':  pkts: 0, drop: 0 (-nan%), invalid chksum: 0

=================================================================
==32378==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 48 byte(s) in 1 object(s) allocated from:
    #0 0x4bccc0  (/usr/bin/suricata+0x4bccc0)
    #1 0x7f92ede7cd3d  (/usr/lib/x86_64-linux-gnu/libmagic.so.1+0x9d3d)

Indirect leak of 2 byte(s) in 2 object(s) allocated from:
    #0 0x4bcb38  (/usr/bin/suricata+0x4bcb38)
    #1 0x7f92ede7d24c  (/usr/lib/x86_64-linux-gnu/libmagic.so.1+0xa24c)

SUMMARY: AddressSanitizer: 50 byte(s) leaked in 3 allocation(s).
```
