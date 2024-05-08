#!/bin/bash

HOST=$(hostname)

# configure .bashrc
echo '
export PS1="\e[1;36m\u@\h:\e[m \e[0;32m\w\e[m\n$ "' >> /home/$(whoami)/.bashrc
echo "export PATH=$PATH:/opt/elrond/elrond" >> /home/$(whoami)/.bashrc
source ~/.bashrc

# configure terminal to launch on login
sudo rm -rf /home/$(whoami)/.config/autostart/gnome-terminal.desktop
sudo rm -rf gnome-terminal.desktop
echo "[Desktop Entry]
Type=Application
Exec=gnome-terminal
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_NG]=Terminal
Name=Terminal
Comment[en_NG]=Start Terminal On Startup
Comment=Start Terminal On Startup" > gnome-terminal.desktop
sudo chmod 744 gnome-terminal.desktop
sudo chown -R $(whoami):$(whoami) gnome-terminal.desktop
mkdir -p /home/$(whoami)/.config/autostart
sudo mv gnome-terminal.desktop /home/$(whoami)/.config/autostart/
sudo chmod 744 /home/$(whoami)/.config/autostart/gnome-terminal.desktop

# cleaning uneeded applications
sudo du -sh /var/cache/apt/archives
sudo apt update
sudo apt-get clean
sudo apt update
sudo updatedb