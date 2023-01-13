from hashlib import sha256
import time

TRANSACTION_A = '$399 for a month of quality instruction'
TRANSACTION_B = '$1,000,000 for a drawing of a monkey wearing sunglasses'
TRANSACTION_C = '$35,000 for a self driving electic sedan'


class Block:
    def __init__(self, payload: str, previous_block):
        self.timestamp = time.time_ns()
        self.payload = payload
        self.previous_hash = previous_block.get_hash() if previous_block else None
        self.previous_block = previous_block
        self.hash = self.generate_hash()

    def get_hash(self):
        return self.hash

    def generate_hash(self):
        sha = sha256()
        sha.update(f"{self.timestamp}{self.payload}".encode())
        return sha.digest()

    def get_previous_block(self):
        return self.previous_block


class Blockchain:
    def __init__(self):
        self.genesis = None
        self.tail = None

    def process_transaction(self, payload):
        block = Block(payload, self.tail)
        if not self.genesis and not self.tail:
            self.genesis = block
        self.tail = block
        return block.get_hash()

    def get_latest_block(self):
        return self.tail

    def get_genesis_block(self):
        return self.genesis


def process_transaction():
    bc = Blockchain()
    block_hash = bc.process_transaction(TRANSACTION_A)
    return bc.get_latest_block().get_hash() == block_hash


def verify_lineage():
    bc = Blockchain()
    hash_a = bc.process_transaction(TRANSACTION_A)
    hash_b = bc.process_transaction(TRANSACTION_B)
    hash_c = bc.process_transaction(TRANSACTION_C)

    current_block = bc.get_latest_block()

    for hash in [hash_c, hash_b, hash_a]:
        if hash != current_block.get_hash():
            return False
        current_block = current_block.get_previous_block()

    return True


def get_genesis():
    bc = Blockchain()
    hash_a = bc.process_transaction(TRANSACTION_A)
    bc.process_transaction(TRANSACTION_B)

    return hash_a == bc.get_genesis_block().get_hash()


if __name__ == "__main__":
    print(process_transaction())
    # True
    print(verify_lineage())
    # True
    print(get_genesis())
    # True
