#!/bin/sh


dwm_pomodoro () {
    printf "%s" "$SEP1"
    printf "`$DIR/../pomodoro/i3-gnome-pomodoro status`"
    printf "%s\n" "$SEP2"
}

dwm_pomodoro
