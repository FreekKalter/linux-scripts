#!/bin/bash
set -euo pipefail
IFS=$'\t\n'

cd /home/fkalter/scripts/sabnzbd

for filename in "$@"; do
    ./cleanup_combined.sh "$filename"
done
