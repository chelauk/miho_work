#!/usr/env/python
import os
import re

"""
script to create miho's preferred file format
"""

# open list of files

file_list = open('/Users/chelajames/chela_james_projects/Miho/new_project/annotated_file.list',  'r')


for line in file_list :
    line=line.rstrip()

    sample_file=open(line, 'r')
    sample_name = os.path.basename(line)
    for sample_line in sample_file:
         
        sample_line=sample_line.rstrip()
        if re.match('#', sample_line):
            continue
        #print sample_line
        
        
        sample_line=re.split('\t|;',sample_line)
        pos = re.split(':', sample_line[1])
        chr = pos[0]
        nucleotide = pos[1]
        sample_line=sample_line[2:]
        if re.match('Transcript', sample_line[3]) and ( re.match('synonymous_variant', sample_line[4]) \
                                                        or re.match('non_coding_exon_variant', sample_line[4]) \
                                                        or re.match('missense_variant', sample_line[4]) \
                                                        or re.match('3_prime_UTR_variant', sample_line[4])):
            for item in sample_line:
                if re.match('SYMBOL', item):
                    gene = item.translate(None,"SYMBOL=")
                elif re.match('SIFT', item):
                    sift = item.translate(None,"SIFT=")
                elif re.match('GMAF', item):
                    gmaf = item.translate(None, "GMAF=[A-Z]:")
                #    sift = item
                    print sample_name + "\t" + chr + "\t" + nucleotide + "\t" + sample_line[0]  + "\t" + sample_line[3]  + "\t" + sample_line[4]  + "\t" + sample_line[5 ] + "\t" + \
                    sample_line[6] + "\t" + sample_line[7] + "\t" + sample_line[8] + "\t" +  gene + "\t" + sift  + "\t" + gmaf

            #else:
            #    print sample_line[13]
            #    print sample_line

                
        #if len(sample_line) == 21:
        # splat operator opens list
        #    print sample_line
            
        #variant = Variant(*sample_line)
