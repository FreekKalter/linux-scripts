#!/bin/bash
TARSNAP=/usr/local/bin/tarsnap
HOME=/home/fkalter
OPTIONS="--configfile $HOME/.tarsnaprc"
TSR=$HOME/gopath/bin/tsr
LOG=/var/log/tarsnap

echo "`date`------------------------------------------------------------------------------" >> $LOG/log.log
$TARSNAP  $OPTIONS -c -f "log(`$TSR --time`)" /var/log &>> $LOG/log.log
$TSR --configfile $HOME/.tarsnaprc --delete log &>> $LOG/log.log

echo "`date`------------------------------------------------------------------------------" >> $LOG/etc.log
$TARSNAP $OPTIONS -c -f "etc(`$TSR --time`)" /etc  &>> $LOG/etc.log
$TSR --configfile $HOME/.tarsnaprc --delete etc &>> $LOG/etc.log

echo "`date`------------------------------------------------------------------------------" >> $LOG/home.log
$TARSNAP $OPTIONS --aggressive-networking -X $HOME/.tarsnap-home-exclude -c -f "home(`$TSR --time`)" $HOME &>> $LOG/home.log
$TSR --configfile $HOME/.tarsnaprc --delete home &>> $LOG/home.log
