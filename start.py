#!/usr/bin/python3

import togglTimer
import sys

args = sys.argv
if len(args) > 1:
    project = args[1]
    togglTimer.start(project)
else:
    print("not enough arguments to start project.")
    print("example: python start.py japanese")

