#!/usr/bin/bash

pip install meson
pip install -r ./dwm-flexipatch/reqirements.txt

sudo pacman -Sy `cat dwm-flexipatch/pacman_dependencies.txt`
yay -Sy `cat dwm-flexipatch/yay_dependencies.txt`

cp -r .config/* ~/.config/
cp -r dwm-flexipatch ~/

cd ~/dwm-flexipatch && sudo make install

sudo cp ./dwm.desktop /usr/share/xsessions/

# Wallpapers
mkdir ~/Pictures/Wallpapers
cp -r ./Wallpapers/0 ~/Pictures/Wallpapers/
cp -r ./Wallpapers/1 ~/Pictures/Wallpapers/
