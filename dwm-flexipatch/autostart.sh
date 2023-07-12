#!/usr/bin/bash

~/dwm-flexipatch/dwm-bar/dwm_bar.sh > /dev/null &

~/xrandr_setup.sh 

$HOME/dwm-flexipatch/scripts/dwm-theme-switcher/theme-switch -n -r

setxkbmap -layout us,ru -option grp:alt_shift_toggle

~/dwm-flexipatch/picom/build/src/picom -b --animations --animation-window-mass 0.5 --animation-for-open-window zoom --animation-stiffness 300 --vsync --experimental-backends

notify-send "Welcome"

spotify &
