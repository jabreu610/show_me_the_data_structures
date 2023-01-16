# Explanation 3

## Rationale
For the Data Compression exercise, I leveraged Python's `heapq` module to create a min heap priority queue for generating the Huffman tree. I utilized a depth first search traversal strategy for building the encoding table.

## Runtime Analysis
1. `huffman_encoding` has a time complexity of `O(n log n)` and a space complexity of `O(n)`. In the worst case, the runtime scales linearly with the unique character count (n), iterating through the input 2 times to construct the min heap used for constructing the huffman tree, Contructing the huffman tree itself has a time complexity of log n, where n as previously mentioned is the unique character count of the input. Storage utilization also scales linearly with the input length (n) in the worst case, given the case where a message contains only unique characters.
2. `huffman_decoding` has a time complexity of `O(n)` and a space complexity of `O(n)`. In the worst case, the runtime scales linearly with the encoded message length (n). The space complexity scales linearly with the encoded input message length and the depth of the huffman tree (n) in the worst case.