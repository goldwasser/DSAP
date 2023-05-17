"""Provides a simple scale(data,factor) function."""

def scale(data, factor):
    """Update the values of data by multiplying each by the given factor."""
    for j in range(len(data)):
        data[j] *= factor
