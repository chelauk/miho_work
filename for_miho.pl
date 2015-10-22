#!/usr/bin/perl 

use strict;
use warnings;

open (my $fh, '<', $ARGV[0]) || die "Can not open $ARGV[0]\n";
print "Chrom\tPosition\tRef\tAlt\tNo Samples\tMean Depth\tStd_dev\tDepths\n";
while(<$fh>){
	chomp;
	my @line=split(/ /, $_);
	my $chrom = $line[0];
	my $start = $line[1];
	my $ref = $line[2];
	my $alt = $line[3];
	my $elements = scalar @line;
	my $number_of_depths = $elements-4;
	my @depths = @line[-$number_of_depths..-1];
	my $num_samples=scalar @depths;
	my $sum = eval join '+', @depths;
	my $mean_depth = $sum/$num_samples;
	my @variance = map { $_ - $mean_depth } @depths;
	my @squares = map { $_ * $_ } @variance;
	my $variance = (eval join '+', @squares)/$num_samples;
	my $std_dev = sqrt($variance);
	print $chrom,"\t",$start,"\t",$ref,"\t",$alt,"\t",$num_samples,"\t",$mean_depth,"\t",$std_dev,"\t","@depths","\n";
	} 
