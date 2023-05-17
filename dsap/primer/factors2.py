"""Provides a simple function factors(n) that returns a generator of factors of integer."""

def factors(n):                 # generator that computes factors
    """Generate the factors of integer n."""
    for k in range(1,n+1):
        if n % k == 0:          # divides evenly, thus k is a factor
            yield k             # yield this factor as next result
