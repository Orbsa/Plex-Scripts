#!/usr/bin/python3

# Script to find a movie using a specific genre and stream it

from moviesearch import *
from subprocess import call
import sys
from random import random
import math

if __name__ == "__main__":
    movies = search() if len(sys.argv) < 2 else search(genre=sys.argv[1])
    index= math.floor(random() * len(movies))
    result=movies[index]
    streamURL=result.getStreamURL(videoResolution='1920x1080',maxVideoBitrate=8000)
    call(['mpv',streamURL])

