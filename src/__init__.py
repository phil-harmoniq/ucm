import os


APP_NAME = "Unix Configuration Manager"
APP_VERSION = "0.0.1"


APP_STRING = f"{APP_NAME} v{APP_VERSION}"
SOURCE_DIR = os.path.dirname(os.path.realpath(__file__))
INSTALL_DIR = os.path.join("/", "usr", "local", "bin")
LAUNCH_FILE = os.path.join(INSTALL_DIR, "ucm")
CLI_WIDTH = 64
