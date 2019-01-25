#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:22:59 2019

@author: jtruch
"""

import argparse
import pysam

parser=argparse.ArgumentParser(description = "Convert bam to bed")

parser.add_argument('--bamfile', help = 'bam file input')
parser.add_argument('--bedfile', help = 'bed file output', default = "default.bed")

args=parser.parse_args()

if args.bedfile == "default.bed":
    args.bedfile = str(args.bamfile.replace(".bam",".bed"))

if str(args.bamfile).rsplit(".",1)[1] != "bam":
    raise Exception("Are you sure this is a BAM file??")
else:
    pass
# input = open(args.bamfile, "r")
output = open(args.bedfile , "w")

# open the file as sam from bam "rb"= read binary 
# OOP using fetch to go through the object created by pysam.AlignmentFile 
count_unmapped = 0
count_none_stop = 0

samfile = pysam.AlignmentFile(args.bamfile, "rb")
for read in samfile.fetch():
    if read.is_unmapped == True:
        count_unmapped += 1
    else:
    #     print(read)
        chromosome = read.reference_name
    #     print(chromosome)
        start = read.reference_start
        stop = read.reference_end
        name = read.query_name
    #     print(name)
        if read.is_reverse == True:
            strand = "-"
        else:
            strand = "+"
    
        bed_line = '{}\t{}\t{}\t{}\t.\t{}\n'.format(chromosome,start,stop,name,strand)
        output.write(bed_line)
#        if stop == None:
#            count_none_stop += 0
print(bed_line)
print(count_unmapped)
print(count_none_stop)
     
#for read in samfile.head(1):
#     print(read)

samfile.close()
output.close()
