#!/bin/bash
set -euo pipefail
IFS=$'\t\n'

cd /home/fkalter/scripts/sabnzbd

rm -rf test/*

mkdir test/kjdfksjdflsdjf-sample
mkdir test/Main\ Movie-x264

cp test-blob.bin test/kjdfksjdflsdjf-sample/This-is-main-movie.avi
touch test/kjdfksjdflsdjf-sample/niks.nzb
