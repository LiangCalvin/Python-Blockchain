import datetime
import json
import hashlib

class Blockchain:
    def __init__(self):
        self.block = [] #list of block
        self.create_block(nonce=1,previous_hash="0")
        self.create_block(nonce=23,previous_hash="230")

        
    def create_block(self,nonce,previous_hash,):
        block={
            "id":len(self.block)+1,
            "timestamp":str(datetime.datetime.now()),
            "nonce":nonce,
            "previous_hash":previous_hash
        }
        self.block.append(block)
        return block
    
    def get_previous_block(self):
        return self.block[-1]
    
    def encode_block_to_json(self,block): #block hash
        encode_block = json.dumps(block,sort_keys=True).encode()
        return encode_block
    
    def calculate_hash(self,block): #block hash
        encode_block = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encode_block).hexdigest() #base16

blockchain = Blockchain()
first_block = blockchain.block
print("First block =",first_block)

previous_block = blockchain.get_previous_block()
print("Previous block =",previous_block)

print("Encode block to JSON =",blockchain.encode_block_to_json(first_block))
print("Hash sha256 =",blockchain.calculate_hash(blockchain.block[0]))