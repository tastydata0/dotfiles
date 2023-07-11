#!/usr/bin/bash

amixer set Capture toggle && amixer get Capture | grep '\[off\]' && notify-send "Microphone muted" || notify-send "Microphone unmuted"