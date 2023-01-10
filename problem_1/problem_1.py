from collections import OrderedDict


class LRU_Cache:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = OrderedDict()

    def __repr__(self) -> str:
        return self.data.__repr__()

    def __cache_is_full(self):
        return len(self.data) >= self.capacity

    def __used(self, key):
        self.data.move_to_end(key)

    def get(self, key):
        if key in self.data:
            self.__used(key)
            return self.data[key]
        return -1

    def set(self, key, value):
        if key not in self.data and self.__cache_is_full():
            self.data.popitem(False)
        self.data[key] = value
        self.__used(key)


def eviction():
    """
    Test Case 1
    Tests proper eviction of cached data when adding entries at capacity
    """
    cache = LRU_Cache(5)
    for entry in range(1, 6):
        cache.set(entry, entry)
    cache.get(1)
    cache.get(3)
    cache.set(6, 6)
    cache.set(7, 7)
    return cache


def cache_miss():
    """
    Test Case 2
    Tests retrieving a value from an empty cache ie cache miss
    """
    cache = LRU_Cache(5)
    return cache.get(1)


def cache_key_collision():
    """
    Test Case 3
    Tests setting values to existing keys, expected behavior: value should be overwritten and cache entry should be considered "used"
    """
    cache = LRU_Cache(5)
    for entry in range(1, 6):
        cache.set(entry, entry)
    cache.set(1, 'I was overwritten')
    return cache


print(eviction())
# OrderedDict([(5, 5), (1, 1), (3, 3), (6, 6), (7, 7)])
print(cache_miss())
# -1
print(cache_key_collision())
# OrderedDict([(2, 2), (3, 3), (4, 4), (5, 5), (1, 'I was overwritten')])
