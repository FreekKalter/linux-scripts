#!/bin/bash
echo "[-] mounting truecrypt volumes"
sudo truecrypt --auto-mount=favorites --keyfiles=./mnt-secret/secret/down_secret
cp -H ~/scripts/gtk-bookmarks ~/.config/gtk-3.0/bookmarks
echo "[+] mounting done"

echo "[-] starting docker"
sudo service docker start
echo "[+] docker started"


echo "[-] starting sabnzb"
sudo start sabnzbd
echo "[+] sabnzb started"

ssh-add
ln -fs $SSH_AUTH_SOCK /home/fkalter/.ssh_auth_sock

echo "[-] starting dropbox"
dropbox start
echo "[+] dropbox started"
