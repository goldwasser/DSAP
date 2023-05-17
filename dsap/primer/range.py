"""An incomplete implementation of a range(start,stop,step) function demonstrating use of default parameters."""

def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    ...
