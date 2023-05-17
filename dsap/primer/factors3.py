"""Provides a simple function factors(n) that returns a generator of factors of integer."""

def factors(n):               # generator that computes factors
    """Generate the factors of integer n."""
    k = 1
    while k * k < n:          # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:            # special case if n is perfect square
        yield k
