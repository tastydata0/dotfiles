#!/bin/sh

crudini --set --inplace --ini-options=ignoreindent /etc/dunst/dunstrc urgency_normal foreground "$(jq '.special.foreground' <<< `cat $HOME/.cache/wal/colors.json`)"
crudini --set --inplace --ini-options=ignoreindent /etc/dunst/dunstrc urgency_normal background "\"$(jq -r '.special.background' <<< `cat $HOME/.cache/wal/colors.json`)e9\""


crudini --set --inplace --ini-options=ignoreindent /etc/dunst/dunstrc urgency_low foreground "$(jq '.special.foreground' <<< `cat $HOME/.cache/wal/colors.json`)"
crudini --set --inplace --ini-options=ignoreindent /etc/dunst/dunstrc urgency_low background "\"$(jq -r '.special.background' <<< `cat $HOME/.cache/wal/colors.json`)e9\""

# Frame
crudini --set --inplace --ini-options=ignoreindent /etc/dunst/dunstrc global frame_color "$(jq '.colors.color6' <<< `cat $HOME/.cache/wal/colors.json`)"

killall dunst
