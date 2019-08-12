#!/usr/bin/python3

# Script to search for a movie and stream it

from moviesearch import *
from subprocess import call
import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        result = console_search(sys.argv[1],sys.argv[2])
        if result is not None:
            call(['mpv', result.getStreamURL()])
    else:
        result = console_search(sys.argv[1])
        if result is not None:
            call(['mpv', result.getStreamURL()])

