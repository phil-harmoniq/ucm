def say_hello(app_name: str, app_version: str) -> None:
    print("\n-------------------- ", end="")
    print(f"{app_name} v{app_version}", end="")
    print(" --------------------")


def say_bye() -> None:
    print("--------------------")
