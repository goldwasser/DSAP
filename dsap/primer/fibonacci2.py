"""Provides a simple function fibonacci() that generates the infinite Fibonacci series."""

def fibonacci():
    """Generate the infinite Fibonacci series, starting with 0, 1, 1, 2, 3, 5, ..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
