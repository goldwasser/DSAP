"""Provides a simple function fibonacci() that generates the infinite Fibonacci series."""

def fibonacci():
    """Generate the infinite Fibonacci series, starting with 0, 1, 1, 2, 3, 5, ..."""
    a = 0
    b = 1
    while True:               # keep going...
        yield a               # report value, a, during this pass
        future = a + b
        a = b                 # this will be next value reported
        b = future            # and subsequently this
