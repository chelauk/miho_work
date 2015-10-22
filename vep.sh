 while read i;do perl ~/variant_effect_predictor/variant_effect_predictor.pl --everything --refseq --cache -i $i.recode.vcf -o $i;done<samples
