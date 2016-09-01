#!/bin/bash
set -e
set -o pipefail

PATH=/usr/local/bin/:$PATH
TARSNAPPER=/home/fkalter/.local/bin/tarsnapper
HOME=/home/fkalter
TARSNAPRC="/usr/local/etc/tarsnap.conf"
TARSNAPPER_YML="$HOME/.tarsnapper.conf"
LOG=/var/log/tarsnap/tarsnap.log

echo "`date`------------------------------------------------------------------------------" >> $LOG
$TARSNAPPER -o configfile $TARSNAPRC -o v -o print-stats -v -c $TARSNAPPER_YML make &>> $LOG
