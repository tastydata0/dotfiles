#!/bin/sh

# A dwm_bar function that displays the current keyboard layout
# Joe Standring <git@joestandring.com>
# GNU GPLv3

# Dependencies: xorg-setxkbmap

dwm_keyboard () {
    printf "%s" "$SEP1"
    if [ "$IDENTIFIER" = "unicode" ]; then
        t=$(xset -q | grep LED)
        code=${t##*mask:  }


        if [[ $code -eq "00000000" ]]; then
                result="EN"
        else
                result="RU"
        fi
        icon=""
        printf "$icon $result"

    else
        printf "KEY %s" "$(setxkbmap -query | awk '/layout/{print $2}')"
    fi
    printf "%s\n" "$SEP2"
}

dwm_keyboard
