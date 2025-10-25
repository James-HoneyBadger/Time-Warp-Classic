#!/usr/bin/env perl
# Perl Example Program - Text Processing and Pattern Matching
# This program demonstrates Perl's powerful text processing capabilities

use strict;
use warnings;
use feature 'say';

# Sample text for processing
my $sample_text = q{
Welcome to TimeWarp IDE - A Multi-Language Programming Environment!

This IDE supports: PILOT, BASIC, Logo, Python, JavaScript, and Perl.

Features include:
- Turtle graphics for visual programming
- Multiple themes for different coding environments
- Interactive debugging and code execution
- Plugin system for extensibility

Perl is known for its excellent text processing capabilities!
};

# Function to count words
sub count_words {
    my ($text) = @_;
    my @words = split /\s+/, $text;
    return scalar @words;
}

# Function to find programming languages mentioned
sub find_languages {
    my ($text) = @_;
    my @languages = $text =~ /\b(PILOT|BASIC|Logo|Python|JavaScript|Perl)\b/g;
    return @languages;
}

# Function to extract features
sub extract_features {
    my ($text) = @_;
    my @features;
    while ($text =~ /- (.+)$/gm) {
        push @features, $1;
    }
    return @features;
}

# Function to create a word frequency hash
sub word_frequency {
    my ($text) = @_;
    my %freq;
    foreach my $word (split /\s+/, lc $text) {
        # Remove punctuation
        $word =~ s/[[:punct:]]//g;
        next if length($word) < 3;  # Skip short words
        $freq{$word}++;
    }
    return %freq;
}

# Main program
say "🟫 Perl Text Processing Example";
say "=" x 50;

say "Original text:";
say $sample_text;
say "";

# Demonstrate word counting
my $word_count = count_words($sample_text);
say "📊 Word count: $word_count";

# Find programming languages
my @languages = find_languages($sample_text);
say "💻 Programming languages mentioned: " . join(", ", @languages);

# Extract features
my @features = extract_features($sample_text);
say "✨ Features found:";
foreach my $feature (@features) {
    say "  • $feature";
}

# Word frequency analysis
say "\n📈 Word frequency analysis (words > 3 chars):";
my %freq = word_frequency($sample_text);
my @top_words = sort { $freq{$b} <=> $freq{$a} } keys %freq;
my $count = 0;
foreach my $word (@top_words) {
    last if $count >= 10;  # Show top 10
    say "  $word: $freq{$word}";
    $count++;
}

# Interactive section
say "\n🎯 Now let's try some interactive text processing!";
say "Enter some text to analyze (or 'quit' to exit):";

while (1) {
    print "> ";
    my $input = <STDIN>;
    chomp $input;

    last if lc $input eq 'quit';

    if (length $input > 0) {
        my $input_words = count_words($input);
        say "Your text has $input_words words.";

        # Check for programming languages
        my @input_languages = find_languages($input);
        if (@input_languages) {
            say "Programming languages mentioned: " . join(", ", @input_languages);
        }

        # Simple sentiment analysis (very basic)
        my $positive_words = $input =~ /\b(good|great|excellent|awesome|fantastic|amazing|wonderful)\b/gi;
        my $negative_words = $input =~ /\b(bad|terrible|awful|horrible|worst)\b/gi;

        if ($positive_words > $negative_words) {
            say "😊 Your text seems positive!";
        } elsif ($negative_words > $positive_words) {
            say "😔 Your text seems negative.";
        } else {
            say "😐 Your text is neutral.";
        }
    }

    say "Enter more text or 'quit' to exit.";
}

say "\n👋 Thanks for exploring Perl text processing!";
say "Perl is excellent for text manipulation, regular expressions, and system administration.";