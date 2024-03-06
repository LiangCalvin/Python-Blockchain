import datetime
import json
import hashlib
from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        self.block = [] #list of block
        self.create_block(nonce=1,previous_hash="0")
     
    def create_block(self,nonce,previous_hash,):
        block={
            "id":len(self.block)+1,
            "timestamp":str(datetime.datetime.now()),
            "nonce":nonce,
            "previous_hash":previous_hash,
            # "hash":""
        }
        # block['hash'] = self.calculate_hash(block)  
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
            # print ("Previous nonce=",previous_nonce)
            if hash_operation[:4] == "0000":
                check_nonce = True
            else:
                new_nonce += 1 
        return new_nonce 
    
    def is_valid_block(self, block,previous_block):
        if block['previous_hash'] != self.calculate_hash(previous_block):
            return False
        hash_operation = hashlib.sha256(str(block['nonce']**2 - previous_block['nonce']**2).encode()).hexdigest()
        if hash_operation[:4] != "0000":
            return False
        return True
    
    def is_valid_chain(self):
        for i in range(1, len(self.block)):
            if not self.is_valid_block(self.block[i], self.block[i-1]):
                return False
        return True

blockchain = Blockchain()

#Create Flask app web server
app = Flask(__name__)

#routing
@app.route('/')
def hello():
    return "<p>Hello Blockchain</p>"

@app.route('/chain', methods=['GET'])
def get_chain():
    chain = blockchain.block
    for block in chain:
        block['hash'] = blockchain.calculate_hash(block)
    response = {
        'chain': chain,
        'length': len(chain)
    }
    return jsonify(response),200

@app.route('/mine',methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_nonce = previous_block['nonce']
    new_nonce = blockchain.proof_of_work(previous_nonce)
    previous_hash = blockchain.calculate_hash(previous_block)
    block = blockchain.create_block(new_nonce, previous_hash)
    response = {
        'message':"Successfully mining block",
        'index':block["id"],
        'timestamp':block["timestamp"],
        'nonce':block["nonce"],
        'previous_hash':block["previous_hash"]
    }
    return jsonify(response),200

# @app.route('/transaction/new', methods=['POST'])
# def new_transaction():
#     data = request.get_json()
#     required_fields = ['sender', 'recipient', 'amount']
#     if not all(field in data for field in required_fields):
#         return 'Missing fields', 400
#     index = blockchain.create_block(data['nonce'], data['previous_hash'])
#     return jsonify(index), 201

@app.route('/chain/validity', methods=['GET'])
def check_chain_validity():
    try:
        is_valid = blockchain.is_valid_chain()
        response = {'is_valid':is_valid}
        return jsonify(response),200
    except Exception as e:
        return jsonify({'error':str(e)}),500

first_block = blockchain.block
print("First block =",first_block)

previous_block = blockchain.get_previous_block()
print("Previous block =",previous_block)

print("Encode block to JSON =",blockchain.encode_block_to_json(first_block))
print("Hash sha256 =",blockchain.calculate_hash(blockchain.block[0]))
print("POW =",blockchain.proof_of_work)

#run server
if __name__ == "__main__":
    app.run()