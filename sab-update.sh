#!/bin/bash
#set -e
#set -o pipefail

echo "[-] stopping sabnzd"
stop sabnzbd
echo "[+] sabnzd stopped"

cd /tmp/
echo "[-] downloading latest version"
wget -q http://sourceforge.net/projects/sabnzbdplus/files/latest/download\?source\=dlp -O sabnzbd.tar.gz || exit 1
echo "[+] downloading done"

FOLDER=`tar -xvzf sabnzbd.tar.gz | sed 's/\/.*//' | tail -n1`
rm sabnzbd.tar.gz
echo "[-] extracting update"
mv $FOLDER /usr/local/bin
if [[ $? -ne 0 ]]; then
    start sabnzbd || echo "[!] something went wrong: could not start sabnzbd"; exit 1
    rm -rf $FOLDER
    echo "already up to date"
    exit 0
fi
echo "[+] extracted"

cd /usr/local/bin
chown fkalter:fkalter $FOLDER
rm SABnzbd
ln -s /usr/local/bin/$FOLDER /usr/local/bin/SABnzbd
echo "[+] links created"

echo "[+] restarting sabnzb"
start sabnzbd || echo "[!] something went wrong: could not start sabnzbd"; exit 1
echo "[+] Done: updated to ${FOLDER}"
