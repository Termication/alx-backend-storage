#!/usr/bin/env python3
'''Module for listing all documents in a MongoDB collection.
'''


def list_all(mongo_collection):
    '''Returns a list of all documents in the MongoDB collection'''
    return [doc for doc in mongo_collection.find()]
