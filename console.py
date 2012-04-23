#!/usr/bin/env python3
import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["serve"])
    namespace, args = parser.parse_known_args()

    if namespace.action == "serve":
        parser.add_argument("--server", default="wsgiref")
        parser.add_argument("--host", default="127.0.0.1")
        parser.add_argument("--port", type=int, default=8080)
        parser.add_argument("--hostname", default="cdn.rithis.com")
        parser.add_argument("--root", default=os.path.join(os.path.dirname(__file__), "files"))

        kwargs = vars(parser.parse_args())
        from blanche import main as action

    else:
        return

    del kwargs["action"]
    action(**kwargs)


if __name__ == "__main__":
    main()
