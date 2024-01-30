#!/bin/bash

amixer set Capture toggle && amixer get Capture | grep '\[off\]' && notify-send -u low "Microphone muted" || notify-send -u low "Microphone unmuted"
