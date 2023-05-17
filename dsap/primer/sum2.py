"""Provides a simple function sum(values) to compute the sum of a sequence of numbers."""

def sum(values):
    """Return the sum of the sequence of numeric values."""
    total = 0
    for v in values:
        total = total + v
    return total
