#!/usr/bin/python3

# Script to search server (setup in connect.py) for a movie
# Usage: search(query, index)
# If no index is provided, it will provide a list of results
# If index is provided and found in the list, it will return the single result

from connect import *

def search(query, index=None):
    if index is not None: # Ensure index is of type Int
        try:
            index = int(index)
        except:
            import sys
            print ('Index provided: \"' + str(index) + '\" is not an integer')
            sys.exit()
    movies = plex.library.section('Movies')
    results = movies.search(query)
    if index is None:
        return results
    try:
        return results[index]
    except:
        return None

def console_search(query, index=None):
    if index is not None:
        results = search(query, index)
        if results is not None:
            return results
        else:
            print("No Match for '%s' With index: %s" % (query, index))
            return None
    else:
        results = search(query)
        if results:
            if len(results) < 2:
                return results[0]
            else:
                for i, movie in enumerate(results):
                    print(str(i) + ": " + movie.title)
        else:
            print("No Match for " + query)
        return None

if __name__ == "__main__":
    import sys
    from pprint import pprint
    if len(sys.argv) > 2:
        result = console_search(sys.argv[1],sys.argv[2])
    else:
        result = console_search(sys.argv[1]) # Pretty Print out dictionary if called from main and match found
    if result is not None:
        pprint(vars(result))
