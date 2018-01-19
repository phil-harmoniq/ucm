import os
import subprocess
from __init__ import SOURCE_DIR, LAUNCH_FILE


LAUNCH_STRING = ('#!/usr/bin/env bash\n'
                 '\n'
                 f'UCM_DIR={SOURCE_DIR}\n'
                 'exec -a UCM python3 "$UCM_DIR" "$@"\n')


def install_launch_script() -> None:
    if symlink_already_exists():
        print("UCM is already installed.")
    else:
        print("Installing launch script...")
        with open(LAUNCH_FILE, "w") as launcher:
            launcher.write(LAUNCH_STRING)
        subprocess.call(["chmod", "a+x", LAUNCH_FILE])


def remove_launch_script() -> None:
    if symlink_already_exists():
        print("Removing launch script...")
        os.remove(LAUNCH_FILE)
    else:
        print("UCM isn't currently installed.")


def symlink_already_exists() -> bool:
    if os.path.isfile(LAUNCH_FILE):
        return True
    return False
