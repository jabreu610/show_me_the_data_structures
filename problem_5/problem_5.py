from hashlib import sha256
import time

TRANSACTION_A = '$399 for a month of quality instruction'
TRANSACTION_B = '$1,000,000 for a drawing of a monkey wearing sunglasses'
TRANSACTION_C = '$35,000 for a self driving electic sedan'


class Block:
    def __init__(self, payload: str, previous_block):
        self.timestamp = time.time()
        self.payload = payload
        self.previous_hash = previous_block.get_hash() if previous_block else None
        self.previous_block: Block | None = previous_block
        self.hash = self.generate_hash()

    def get_hash(self):
        return self.hash

    def get_timestamp_string(self):
        return time.strftime("%x %X", time.localtime(self.timestamp))

    def generate_hash(self):
        sha = sha256()
        sha.update(f"{self.timestamp}{self.payload}".encode())
        return sha.digest()

    def get_previous_block(self):
        return self.previous_block

    def __repr__(self):
        return f"Timestamp: {self.get_timestamp_string()}\nData: {self.payload}\nSHA256 Hash: {self.get_hash()}\nPrevious Hash: {self.get_previous_block().get_hash() if self.get_previous_block() else 'None'}"


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

    def __iter__(self):
        current_block = self.tail
        while current_block:
            yield current_block
            current_block = current_block.get_previous_block()

    def __repr__(self) -> str:
        output = []
        for block in self:
            output.append(str(block) )
        return "\n⬇\n".join(output) +"\n"


def process_transaction():
    bc = Blockchain()
    bc.process_transaction(TRANSACTION_B)
    block_hash = bc.process_transaction(TRANSACTION_A)
    print(bc)
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

    print(bc)
    return True


def get_genesis():
    bc = Blockchain()
    hash_a = bc.process_transaction(TRANSACTION_A)
    bc.process_transaction(TRANSACTION_B)

    print(bc)
    return hash_a == bc.get_genesis_block().get_hash()


if __name__ == "__main__":
    # Note timestamps provided below will not be exact matches as format depends on locale and timestamp is determined at runtime

    print(process_transaction(), "\n\n")
    # Timestamp: 01/15/23 17:17:20
    # Data: $399 for a month of quality instruction
    # SHA256 Hash: b's\xe7-\xf5\xe9X,\xde\xa5/\xcb\xe7\xe4\x87\x10\x84\x96\xe5m\x9a\xa8\x07h!.\x1bg~\xa9\xf0\xbe\x81'
    # Previous Hash: b'\xdb\xfb\xfaFS85\xf3P/t\x8a"@\x92\xbd\x00\xf7\xa7~_\xd9\xd54wQ\xd1\xbe\x9e|\xfc\xda'
    # ⬇
    # Timestamp: 01/15/23 17:17:20
    # Data: $1,000,000 for a drawing of a monkey wearing sunglasses
    # SHA256 Hash: b'\xdb\xfb\xfaFS85\xf3P/t\x8a"@\x92\xbd\x00\xf7\xa7~_\xd9\xd54wQ\xd1\xbe\x9e|\xfc\xda'
    # Previous Hash: None

    # True 
    print(verify_lineage(), "\n\n")
    # Timestamp: 01/15/23 17:17:20
    # Data: $35,000 for a self driving electic sedan
    # SHA256 Hash: b"\xa9\x1d\xd3\x89P\xa5I\x05\x99\xf6\x14k\x04'\xf6\xbc\xa6V\xcb\x977f\xb46\xbav9f\xfd\xa4\x87\x82"
    # Previous Hash: b'\xd07\xe1\xf60\xccN\x85\xae\x00\xa7bdf4"\xa5o\xa2\xe2h\x0bv.f\xdb\n\xc2%\xec\xb3\xec'
    # ⬇
    # Timestamp: 01/15/23 17:17:20
    # Data: $1,000,000 for a drawing of a monkey wearing sunglasses
    # SHA256 Hash: b'\xd07\xe1\xf60\xccN\x85\xae\x00\xa7bdf4"\xa5o\xa2\xe2h\x0bv.f\xdb\n\xc2%\xec\xb3\xec'
    # Previous Hash: b'\xb7\xae\xc1;\xaao\xd0\\\xbb\xfcfZ))#\xfb\x13Y>S\xda\x80\xbbJ\xf8\xaf=\xc0P\xeby\x1f'
    # ⬇
    # Timestamp: 01/15/23 17:17:20
    # Data: $399 for a month of quality instruction
    # SHA256 Hash: b'\xb7\xae\xc1;\xaao\xd0\\\xbb\xfcfZ))#\xfb\x13Y>S\xda\x80\xbbJ\xf8\xaf=\xc0P\xeby\x1f'
    # Previous Hash: None

    # True 
    print(get_genesis(), "\n\n")
    # Timestamp: 01/15/23 17:17:20
    # Data: $1,000,000 for a drawing of a monkey wearing sunglasses
    # SHA256 Hash: b'\xc9\xa7\xb9\xa6\x87S\x9f\xf9\x1f\x91\xb9(n\xa9TO;F9R\x8f/V/\x1eq\x17<\xbf\xf6F\x0e'
    # Previous Hash: b'_\xca\xbf\xb5\xe0\xe8\xad!\xfd\x04\x83?|\x89[r\xc2\xe3\xdaN\xf3\xf0\xd5\x1bc\xfc\xd8t\r\xa1\xf3\xad'
    # ⬇
    # Timestamp: 01/15/23 17:17:20
    # Data: $399 for a month of quality instruction
    # SHA256 Hash: b'_\xca\xbf\xb5\xe0\xe8\xad!\xfd\x04\x83?|\x89[r\xc2\xe3\xdaN\xf3\xf0\xd5\x1bc\xfc\xd8t\r\xa1\xf3\xad'
    # Previous Hash: None

    # True 
