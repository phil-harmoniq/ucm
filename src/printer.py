from __init__ import APP_STRING, CLI_WIDTH, APP_VERSION


def say_hello() -> None:
    new_width = CLI_WIDTH - len(APP_STRING) - 2
    left_bar = int(new_width / 2)
    if new_width % 2 > 0:
        right_bar = int(new_width / 2) + 1
    else:
        right_bar = int(new_width / 2)
    print(f"\n{'-' * left_bar} {APP_STRING} {'-' * right_bar}")


def say_bye() -> None:
    print(f'{"-" * CLI_WIDTH}\n')


def show_help_menu() -> None:
    say_hello()
    print('\n               Usage:'
          '\n       ucm [arguments] [command]'
          '\n'
          '\n            Commands:'
          '\n     install: Make UCM available on $PATH'
          '\n      remove: Remove UCM from $PATH'
          '\n       track: Add given file to config cache'
          '\n     untrack: Remove given file from config cache'
          '\n        list: Show list of all currently tracked files'
          '\n'
          '\n           Arguments:'
          '\n    --verbose or -v: Verbose output'
          '\n       --help or -h: Help menu'
          '\n          --version: Show UCM version'
          '\n')
    say_bye()


def show_version() -> None:
    print(APP_VERSION)
