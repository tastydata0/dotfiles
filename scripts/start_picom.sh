#!/bin/sh
pidof picom > /dev/null || ~/dwm-flexipatch/picom/build/src/picom -b --animations --animation-window-mass 0.9 --animation-for-open-window zoom --animation-stiffness 250 --vsync --experimental-backends

