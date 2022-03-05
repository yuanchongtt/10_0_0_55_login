import argparse
import sys

from .action import Action
from .config import read_config
from .user import User


def main():
    parser = argparse.ArgumentParser(description="Login to BIT network")
    parser.add_argument("action", choices=["login", "logout"], help="login or logout")
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.username and args.password:
        user = User(args.username, args.password)
    elif conf := read_config():
        user = User(*conf)
    else:
        parser.print_usage()
        sys.exit(1)

    try:
        if args.action == "login":
            res = user.do_action(Action.LOGIN)
        else:
            res = user.do_action(Action.LOGOUT)

        if args.verbose:
            print("\33[34m[Info]\033[0m", res)

    except Exception as e:
        print("\033[91m[Error]", e, "\033[0m")


if __name__ == "__main__":
    main()