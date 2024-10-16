-- Script to create the 'users' table with the following fields:
-- id: An auto-incremented primary key
-- email: A unique, non-nullable field for storing user emails
-- name: An optional field for storing user names

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
