#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE DATABASE mydb;
    GRANT ALL PRIVILEGES ON DATABASE mydb TO postgres;
    \c mydb;
    CREATE TABLE PUBLIC.PRODUCT (
        id INT PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    );
    CREATE TABLE PUBLIC.USER (
        id INT PRIMARY KEY,
        name TEXT NOT NULL
    );
    CREATE TABLE PUBLIC.REVIEW (
        id INT PRIMARY KEY,
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
    INSERT INTO PUBLIC.REVIEW VALUES (12, 'Excellent', 5.0, 1, 2);
    INSERT INTO PUBLIC.REVIEW VALUES (22, 'Good', 3.0, 2, 2);
    INSERT INTO PUBLIC.REVIEW VALUES (21, 'Pathetic', 1.0, 2, 1);
    INSERT INTO PUBLIC.REVIEW VALUES (44, 'Extremely Woww', 5.0, 4, 4);
    INSERT INTO PUBLIC.REVIEW VALUES (35, 'Superb', 4.6, 3, 5);
    INSERT INTO PUBLIC.REVIEW VALUES (53, 'Poor', 3.6, 5, 3);
EOSQL