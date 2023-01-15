# Explanation 3

## Rationale
For the Data Compression exercise, I leveraged Python's `heapq` module to create a min heap priority queue for generating the Huffman tree. I utilized a depth first search traversal strategy for building the encoding table.

## Runtime Analysis
1. `huffman_encoding` has a time complexity of `O(n)` and a space complexity of `O(n)`. In the worst case, the runtime scales linearly with the input message length (n), iterating tthrough the input 3 times. Storage utilization also scales linearly with the input length (n) in the worst case, given the case where a message contains only unique characters.
2. `huffman_decoding` has a time complexity of `O(n)` and a space complexity of `O(n)`. In the worst case, the runtime scales linearly with the encoded message length (n). The space complexity scales linearly with the encoded input message length and the depth of the huffman tree (n) in the worst case.