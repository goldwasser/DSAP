"""
Provides an OurRange class that mimics the built-in range class.
"""

class OurRange:
    """A class that mimics the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize an OurRange instance.

        Semantics are similar to the built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:                        # special case of OurRange(n)
            start, stop = 0, start              # should be treated as if OurRange(0,n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - step/abs(step)) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)                      # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step
