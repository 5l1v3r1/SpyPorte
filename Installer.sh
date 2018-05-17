#!/bin/bash

## Check User Is Root..:)

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;31m[!]\e[0;31m Error: Please Run This Script As ROOT !\n"
   exit 1
fi

# Installer...
printf "\n\e[1;32m[*]\e[0;32m Installing.....\e[1;33m SpyPorte\n"
sleep 2
mv SpyPorte.py spyporte
chmod +x spyporte
mv spyporte /usr/bin/
printf "\n\n\e[1;31m[\e[1;33m*\e[1;31m] \e[1;35m Done! SpyPorte Has Been Installed.\e[1;32m!!!\n\e[1;37m[*] Type \e[1;32m[ spyporte ]\e[1;37m In Your Terminal To Run It\e[1;32m :)\n"
rm -rf *

