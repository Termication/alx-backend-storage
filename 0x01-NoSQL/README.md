# Introduction to NoSQL and MongoDB
#### Table of Contents

    What NoSQL Means
    Difference Between SQL and NoSQL
    What is ACID
    What is Document Storage
    Types of NoSQL Databases
    Benefits of NoSQL Databases
    Querying Information from a NoSQL Database
    Inserting, Updating, and Deleting Information from a NoSQL Database
    How to Use MongoDB

## What NoSQL Means

NoSQL stands for "Not Only SQL," and refers to a broad class of database systems that do not rely on traditional relational database structures (like tables) or SQL queries. These databases are designed to handle unstructured or semi-structured data, provide flexibility in data storage, and scale horizontally.

## Difference Between SQL and NoSQL

| Feature             | SQL (Relational) Databases                      | NoSQL (Non-Relational) Databases                     |
|---------------------|-------------------------------------------------|------------------------------------------------------|
| **Data Model**       | Tables with fixed schemas                       | Flexible schemas (e.g., documents, key-value pairs)   |
| **Query Language**   | Structured Query Language (SQL)                 | Query methods vary (e.g., MongoDB queries)            |
| **Schema**           | Predefined schema, strict relationships         | Dynamic, flexible schema                             |
| **Scaling**          | Scales vertically (adding more powerful hardware) | Scales horizontally (adding more servers)            |
| **ACID Compliance**  | Strong ACID properties                          | Some NoSQL databases provide eventual consistency     |
| **Data Type**        | Structured, well-defined                       | Unstructured, semi-structured                        |

## What is ACID?

ACID stands for Atomicity, Consistency, Isolation, and Durability. These are the four key properties that ensure reliable processing of database transactions in SQL databases:

    Atomicity: Ensures all parts of a transaction are completed successfully, or none are applied.
    Consistency: Ensures that a transaction brings the database from one valid state to another.
    Isolation: Ensures that the execution of one transaction does not affect others.
    Durability: Ensures that once a transaction is committed, it remains permanent, even in case of a system failure.

Many NoSQL databases compromise some ACID properties (especially consistency and isolation) to allow greater flexibility and scalability.
## What is Document Storage?

In a document store, data is stored as documents, typically in formats like JSON, BSON, or XML. Each document is a self-contained unit that holds all the necessary information, and fields may vary from document to document.

### Example document (in JSON):

```json

{
    "name": "Alice",
    "age": 30,
    "address": {
        "city": "New York",
        "zipcode": "10001"
    }
}
```
Document-based databases like MongoDB are designed for scenarios where data relationships are less rigid, and the structure of stored data is flexible.
#### Types of NoSQL Databases

    Document Stores: Store data as documents (e.g., MongoDB, CouchDB).
    Key-Value Stores: Store data as key-value pairs (e.g., Redis, DynamoDB).
    Column Family Stores: Store data in columns rather than rows (e.g., Cassandra, HBase).
    Graph Databases: Store data as nodes and relationships between them (e.g., Neo4j).

#### Benefits of NoSQL Databases

    Scalability: Designed to scale horizontally, making it easy to distribute across multiple servers.
    Flexibility: Allows for dynamic, schema-less data models, making it ideal for unstructured or semi-structured data.
    Performance: Optimized for fast reads and writes, making it suitable for real-time applications.
    Big Data Handling: Well-suited for handling large datasets and high-throughput applications.
    Distributed Architecture: NoSQL databases are often designed for high availability and fault tolerance.

#### Querying Information from a NoSQL Database

NoSQL databases have different ways to query data based on the database type. For MongoDB (a document store), the queries are based on document fields, and use a JSON-like syntax.

MongoDB Example: Find all documents where age is 30.

```bash

db.collection.find({ age: 30 })
```
MongoDB Example: Find documents with a specific nested field.

```bash

db.collection.find({ "address.city": "New York" })
```
Inserting, Updating, and Deleting Information from a NoSQL Database
Inserting Data

In MongoDB, data is inserted as documents into a collection.

```bash

db.collection.insert({
    name: "Alice",
    age: 30,
    address: {
        city: "New York",
        zipcode: "10001"
    }
})
```
##### Updating Data

MongoDB allows updating specific fields in a document.

```bash

db.collection.update(
    { name: "Alice" },
    { $set: { age: 31 } }
)
```
#### Deleting Data

You can delete documents based on a condition.

```bash

db.collection.remove({ name: "Alice" })
```
#### How to Use MongoDB

MongoDB is one of the most popular NoSQL databases and is easy to use with various platforms. Here are the basic steps to get started:
### 1. Installation

You can install MongoDB by following the instructions on the official MongoDB website.
### 2. Running MongoDB

After installation, you can start MongoDB using:

```bash

mongod
```
This starts the MongoDB server.
### 3. MongoDB Shell

To interact with the database, open the MongoDB shell by typing:

```bash

mongo
```
### 4. Basic Operations

    Create a database: MongoDB automatically creates a database when you insert a document into a collection.

```bash

use myDatabase
```
### Create a collection and insert a document:

```bash

db.myCollection.insert({ name: "John", age: 25 })
```
### Query the collection:

```bash

db.myCollection.find()
```
### Update a document:

```bash

db.myCollection.update({ name: "John" }, { $set: { age: 26 } })
```
### Delete a document:

```bash

db.myCollection.remove({ name: "John" })
```
By following these steps, you will be able to understand the fundamental concepts of NoSQL databases and how to use MongoDB for basic data operations.
