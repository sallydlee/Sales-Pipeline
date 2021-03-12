DROP DATABASE IF EXISTS online_sales;
CREATE DATABASE online_sales;

USE online_sales;

CREATE TABLE ticket_sale (
	ticket_id INT UNIQUE NOT NULL,
    trans_date DATE,
    event_id INT,
    event_name VARCHAR(50),
    event_date DATE,
    event_type VARCHAR(10),
    event_city VARCHAR(20),
    event_addr VARCHAR(100),
    customer_id INT,
    price DECIMAL,
    num_tickets INT,
    PRIMARY KEY (ticket_id)
);