import datetime
import json
import hashlib
from flask import Flask

class Blockchain:
    def __init__(self):
        self.block = [] #list of block
        self.create_block(nonce=1,previous_hash="0")
     
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

    def proof_of_work(self,previous_nonce):
        #requirement: target hash (nonce) = first 4 digit == 0000
        new_nonce = 1
        check_nonce = False
        #mathematics algorithym
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()    
            print ("Previous nonce=",previous_nonce)
            if hash_operation[:4] == "0000":
                check_nonce = True
            else:
                new_nonce += 1 
        return new_nonce 

#web server
app = Flask(__name__)
#routing
@app.route('/')
def hello():
    return "<p>hello</p>"
#run server
if __name__ == "__main__":
    app.run()

blockchain = Blockchain()

first_block = blockchain.block
print("First block =",first_block)

previous_block = blockchain.get_previous_block()
print("Previous block =",previous_block)

print("Encode block to JSON =",blockchain.encode_block_to_json(first_block))
print("Hash sha256 =",blockchain.calculate_hash(blockchain.block[0]))
print("POW =",blockchain.proof_of_work)