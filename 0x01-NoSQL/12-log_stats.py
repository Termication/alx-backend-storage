#!/usr/bin/env python3
'''Module for analyzing and printing statistics from Nginx request logs stored in MongoDB.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints statistics about Nginx request logs from a MongoDB collection.
    
    The function outputs:
    - Total number of log entries.
    - Count of requests for each HTTP method (GET, POST, PUT, PATCH, DELETE).
    - Count of GET requests to the `/status` path.

    Args:
        nginx_collection: The MongoDB collection object containing Nginx logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    
    # Count GET requests to the `/status` path
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    '''Connects to the MongoDB server and prints Nginx log statistics.
    
    This function connects to a MongoDB instance running on `localhost:27017`,
    accesses the `logs.nginx` collection, and prints log statistics using the
    `print_nginx_request_logs` function.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
