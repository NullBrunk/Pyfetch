#!/bin/bash

if [ -z $1 ]; then

    echo "Usage: ./install.sh ( install | remove )"

    exit

fi

if [ $1=="install" ]; then

    pip3 install termcolor

    git clone https://github.com/NullBrunk/Morpion

    mv Morpion/morpion.py .

    rm -r Morpion

    echo "[+] Done"

elif [ $1=="remove" ]; then

    pip3 uninstall termcolor

    rm morpion.py

else

    echo "[!] Unrecognized argument: $1"

fi
