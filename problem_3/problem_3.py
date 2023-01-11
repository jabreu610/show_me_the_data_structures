import sys
from collections import Counter
from heapq import heapify, heappop, heappush

MESSAGE = "AAAAAAABBBCCCCCCCDDEEEEEE"
ENCODED = "1010101010101000100100111111111111111000000010101010101"

LONG_MESSAGE = "iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis urna id volutpat lacus laoreet non curabitur gravida arcu ac tortor dignissim"
DECODED_LONG_MESSAGE = "0010000100101001010010110110000101111010000111000101111011110110000101010110001110010111000011011110000101010001100001001100111110100101100100001111001001011100100111111110111101111111001111111110100001010011011110000101111000111101111101100001111001100110001011110100111010001110000010001001010111010110000111001100110001101111000011101100010111101110010100101010100011011110001000010000101010010110001110111011111101111111001001110101110001110111110110100110110001000010010100101001011011010100111111000001100011001111010010011111010110101011111101000101111001010000100101001101100101000111110111100010001011110111001111111100110010010100111000111100100110111010011111010010101110001001000011001100011000001110100101011000001001101011111110111101111111011111010011001100101111000010110011000111101"


class Node:
    def __init__(self, value, frequency, left=None, right=None):
        self.value = value
        self.frequency: int = frequency
        self.left: Node | None = left
        self.right = right

    def get_value(self):
        return self.value

    def get_label(self):
        return self.value if self.value else self.frequency

    def is_leaf_node(self):
        return self.left == None and self.right == None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __repr__(self) -> str:
        left = self.left.get_label() if self.left else None
        right = self.right.get_label() if self.right else None
        return f"Node(value={self.value}, frequency={self.frequency}, left={left} right={right})"


def generate_cipher_dfs(node: Node, path=''):
    if node.is_leaf_node():
        return [(node.get_label(), path)]

    left_leaves = generate_cipher_dfs(node.left, path + '0') if node.left else [None]
    right_leaves = generate_cipher_dfs(node.right, path + '1') if node.right else [None]

    return [x for x in left_leaves + right_leaves if x]


def huffman_encoding(data):
    if len(data) == 0:
        return '', None
    # Create a list of tuples representing (character frequency, index, Node); the index serves as a tiebreaker value
    # for comparisons made while maintaining the min heap
    character_heap = [(count[1], index, Node(count[0], count[1]))
                      for index, count in enumerate(Counter(data).items())]
    heapify(character_heap)

    while len(character_heap) > 1:
        left_freq, _, left = heappop(character_heap)
        right_freq, tiebreaker_index, right = heappop(character_heap)
        total_frequency = left_freq + right_freq
        internal_node = Node(None, total_frequency, left, right)
        heappush(character_heap, (total_frequency,
                 tiebreaker_index, internal_node))

    _, _, tree = character_heap[0]
    cipher = dict(generate_cipher_dfs(tree))

    encoded = ''
    for char in data:
        encoded += cipher[char]

    return encoded, tree


def huffman_decoding(data, tree: Node):
    decoded = ''
    head = current_node = tree
    for bit in data:
        current_node = current_node.get_left() if bit == '0' else current_node.get_right()

        if current_node.is_leaf_node():
            decoded += current_node.get_value()
            current_node = head

    return decoded


def huffman_encode_decode(message, expected):
    print("The size of the data is: {}".format(
        sys.getsizeof(message)))
    print("The content of the data is: {}\n".format(message))

    encoded_data, tree = huffman_encoding(message)

    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    return expected == encoded_data


def empty_message():
    encoded, tree = huffman_encoding('')
    decoded = huffman_decoding(encoded, tree)
    return encoded == decoded


def large_message():
    return huffman_encode_decode(LONG_MESSAGE, DECODED_LONG_MESSAGE)


if __name__ == "__main__":
    print(huffman_encode_decode(MESSAGE, ENCODED))
    # The size of the data is: 74
    # The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE

    # The size of the encoded data is: 32
    # The content of the encoded data is: 1010101010101000100100111111111111111000000010101010101

    # The size of the decoded data is: 74
    # The content of the encoded data is: AAAAAAABBBCCCCCCCDDEEEEEE

    # True
    print(empty_message())
    # True
    print(large_message())
    # The size of the data is: 250
    # The content of the data is: iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis urna id volutpat lacus laoreet non curabitur gravida arcu ac tortor dignissim

    # The size of the encoded data is: 132
    # The content of the encoded data is: 0010000100101001010010110110000101111010000111000101111011110110000101010110001110010111000011011110000101010001100001001100111110100101100100001111001001011100100111111110111101111111001111111110100001010011011110000101111000111101111101100001111001100110001011110100111010001110000010001001010111010110000111001100110001101111000011101100010111101110010100101010100011011110001000010000101010010110001110111011111101111111001001110101110001110111110110100110110001000010010100101001011011010100111111000001100011001111010010011111010110101011111101000101111001010000100101001101100101000111110111100010001011110111001111111100110010010100111000111100100110111010011111010010101110001001000011001100011000001110100101011000001001101011111110111101111111011111010011001100101111000010110011000111101

    # The size of the decoded data is: 250
    # The content of the encoded data is: iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis urna id volutpat lacus laoreet non curabitur gravida arcu ac tortor dignissim
    
    # True
