#!/usr/bin/env python
import os
import sys
import time
import subprocess
from daemonize import Daemonize

# Путь к файлу с кэшем
CACHE_FILE = "/tmp/screen_settings_cache"

DEFAULT_TEMP = 6500
DEFAULT_TEMP = float(os.popen("redshift -p | grep Color | cut -d' ' -f3").read().strip()[:-1])

DEFAULT_BRIGHTNESS = 1


def get_screen_settings():
    try:
        with open(CACHE_FILE, 'r') as file:
            content = file.read()
            temp, brightness = map(float, content.strip().split())
            return temp, brightness
    except FileNotFoundError:
        # Если файл не найден, создаем новый с дефолтными значениями
        save_screen_settings(DEFAULT_TEMP, 1)
        return DEFAULT_TEMP, 1

def save_screen_settings(temp, brightness):
    brightness = max(0.1, min(1, brightness))
    temp = max(1000, min(10000, temp))
    with open(CACHE_FILE, 'w') as file:
        file.write(f"{temp} {brightness}")

def apply_redshift(temp, brightness):
    command = f"redshift -m vidmode -O {temp} -b {brightness} -P"
    subprocess.run(command, shell=True)
    os.system(f'notify-send -u low "Brightness: {brightness}, Temp: {temp}"')

def change_settings(temp_change, brightness_change):
    current_settings = get_screen_settings()
    if current_settings:
        current_temp, current_brightness = current_settings
        new_temp = max(1000, min(10000, current_temp + temp_change))
        new_brightness = max(0.1, min(1, current_brightness + brightness_change))
        new_brightness = round(new_brightness * 10) / 10
        print(f"Current settings: {current_temp}, {current_brightness}")
        print(f"New settings: {new_temp}, {new_brightness}")
        save_screen_settings(new_temp, new_brightness)
        apply_redshift(new_temp, new_brightness)
    else:
        print("Error: Cache file not found.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python script.py start|stop|restart|temp_change brightness_change")
        sys.exit(1)

    if len(sys.argv) == 2:
        if sys.argv[1] == "reset":
            save_screen_settings(DEFAULT_TEMP, 1)
            apply_redshift(DEFAULT_TEMP, 1)
            print("Settings reset to default:", DEFAULT_TEMP, 1)
            sys.exit(0)
    elif len(sys.argv) == 3:
        temp_change = float(sys.argv[1])
        brightness_change = float(sys.argv[2])
        change_settings(temp_change, brightness_change)
    else:
        print("Invalid arguments.")
        sys.exit(1)
