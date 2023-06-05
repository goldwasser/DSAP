"""Provides the AdaptableHeapPriorityQueue class."""

from .heap_priority_queue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    #------------------------------ nested Locator class ------------------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an item within the priority queue."""
        __slots__ = '_index'                    # add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k,v)
            self._index = j

    #------------------------------ nonpublic behaviors ------------------------------
    # override swap to record new indices
    def _swap(self, i, j):
        super()._swap(i,j)                      # perform the swap
        self._data[i]._index = i                # reset locator index (post-swap)
        self._data[j]._index = j                # reset locator index (post-swap)

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def _validate(self, loc):
        if not isinstance(loc,self.Locator):                   # ensure loc is a Locator
            raise TypeError('Invalid locator')
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):  # ensure locator matches this PQ
            raise ValueError('Invalid locator')
        return j                                               # return locator's index in the list

    #------------------------------ public behaviors ------------------------------
    def add(self, key, value):
        """Add a key-value pair and return a Locator for the new item."""
        token = self.Locator(key, value, len(self._data)) # initialize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newvalue):
        """Update the key and value for the item identified by Locator loc."""
        j = self._validate(loc)
        loc._key = newkey
        loc._value = newvalue
        self._bubble(j)                         # restore heap property

    def remove(self, loc):
        """Remove and return the (k,v) pair identified by Locator loc."""
        j = self._validate(loc)
        if j == len(self) - 1:                  # item at last position
            self._data.pop()                    # just remove it
        else:
            self._swap(j, len(self)-1)          # swap item to the last position
            self._data.pop()                    # remove it from the list
            self._bubble(j)                     # fix item displaced by the swap
        return (loc._key, loc._value)
