#!/usr/env/python
import os
import re
import sys

"""
script to create miho's preferred file format
"""
# open list of files

file = open(sys.argv[0],  'r')
#file = open('/Users/chelajames/chela_james_projects/Miho/start_again/test_26_10')

print "Sample ID\tChr\tStart\tEnd\tGene name\tRef\tAlt\tFrequency in Sample\tGenotype\tMutation type\tRead depth\t1K genome MAF\t SNP ID\t\
ExAC_EAS_AF\tExAC_AMR_AF\tExAC_NFE_AF\tExAC_AFR_AF\tExAC_AF\tExAC_FIN_AF\tExAC_OTH_AF\tExAC_SAS_AF\tClinically significant variant\tSIFT\tPolyPhen\tQuality score"

for sample_line in file:
    sample_line = sample_line.rstrip()
    if re.match('#', sample_line):
        info_line = re.split('\t',sample_line)
        samples = info_line[9:]
        continue
    sample_line=sample_line.rstrip()
    variant_details = re.split('\t', sample_line)
    chr=variant_details[0]
    if ( len(variant_details[3]) == 1 ) and ( len(variant_details[4]) == 1 ):
        snv_start = variant_details[1]
        snv_end = variant_details[1]
    else:
        start = "something_else"
    ref = variant_details[3]
    alt = variant_details[4]
    info = variant_details[7]
    
    info_split = re.split(';', info)
    ns = info_split[0]
    an = info_split[1]
    ac = info_split[2]
    consequence = info_split[3]
    consequences = re.split('\|', consequence)
    consequence_list = ['Allele','Gene','Feature','Feature_type','Consequence','cDNA_position','CDS_position','Protein_position',\
                        'Amino_acids','Codons','Existing_variation','AA_MAF','EA_MAF','EXON','INTRON','MOTIF_NAME','MOTIF_POS',\
                        'HIGH_INF_POS','MOTIF_SCORE_CHANGE','DISTANCE','STRAND','CLIN_SIG','CANONICAL','SYMBOL','SYMBOL_SOURCE',\
                        'SIFT','PolyPhen','GMAF','BIOTYPE','ENSP','DOMAINS','CCDS','HGVSc','HGVSp','AFR_MAF','AMR_MAF','ASN_MAF',\
                        'EUR_MAF','PUBMED','ExAC_EAS_AF','ExAC_AMR_AF','ExAC_NFE_AF','ExAC_AFR_AF','ExAC_AF','ExAC_FIN_AF','ExAC_OTH_AF','ExAC_SAS_AF']
    consequence_dict =  dict(zip(consequence_list, consequences))
    gt_details=variant_details[9:]
 
    count_gts = 0
    for count_genotype in gt_details:
        count_gt = re.split(':', count_genotype)
        if '1' in count_gt[0]:
            count_gts += 1

    frequency = round((float(count_gts)/float(len(samples))),3)
    
    
    
    # this is for printing the output
    count = 0 # this one counts samples with a useful genotype
    for genotype in gt_details:
        gt_split = re.split(':', genotype)          
        if '1' in gt_split[0]:
            print samples[count]  +  '\t' + chr + '\t' + snv_start + '\t' + snv_end + '\t' + consequence_dict['SYMBOL'] + '\t' + ref + '\t' + alt + '\t'  + str(frequency) + '\t' + gt_split[0]   + '\t' \
            + consequence_dict['Consequence'] + '\t' + gt_split[9] + '\t' + consequence_dict['GMAF'] + '\t' + consequence_dict['Existing_variation'] + '\t' + consequence_dict['ExAC_EAS_AF'] + '\t' +\
             consequence_dict['ExAC_AMR_AF'] + '\t' + consequence_dict['ExAC_AMR_AF'] + '\t' + consequence_dict['ExAC_NFE_AF'] + '\t' + consequence_dict['ExAC_AF']  + '\t' + consequence_dict['ExAC_FIN_AF'] \
             + '\t' +  consequence_dict['ExAC_OTH_AF'] + '\t' + consequence_dict['ExAC_SAS_AF'] + '\t' + consequence_dict['CLIN_SIG'] + '\t' + consequence_dict['SIFT'] + '\t' + consequence_dict['PolyPhen'] \
             + '\t' + gt_split[3]
            count += 1
   
        else:
            count += 1
            next
