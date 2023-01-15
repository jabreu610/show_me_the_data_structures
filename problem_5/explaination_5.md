# Explanation 5

## Rationale
For the Blockchain exercise, I defined a `Blockchain` class than arranges `Blocks` in a singly linked list. THe linked list is tail-first as each `Block` holds a reference the previous block as opposed to the next

## Runtime Analysis
By blockchain implementation has one method that accepts input:
`process_transaction` has a time complexity of `O(n)` and a space complexity of `O(n)`. A quick look at the pseudocode on [Wikipedia](https://en.wikipedia.org/wiki/SHA-2#Pseudocode) seems to indidcate the SHA-256 scales linearly with its inputs byte length (n). The space complexity scales linearly with input size (n) as it is persisted as new block on the Blockchain.
