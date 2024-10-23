#!/usr/bin/env python3
'''Module for analyzing and printing Nginx request log statistics stored in MongoDB.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints statistics about Nginx request logs from a MongoDB collection.
    
    The function outputs:
    - Total number of log entries.
    - Count of requests for each HTTP method (GET, POST, PUT, PATCH, DELETE).
    - Count of GET requests made to the `/status` path.

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


def print_top_ips(server_collection):
    '''Prints statistics about the top 10 IPs making requests in a MongoDB collection.
    
    This function aggregates the logs to count the number of requests made by each unique IP,
    then prints the top 10 IPs with the most requests, sorted in descending order.

    Args:
        server_collection: The MongoDB collection object containing Nginx logs.
    '''
    print('IPs:')
    request_logs = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))


def run():
    '''Connects to the MongoDB server and prints Nginx log statistics.
    
    This function connects to a MongoDB instance running on `localhost:27017`, 
    accesses the `logs.nginx` collection, and prints log statistics using the
    `print_nginx_request_logs` and `print_top_ips` functions.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)
    print_top_ips(client.logs.nginx)


if __name__ == '__main__':
    run()
