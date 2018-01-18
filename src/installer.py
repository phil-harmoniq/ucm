import os
import subprocess
from app_info import APP_INSTALL_DIR


def add_ucm_symlink() -> None:
    symlink_already_exists()


def symlink_already_exists() -> None:
    if os.path.isfile(f"{APP_INSTALL_DIR}/ucm"):
        print("UCM is already installed.")
    else:
        print("Installing...")
        subprocess.call(["ln", "-s", f"{os.environ['UCM_DIR']}/ucm", APP_INSTALL_DIR])
