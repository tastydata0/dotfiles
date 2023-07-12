#!/usr/bin/bash

mkdir .config

# Clean previous
rm -rf ~/dotfiles/.config ~/dotfiles/dwm-flexipatch ~/dotfiles/Wallpapers

cp -r ~/.config/alacritty .config
cp -r ~/.config/my-theme-switch .config
#cp -r ~/.config/chadwm/ .config
cp -r ~/.config/rofi/ .config

cp -r ~/dwm-flexipatch .

cp /usr/share/xsessions/dwm.desktop .

# Wallpapers
mkdir Wallpapers
cp -r ~/Pictures/Wallpapers/0 ./Wallpapers
cp -r ~/Pictures/Wallpapers/1 ./Wallpapers
