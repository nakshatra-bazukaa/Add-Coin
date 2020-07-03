# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:48:08 2020

@author: Nakshatra Gupta
"""
from MyBlockchain.Blockchain import Blockchain
from flask import Flask, jsonify

# Creating a web app
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()

# Mining a new Block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    prev_block = blockchain.get_prev_block()
    prev_proof = prev_block['proof']
    proof = blockchain.proof_of_work(prev_proof)
    prev_hash = blockchain.hash(prev_block)
    block = blockchain.create_block(proof, prev_hash)
    response = {'message' : 'Congraluations, you just mined a block!',
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof' : block['proof'],
                'prev_hash' : block['prev_hash']}
    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain' : blockchain.chain,
                'length' : len(blockchain.chain)}
    return jsonify(response), 200

# Checking validity of chain
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'Message' : 'The Blockchain is valid.'}
    else:
        response = {'Message' : 'The Blockchain is not valid.'}
    return jsonify(response), 200

# Running the app
app.run(host = '0.0.0.0', port = 5000)
    