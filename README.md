# miho_work


Processing Miho's vcfs
1) split vcfs from big vcf file
vcf file was in a weird format, took a while to fix


my idea now is to get the ASM files to create a vep input

awk 'BEGIN{OFS="\t"}!x[$1 $2 $3]++{split($1,a,"_");print a[1],a[2],a[2],a[3]}' GS800002252-ASM

perl -nae 'if (length($F[3])>3){print $F[2],$F[3],"\n"}' GS800002252-ASM.vep.input

I have to sort out the coordinates for the dels and insertions though

http://www.ensembl.org/info/docs/tools/vep/vep_formats.html

just starting with this to check the lenght of the anno.

doesn't quite work because several alternate alleles is greater than 3 too.


perl -nae 'if (length($F[3])>3){print $F[3],"\n"}' GS800002252-ASM.vep.input

in this instance

1_876499_A/GG  1:876499 is an A and GG has been entered, I nearly sure this is a simple gg insertion rather than a snv + insertion event

