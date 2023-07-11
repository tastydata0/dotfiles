#!/usr/bin/bash

mkdir .config

rm -rf ~/dotfiles/.config ~/dotfiles/dwm-flexipatch

cp -r ~/.config/alacritty .config
cp -r ~/.config/my-theme-switch .config
#cp -r ~/.config/chadwm/ .config
cp -r ~/.config/rofi/ .config

cp -r ~/dwm-flexipatch .

