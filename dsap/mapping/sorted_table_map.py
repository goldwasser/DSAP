from .map_base import MapBase

class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

    #----------------------------- nonpublic behaviors -----------------------------
    def _find_index(self, k):
        """Return index of the leftmost item with key greater than or equal to k.

        Return len(self) if no such item qualifies.

        That is, j will be returned such that:
           all items of slice table[ :j] have key < k
           all items of slice table[j: ] have key >= k
        """
        low = 0
        high = len(self._table) - 1
        while low <= high:
            mid = (low + high) // 2
            if k == self._table[mid]._key:                           # exact match found
                return mid                                           #    at index mid
            elif k < self._table[mid]._key:                          # target is smaller than _table[mid]
                high = mid - 1                                       #    so continue searching left of mid
            else:                                                    # target is larger than _table[mid]
                low = mid + 1                                        #    so continue searching right of mid
        return low                                                   # low = 1+high for unsuccessful search

    #----------------------------- public behaviors -----------------------------
    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self._find_index(k)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self._find_index(k)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v                                # reassign value
        else:
            self._table.insert(j, self._Item(k,v))                   # adds new item

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self._find_index(k)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)                                           # delete item

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum."""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """Return (key,value) pair with maximum key (or None if empty)."""
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k.

        Return None if there does not exist such a key.
        """
        j = self._find_index(k)                                      # j's key >= k
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_gt(self, k):
        """Return (key,value) pair with least key strictly greater than k.

        Return None if there does not exist such a key.
        """
        j = self._find_index(k)                                      # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j += 1                                                   # advanced past exact match
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_le(self, k):
        """Return (key,value) pair with greatest key less than or equal to k.

        Return None if there does not exist such a key.
        """
        j = self._find_index(k)                                      # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            return (self._table[j]._key, self._table[j]._value)      # exact match
        elif j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)  # Note use of j-1
        else:
            return None

    def find_lt(self, k):
        """Return (key,value) pair with greatest key strictly less than k.

        Return None if there does not exist such a key.
        """
        j = self._find_index(k)                                      # j's key >= k
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)  # Note use of j-1
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start)                              # find first result
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1
