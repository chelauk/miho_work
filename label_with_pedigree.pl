#!/usr/bin/perl

use strict;
use warnings;


my %dictionary;



open (my $fh,"<",$ARGV[0]) or die "can not open $ARGV[0]\n";

while(<$fh>){
	chomp;
	my @line = split(/\t/, $_);
	my $position = $line[0]."\t".$line[1];
	my $ref = $line[2];
	my $alt = $line[3];
	my $sample = $line[4];
	my $pedigree = $line[7];
	my $sample_ped = $sample."---".$pedigree;
	push @{$dictionary{$position}}, $sample_ped;
	}

foreach my $key (keys %dictionary){
	print $key,"\t\t","@{$dictionary{$key}}\n";
	}
