DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS sensor_types;
DROP TABLE IF EXISTS readings;

CREATE TABLE users
(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE sensor_types
(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    unit VARCHAR(20)
);

CREATE TABLE readings
(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    sensor_type_id INT NOT NULL,
    value DOUBLE NOT NULL,
    rec_time DATETIME(3) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (sensor_type_id) REFERENCES sensor_types(id),
    INDEX idx_lookup (user_id, sensor_type_id, rec_time)
);