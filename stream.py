#!/usr/bin/python3

# Script to search for a movie and stream it

from moviesearch import *
from subprocess import call
import sys

if __name__ == "__main__":
    result = search(sys.argv[1])
    call(mpv, result.getStreamURL())


