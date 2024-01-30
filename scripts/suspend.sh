#!/bin/sh

playerctl -a pause

if [[ -x '/usr/bin/betterlockscreen' ]]; then
  betterlockscreen -l &
elif [[ -x '/usr/bin/i3lock' ]]; then
  i3lock &
fi

systemctl suspend
