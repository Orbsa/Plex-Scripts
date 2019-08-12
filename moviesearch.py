#!/usr/bin/python3

# Script to search server (setup in connect.py) for a movie
# Usage: search(query, index)
# If no index is provided, it will provide a list of results
# If index is provided and found in the list, it will return the single result

from connect import *

def search(query, index=None):
    movies = plex.library.section('Movies')
    results = movies.search(query)
    print(index)
    if index is None:
        return results
    try:
        return results[index]
    except:
        return None;

if __name__ == "__main__":
    # Only import sys if running from shell
    import sys
    from pprint import pprint
    if len(sys.argv) > 2:
        results = search(sys.argv[1], int(sys.argv[2]))
        if results is not None:
            pprint(vars(results))
        else:
            print("No Match for '%s' With index: %s" % (sys.argv[1], sys.argv[2]))
    else:
        results = search(sys.argv[1])
        if results:
            if len(results) < 2:
                pprint(vars(results[0]))
            else:
                for i, movie in enumerate(results):
                    print(str(i) + ": " + movie.title)
        else:
            print("No Match for " + sys.argv[1])

