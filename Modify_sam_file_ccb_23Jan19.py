#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:44:38 2019

@author: jtruch
"""
# command line parameters (SAM to bed)
# open file    /t1-data/user/jtruch/CCB_training_2019/odbs/week2/ERR1755082.test.sam
# iterate over each line and ignore header line
# slip the line
# assign each to a variable
# create missing variable
# reorder the variable and print out the new file
# bed file order : chr, stat, stop, name, score, strand
#
""""
# use sys pakage to run the script on the command line using arguments (tested using run -> configuration per file ->command options)
import sys

input = open(sys.argv[1], "r")
output = open(sys.argv[2] , "w")
"""
# use parse instead of sys to give more option on the commande line

import argparse

parser=argparse.ArgumentParser(description = "Convert sam to bed")

parser.add_argument('--samfile', help = 'sam file input')
args=parser.parse_args()
parser.add_argument('--bedfile', help = 'bed file output', default=str(args.samfile.replace(".sam",".bed")))

args=parser.parse_args()


if str(args.samfile).rsplit(".",1)[1] != "sam":
    raise Exception("Are you sure this is a SAM file??")
else:
    pass
input = open(args.samfile, "r")
output = open(args.bedfile , "w")


#input = open("/t1-data/user/jtruch/CCB_training_2019/odbs/week2/ERR1755082.test.sam", "r")
#output = open("bed_file" , "w")

for line in input:
    if line.startswith('@'):
        continue
    elif "XS:A:" not in line:
        continue
    else:
        #print(line.split('\t')[0])
        splitline = (line.split('\t'))
         # ignore the unmapped reads => they have * in col 2
        if splitline[2] == '*':
            continue
        else:
            chr = splitline[2]
            seq_name = splitline[0]
            #print(seq_name)
            #need to specify that the start in SAM file is a number
            SAM_file_start = (int(splitline[3])-1)
            #find the length of the sequence to determine the stop
            SAM_file_length = len(splitline[9])
            strand = ""
            if 'XS:A:-' in line:
                strand = "-"
 #SAM are in 1 based whereas bed are in 0 base so we remove 1 to each start value
 # And it is on the - strand so stop = start and start = stop
                stop = SAM_file_start
                start = stop - SAM_file_length

            elif 'XS:A:+' in line:            
                strand = "+"
#SAM are in 1 based whereas bed are in 0 base so we remove 1 to each start value 
                start = SAM_file_start
                stop = start + SAM_file_length
#print line by line using the string formating locals()            
            Bed_line = '%(chr)s\t%(start)s\t%(stop)s\t%(seq_name)s\t.\t%(strand)s\n' % locals()
             # Bed_line = chr, "\t", start, "\t" , stop, "\t" , seq_name , "\t" , "." , "\t" , strand, "\t" 
             #print(Bed_line)
            output.write(Bed_line)

output.close()
input.close()



                
                
                
                
                
                
                
                
            