import datetime
import json
import hashlib
from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        self.block = [] #list of block
        self.create_block(nonce=1,previous_hash="0")
     
    def create_block(self,nonce,previous_hash,transactions=None):
        block={
            "id":len(self.block)+1,
            "timestamp":str(datetime.datetime.now()),
            "nonce":nonce,
            "previous_hash":previous_hash,
            "transactions": transactions or []
        }
        self.block.append(block)
        block_hash = self.calculate_hash(block)
        print(f"Hash of block {block['id']}: {block_hash}")
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
            if hash_operation[:4] == "0000":
                check_nonce = True
            else:
                new_nonce += 1 
        return new_nonce

    def is_valid_chain(self,block):
        previous_block = block[0]
        block_index = 1
        while block_index < len(block):
            current_block = block[block_index]
            if current_block["previous_hash"] != self.calculate_hash(previous_block):
                return False
            previous_nonce = previous_block["nonce"]
            nonce = current_block["nonce"]
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != "0000":
                return False
            previous_block = current_block
            block_index += 1
        return True

class Transaction:
    def __init__(self, sender, recipient, amount, timestamp):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": str(self.timestamp)
        }


blockchain = Blockchain()

#Create Flask app web server
app = Flask(__name__)

#routing
@app.route('/')
def hello():
    return "<p>Hello Blockchain</p>"

# @app.route('/chain', methods=['GET'])
# def get_chain():
#     chain = blockchain.block
#     response = {
#         'chain': chain,
#         'length': len(chain)
#     }
#     return jsonify(response),200
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_with_hashes = []
    for block in blockchain.block:
        block_with_hash = block.copy()
        block_with_hash["hash"] = blockchain.calculate_hash(block)
        chain_with_hashes.append(block_with_hash)

    response = {
        'chain': chain_with_hashes,
        'length': len(chain_with_hashes)
    }
    return jsonify(response), 200

@app.route('/mine',methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_nonce = previous_block['nonce']
    new_nonce = blockchain.proof_of_work(previous_nonce)
    previous_hash = blockchain.calculate_hash(previous_block)
    
    transaction = {
        'sender': "sender_address",
        'recipient': "recipient_address",
        'amount': 10.0,
        'timestamp': str(datetime.datetime.now())
    }

    block = blockchain.create_block(new_nonce, previous_hash, transactions=[transaction])
    block_hash = blockchain.calculate_hash(block)  # Calculate hash of the mined block

    response = {
        'message':"Successfully mining block",
        'id':block["id"],
        'timestamp':block["timestamp"],
        'nonce':block["nonce"],
        'previous_hash':block["previous_hash"],
        'block_hash': block_hash  
    }
    return jsonify(response),200

@app.route('/chain/validity', methods=['GET'])
def check_chain_validity():
    try:
        is_valid = blockchain.is_valid_chain(blockchain.block)
        response = {'is_valid':is_valid}
        return jsonify(response),200
    except Exception as e:
        return jsonify({'error':str(e)}),500
    
    # is_valid = blockchain.is_chain_valid(blockchain.block)
    # if is_valid:
    #     response = {"message":"Blockchain valid"}
    # else:
    #     response = {"message":"Blockchain invalid"}
    # return jsonify(response), 200
    

first_block = blockchain.block
print(f"First block =",first_block)

previous_block = blockchain.get_previous_block()
print(f"Previous block =",previous_block)

# print("Encode block to JSON =",blockchain.encode_block_to_json(first_block))

print(f"Hash block 1 =",blockchain.calculate_hash(blockchain.block[0]))
# print("POW =",blockchain.proof_of_work)

#run server
if __name__ == "__main__":
    app.run()