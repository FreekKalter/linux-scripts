# scripts

## Description
A wide selection of scripts I use on my main workstation/home pc.
These scripts are written in alot of languages from bash to go and from perl to python.
I call them scripts because hey have all 1 thing in common, there are *very specific*.
Which means I wroten them for my own specific usecase , and they are working well
in my setup (read this as a disclaimer). I also have a folder with one-offs, wich are scripts i have written for 1
task and probably will never use agian. But i keep them around for future reference.

This repo lives in my home directoty under ~/scripts. I added this to my $PATH, and so all files that are executable
are at my fingertips.

Sometimes a script might be useful to other people. I will clean it up and give it some sensible commandline options
(opposed to hardcoded defautls) before i extract it into its own repo. For example:

- [text](https://github.com/FreekKalter/text) a golang package for printing nicely formatted columns in cli apps
- [gls](https://github.com/FreekKalter/gls) performs a quick status checks on multiple git repos in a "projects" directory
- [geoselect](https://github.com/FreekKalter/geoselect) a script to selct photos from a set based on geographical location

## Index

### find_missing

A python script to find missing files in a series of numbered files.
It grabs the first number from every file specified, and checks if any numbers are missing from a series.
For example, a directory with the files: file_1.txt, file_2.txt and file_4.txt

Running *find_missing* in this directory will print '3', since this number is missing in the serie 1-4.

### passgen

Very simple password generation utility, writtin in Perl.
