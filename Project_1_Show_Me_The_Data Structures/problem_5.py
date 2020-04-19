import datetime
import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None

    def calc_hash(self, data):
        hash_str = data.encode('utf-8')
        sha = hashlib.sha256()
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        if value is None:
            return

        self.size += 1
        node = self.head

        if node is None:
            block = Block(datetime.datetime.now(), value, None)
            self.head = block
        else:
            while node.next:
                node = node.next
            node.next = Block(datetime.datetime.now(), value, node.hash)

#------------------------------------
# Test Case 1
chain = BlockChain()
chain.append('data for a')
chain.append('data for b')
chain.append('data for c')
chain.append(None)

print(chain.head.data)
# data for a

b = chain.head.next
c = chain.head.next.next
print(b.hash == c.previous_hash)
# True

print(c.data)
# data for c
#-----------------------------------
# Test Case 2
chain = BlockChain()
chain.append('')
chain.append(None)

print(chain.head.data)
# ''

# Test Case 3
chain = BlockChain()
chain.append('value1')
chain.append('value2')
chain.append('value3')
chain.append('value4')
chain.append(None)

print(chain.head.data)
# value1

val2 = chain.head.next
val3 = chain.head.next.next
val4 = chain.head.next.next.next
print(val2.hash == val3.previous_hash)
# True
print(val3.hash == val4.previous_hash)
# True
print(val4.data)
## value4

