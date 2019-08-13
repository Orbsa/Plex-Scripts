#!/usr/bin/python3

# Script to search for a movie and stream it

from moviesearch import *
from subprocess import call
import sys

if __name__ == "__main__":
    result= console_search(sys.argv[1]) if len(sys.argv) < 3 else console_search(sys.argv[1],sys.argv[2])
    if result is not None:
        streamURL=result.getStreamURL(videoResolution='1920x1080',maxVideoBitrate=8000)
        call(['mpv',streamURL])
        #print(streamURL)

