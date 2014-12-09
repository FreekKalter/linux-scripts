#!/bin/bash
echo "[-] mounting truecrypt volumes"
sudo truecrypt --auto-mount=favorites --keyfiles=/mnt/secret/down_secret
cp -H ~/scripts/gtk-bookmarks ~/.config/gtk-3.0/bookmarks
echo "[+] mounting done"

echo "[-] starting docker"
sudo service docker start
echo "[+] docker started"


echo "[-] starting sabnzb"
sudo start sabnzbd
echo "[+] sabnzb started"

ssh-add
ln -s $SSH_AUTH_SOCK /home/fkalter/.ssh_auth_sock

echo "[-] starting dropbox"
dropbox start
echo "[+] dropbox started"

# Build Go from tip every week
# (not a cron job because it needs an attached terminal)
cd ~/go/src
# only on wednesday (day 3 of the week)
if [ `date +%-u` -eq 3 ]; then
    echo "[-] building go from source"
    hg pull
    hg update default
    ./all.bash
    go get -u code.google.com/p/go.tools/cmd/...
    go get -u github.com/laher/goxc
    goxc -t
    echo "[+] done building"
fi
