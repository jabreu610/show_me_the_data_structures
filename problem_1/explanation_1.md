# Explanation 1

## Rationale
For the LRU cache exercise, I decided to leverage Python's [OrderedDict](https://docs.python.org/3.11/library/collections.html#collections.OrderedDict). OrderedDict instances keep track of insertion order and provide two helpful methods when implementing a simple LRU cache:

1. popitem returns and removes a key value pair, passing `False` as the argument will ensure entities are popped from left
2. move_to_end accepts an existing key as an argument and moves it, and its paired value, to the right most position

## Runtime Analysis

1. LRU_Cache's `get` method has a time complexity of `O(1)` and space complexity of `O(1)`. Retrieving a value by key from an OrderedDict is a constant time operation. No additional storage is allocated in the execution of this method.
2. LRU_Cache's `set` method has a time complextity of `O(1)` and a space complexity of `O(n)`. Setting a value on an OrderedDict is a constant time operation. In the event the cache is full, removing the oldest accessed entry is also a constant time operation. Memory utilization scales linearly with the input value being set as it is persisted. 

