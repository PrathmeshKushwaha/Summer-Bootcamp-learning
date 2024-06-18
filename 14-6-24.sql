-- Create the database
CREATE DATABASE AmulCompany;
USE AmulCompany;

-- Create the employees table
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    position VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- Create the products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,
    stock INT
);

-- Create the customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
);

-- Create the sales table
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into employees table
INSERT INTO employees (first_name, last_name, position, salary, hire_date) VALUES
('Amit', 'Sharma', 'Manager', 75000.00, '2019-01-15'),
('Priya', 'Verma', 'Salesperson', 45000.00, '2020-03-10'),
('Raj', 'Patel', 'Accountant', 55000.00, '2018-07-25');

-- Insert sample data into products table
INSERT INTO products (product_name, category, price, stock) VALUES
('Milk', 'Dairy', 45.00, 1000),
('Butter', 'Dairy', 200.00, 500),
('Cheese', 'Dairy', 300.00, 300);

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone) VALUES
('Suresh', 'Kumar', 'suresh.kumar@example.com', '9876543210'),
('Rita', 'Singh', 'rita.singh@example.com', '9123456780');

-- Insert sample data into sales table
INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES
(1, 1, 2, '2023-06-01'),
(1, 2, 1, '2023-06-02'),
(2, 3, 5, '2023-06-03');

-- Retrieve all employees
SELECT * FROM employees;

-- Retrieve all products
SELECT * FROM products;

-- Retrieve all customers
SELECT * FROM customers;

-- Retrieve all sales
SELECT * FROM sales;
