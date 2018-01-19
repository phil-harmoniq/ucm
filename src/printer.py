from __init__ import APP_STRING, CLI_WIDTH


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
