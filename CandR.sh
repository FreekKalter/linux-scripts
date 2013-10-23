#!/bin/bash

# strip of the extensin (.c, .s ,..)
base=${1%.*}

# act based upon extension
case "${1##*.}" in
    c)
        gcc -ggdb -o $base $1
        ;;
    s | asm)
        as --gstabs -o ${base}.o $1
        ld -o $base ${base}.o
        rm ${base}.o
        ;;
    nasm)
        nasm -f elf32 -o ${base}.o $1
        ld -o $base ${base}.o
        rm ${base}.o
        ;;
    *)
        echo "extension not recongized"
        exit
        ;;
esac

# pass extra arguments given on to the build executable
# shift strips the source file given to ./run
shift
./$base "$@"
