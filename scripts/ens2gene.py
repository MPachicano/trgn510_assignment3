#!/usr/bin/python3

import sys
import re
import csv

ens2gene={}
## Build Dictionary
with open ("Homo_sapiens.GRCh37.75.gtf", 'r') as file:
    for line in file:
        matches=re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
        if matches:
            ens2gene[matches[0][0]]=matches[0][1]



with open('output.csv', 'w') as f:
    w = csv.writer(f, delimiter = ',')
    with open ('rna/expression_results.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[0] in ens2gene:
                row[0]=ens2gene[row[0]]
                print(row)
        w.writerows([x.split(',') for x in row])

