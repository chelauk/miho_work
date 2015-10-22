#!/usr/bin/perl

use warnings;
use strict;
my $position;
my %dictionary;
my @line2;
my $gene_effect;

open (my $fh, "<", $ARGV[0]) or die "Can not open ARGV[0]\n";

while (<$fh>){
	chomp;
	my @line = split(/\t/, $_);
	$position = $line[0]."\t".$line[1];
	$gene_effect = $line[4]."\t".$line[5];
	$dictionary{$position} = $gene_effect;
	}
close $fh;

open (my $fh2, "<", $ARGV[1]) or die "Can not open ARGV[1]\n";

while (<$fh2>){
	chomp;
	@line2 = split(/\t/, $_);
	my $position2=$line2[0]."\t".$line2[1];
	if (exists $dictionary{$position2}){
		print $line2[0]."\t".$line2[1]."\t".$line2[2]."\t".$line2[3]."\t"."$dictionary{$position2}"."\t".$line2[4]."\t".$line2[5]."\t".$line2[6]."\t".$line2[7]."\n";
		}
	}
close $fh2;
