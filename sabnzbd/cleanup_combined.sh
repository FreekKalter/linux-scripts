#!/bin/bash
set -euo pipefail
IFS=$'\t\n'

cd /home/fkalter/scripts/sabnzbd

echo "[-] starting cleanup.pl $1"
./cleanup.pl "$1"
echo "[-] starting cleanupfilename.py $1"
# remove cruft from filename from wich rename_dir.py may conclude it is valid english when its not
# ex: "garbagefilene sample" is considerd valid english because the word 'sample' is valid
cleanup=$(./cleanupfilename.py "$1")
echo "[-] starting rename_dir.py $cleanup"
renamed=$(./rename_dir.py "$cleanup")
final=$renamed
if [ $cleanup != $renamed ]; then
    echo "[-] starting cleanupfilename.py again with $renamed"
    final=$(./cleanupfilename.py "$renamed")
fi
echo "Done: ${final##*/}"
