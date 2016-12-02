#!/usr/bin/python3

import itertools
import os
import sys
import statistics

import xlsxwriter


def to_num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def read_data_set(path):
    """
    Read the dataset whose format is {index value\n}+. If an index appears more
    than once, use the median of associated values. Also include the stdev
    of the sample.
    """
    print(path)
    ds = dict()
    try:
        with open(path, 'r') as f:
            for line in f:
                index, value = [to_num(v) for v in line.strip().split(maxsplit=1)]
                if index in ds:
                    ds[index].append(value)
                else:
                    ds[index] = [value]
    except OSError as e:
        print('Error: ' + str(e))
    d = dict()
    for k, v in ds.items():
        med = statistics.median(v)
        stdev = statistics.stdev(v) if len(v) > 1 else 0
        d[k] = (med, stdev)
    return d


datasets = ['cache_handread', 'cache_handwrite', 'cache_handrmw',
            'cache_memcpy', 'cache_memset',
            'cache_read', 'cache_rmw', 'cache_write',
            'blas_vdaxpy', 'blas_vdgemm', 'blas_vdgemv']

tags = ['base', 'asan', 'mpx']

workbook = xlsxwriter.Workbook('llcbench.xlsx', {'strings_to_numbers': True})

for dataset in datasets:
    ds = dict()
    sheet = workbook.add_worksheet(dataset)
    sheet.write(0, 0, 'Size')
    sheet.set_column('{0}:{0}'.format(chr(ord('A') + 0)), 10)
    for i, tag in enumerate(tags):
        sheet.write(0, i + 1, tag + '_med')
        sheet.write(0, i + 1 + len(tags), tag + '_stdev')
        ds[tag] = read_data_set('llcbench-' + tag + '/results/giga-x86_64_' + dataset + '.dat')
    for pair in itertools.permutations(ds.keys(), r=2):
        pa, pb = pair
        if sorted(ds[pa].keys()) != sorted(ds[pb].keys()):
            print('Error: in dataset %s indices of tags %s and %s are not equal!' % (dataset, pa, pb))
            sys.exit(1)
    indices = sorted(ds[tags[0]].keys())
    for rowid, index in enumerate(indices):
        sheet.write(rowid + 1, 0, index)
        for cowid, tag in enumerate(tags):
            sheet.write(rowid + 1, cowid + 1, ds[tag][index][0])
            sheet.write(rowid + 1, cowid + 1 + len(tags), ds[tag][index][1])

workbook.close()
