#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE DATABASE mydb;
    GRANT ALL PRIVILEGES ON DATABASE mydb TO postgres;
    \c mydb;
    CREATE TABLE PUBLIC.PRODUCT (
        id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    );
    CREATE TABLE PUBLIC.USER (
        id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL
    );
    CREATE TABLE PUBLIC.REVIEW (
        id INT PRIMARY KEY NOT NULL,
        review TEXT NOT NULL,
        rating REAL NOT NULL,
        user_id INT NOT NULL REFERENCES PUBLIC.USER(id),
        product_id INT NOT NULL REFERENCES PUBLIC.PRODUCT(id)
    );
    CREATE UNIQUE INDEX uniq_idx ON PUBLIC.REVIEW (user_id, product_id);
    INSERT INTO PUBLIC.USER VALUES (1, 'ashu');
    INSERT INTO PUBLIC.USER VALUES (2, 'nitin');
    INSERT INTO PUBLIC.USER VALUES (3, 'abhishek');
    INSERT INTO PUBLIC.USER VALUES (4, 'sachin');
    INSERT INTO PUBLIC.USER VALUES (5, 'arnab');
    INSERT INTO PUBLIC.PRODUCT VALUES (1, 'Laptop', 'Dell inspiron 15R');
    INSERT INTO PUBLIC.PRODUCT VALUES (2, 'Mobile', 'iPhone SE 2020');
    INSERT INTO PUBLIC.PRODUCT VALUES (3, 'Playstation', 'PS5');
    INSERT INTO PUBLIC.PRODUCT VALUES (4, 'Guitar', 'Gibson guitar');
    INSERT INTO PUBLIC.PRODUCT VALUES (5, 'Piano', '58 keys Casio keyboard');
    INSERT INTO PUBLIC.REVIEW VALUES (1, 'Excellet', 5.0, 1, 2);
    INSERT INTO PUBLIC.REVIEW VALUES (2, 'Good', 3.6, 2, 2);
    INSERT INTO PUBLIC.REVIEW VALUES (3, 'Pathetic', 3.6, 2, 1);
EOSQL