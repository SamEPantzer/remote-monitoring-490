CREATE IF NOT EXISTS capstone;
USE capstone;

CREATE TABLE test
(
    id INT unsigned NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    primary key (id) -- Change this later to match username(?)
);