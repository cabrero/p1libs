#!/usr/bin/env python3

import sys

from p1 import e2e


def dump_desktop():
    desktop = e2e.Atspi.get_desktop(0)
    for _, app in e2e.children(desktop):
        print(app.get_name())

        
def dump_app(name):
    desktop = e2e.Atspi.get_desktop(0)
    app = next((app for _, app in e2e.children(desktop) if app.get_name() == name), None)
    if not app:
        print(f"App {name} not found in desktop")
        print(f"Try running {__file__} without args to get the list of apps")
        sys.exit(0)
    for path, node in e2e.tree(app):
        interfaces = node.get_interfaces()
        if 'Action' in interfaces:
            n = node.get_n_actions()
        else:
            n = 0
        actions = [node.get_action_name(i) for i in range(0, n)]
        if actions:
            actions_s = f" actions: {actions}"
        else:
            actions_s = ""
        print("  "*len(path),
              f"{path} {node.get_role_name()}({node.get_name()})"
              f" {actions_s}"
              f" ifaces: {interfaces}",
              sep= "")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        dump_desktop()
    else:
        dump_app(sys.argv[1])
