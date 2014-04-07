#!/bin/bash
TARSNAP=/usr/local/bin/tarsnap
HOME=/home/fkalter
TSR=$HOME/gopath/bin/tsr
LOG=/var/log/tarsnap

if [[ $1 == "root" ]]; then
    echo "`date`------------------------------------------------------------------------------" >> $LOG/log.log
    $TARSNAP --configfile $HOME/.tarsnaprc -c -f "log(`$TSR --time`)" /var/log &>> $LOG/log.log
    $TSR --configfile $HOME/.tarsnaprc --delete log &>> $LOG/log.log

    echo "`date`------------------------------------------------------------------------------" >> $LOG/etc.log
    $TARSNAP --configfile $HOME/.tarsnaprc -c -f "etc(`$TSR --time`)" /etc  &>> $LOG/etc.log
    $TSR --configfile $HOME/.tarsnaprc --delete etc &>> $LOG/etc.log
else
    echo "`date`------------------------------------------------------------------------------" >> $LOG/home.log
    $TARSNAP --configfile $HOME/.tarsnaprc -c -f "home(`$TSR --time`)" $HOME &>> $LOG/home.log
    $TSR --configfile $HOME/.tarsnaprc --delete home &>> $LOG/home.log
fi
