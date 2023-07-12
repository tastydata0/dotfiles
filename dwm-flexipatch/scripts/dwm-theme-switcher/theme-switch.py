# /usr/bin/python

from argparse import ArgumentError
import os
import re
import sys
import json
from time import sleep

pywal_util_path = os.path.expandvars(
    "$AUTOMATIONHOME/linux/kde/pywal-utils/pywal_util.py"
)
config_path = os.path.expandvars("$HOME/.config/my-theme-switch/config.json")
with open(config_path, "r") as f:
    config = json.load(f)

index = -2
if len(sys.argv) > 1:
    arg = int(sys.argv[1])
    if arg in (0, 1):
        index = arg
    elif arg == -1:
        index = 1 - config["light"]
    else:
        raise ArgumentError(argument=None, message="Invalid argument")
else:
    index = 1 - config["light"]

assert index != -2
print(index)

# print("Saving previous wallpaper...")


# print("Changing theme (lookandfeeltool)...")
# # Prevent wallpaper glitch
# black_screen_path = os.path.expandvars("$HOME/Windows/Users/Alex/Pictures/black.png")
# # os.system(f'wal -s -i "{black_screen_path}" ')

# global_theme = config["global_theme"][index]
# os.system(f"lookandfeeltool -a {global_theme}")

# applcation_style = config["applcation_style"][index]
# os.system(
#     f"~/Applications/plasma-theme-switcher/cmake-build-release/plasma-theme -w {applcation_style} &"
# )

# # KDE colors
# print("Changing kde colors...")
# color_scheme = config["color_scheme"][index]
# os.system(
#     f"$AUTOMATIONHOME/linux/kde/pywal-utils/plasma-theme-switcher/cmake-build-release/plasma-theme -c {color_scheme} &"
# )


# # Window decoration
# print("Setting window decoration...")
# window_decoration_config = """

# # Added automatically by my-theme-switch.py
# [org.kde.kdecoration2]
# BorderSize=Tiny
# BorderSizeAuto=false
# library=org.kde.bismuth.decoration
# theme=Bismuth
# """
# # with open('/home/alex/.config/kwinrc', 'r') as f:
# #     kwin_config = f.read()
# #     replaceable = re.search(re.compile(r'\[org.kde.kdecoration2\][^\[]+'), kwin_config)[0]
# #     kwin_config = kwin_config.replace(replaceable, window_decoration_config)
# with open(os.path.expandvars("$HOME/.config/kwinrc"), "a") as f:
#     f.write(window_decoration_config)


print("Changing theme (vscode)...")
vscode_settings_path = "/home/alex/.config/Code/User/settings.json"
with open(vscode_settings_path, "r") as f:
    vscode_json_config = json.load(f)
    vscode_json_config["workbench.colorTheme"] = config["vscode_theme"][index]
    with open(vscode_settings_path, "w") as f2:
        json.dump(vscode_json_config, f2)


konsole_dynamic_profile_path = "/home/alex/.local/share/konsole/Dynamic.profile"
konsole_base_profile_path = "/home/alex/.local/share/konsole/MyLight [base].profile"
konsole_theme = config["konsole_theme"][index]
os.system(f'cp "{konsole_base_profile_path}" "{konsole_dynamic_profile_path}"')
with open(konsole_dynamic_profile_path, "a") as f:
    f.write(f"[Appearance]\nColorScheme={konsole_theme}\n\n[General]\nName=Dynamic")

# Btop
btop_dynamic_theme_path = "/home/alex/.config/btop/btop-dynamic.theme"
btop_theme_path = config["btop_theme"][index]
os.system(f"cp {btop_theme_path} {btop_dynamic_theme_path}")


# Qt Creator
qt_creator_config_path = "/home/alex/.config/QtProject/QtCreator.ini"
qt_creator_theme = config["qt_creator_theme"][index]
# qt_config = configparser.ConfigParser()
# qt_config.read(qt_creator_config_path)
# qt_config['Core']['CreatorTheme'] = qt_creator_theme
# with open(qt_creator_config_path, 'w') as f:
#     qt_config.write(f)

with open(qt_creator_config_path) as f:
    qt_config_ini = f.read()
qt_creator_replace_text = re.search(re.compile("CreatorTheme=.+"), qt_config_ini).group(
    0
)
print(qt_creator_replace_text, f"CreatorTheme={qt_creator_theme}")
qt_config_ini = qt_config_ini.replace(
    qt_creator_replace_text, f"CreatorTheme={qt_creator_theme}"
)
with open(qt_creator_config_path, "w") as f:
    f.write(qt_config_ini)


# Wallpaper
wallpaper = config["wallpaper"][index]
print(wallpaper)

if os.environ.get('DESKTOP_SESSION') == 'dwm':
    pass
else:
    os.system(
        f'python {pywal_util_path} --wallpaper {wallpaper} {"--light" if index == 1 else ""} --monitor -1'
    )
    os.system(
        f'python {pywal_util_path} --wallpaper {wallpaper} {"--light" if index == 1 else ""} --monitor 0 &'
    )



# # Lock screen wallpaper
# lock_screen_wallpaper = config["lock_screen_wallpaper"][index]

# with open("/home/alex/.config/kscreenlockerrc", "r") as f:
#     lock_screen_config = f.read()

# lock_screen_config = lock_screen_config.replace(
#     re.search(re.compile("Image=.+"), lock_screen_config)[0],
#     f"Image={lock_screen_wallpaper}",
# )

# with open("/home/alex/.config/kscreenlockerrc", "w") as f:
#     f.write(lock_screen_config)


os.system("mkdir /home/alex/.config/my-theme-switch &> /dev/null")
config["light"] = index
with open(config_path, "w") as f:
    json.dump(config, f, indent=4)

# Dolphin restart to reset terminal theme
# os.system('ps -A | grep dolphin && killall dolphin && dolphin &')
# os.system('xdotool search  "Dolphin" windowminimize')

# os.system("kwin_x11 --replace  >/dev/null 2>&1 &")
# sleep(0.1)
# os.system(
#     """for w in $(xdotool search --name ".*"); do 
#         xdotool windowminimize "$w" 
#     done
#     """
# )
