#!/bin/bash

echo "[-] building go from source"
cd ~/go/src
git pull
./all.bash
go get -u golang.org/x/tools/cmd/...
go get -u github.com/laher/goxc
goxc -t
echo "[+] done building"
