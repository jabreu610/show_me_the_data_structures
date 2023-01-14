# Explanation 6

## Rationale
For the Union and Intersection of Two Linked Lists exercise, I opted to extend the provided `LinkedList` class by implementing the __iter__ method. This results in much more concise code in the `union` and `intersection` functions

## Runtime Analysis
Both the `union` and `intersection` function share a time complexity of `O(n)` and a space complexity of `O(n)`. The runtime scales linearly with input size as we iterate through both provided inputs once. Memory allocation also scales linearly with the input size in the worst case, ie an empty Linked List as one of the inputs, as we utilize a set for comparison purposes.
 