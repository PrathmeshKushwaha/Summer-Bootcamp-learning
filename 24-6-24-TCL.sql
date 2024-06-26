-- Drop existing tables if they exist
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Departments;

-- Create Employees table
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    department_id INT
);

-- Create Departments table
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    employee_count INT DEFAULT 0
);

-- Create Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Create Sales table
CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    employee_id INT,
    sale_date DATE,
    quantity INT,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES Products(product_id),
    CONSTRAINT fk_employee FOREIGN KEY (employee_id) REFERENCES Employees(id)
);

-- TCL Example: Managing transactions with BEGIN, COMMIT, and ROLLBACK
BEGIN;

-- Inserting data into Employees table
INSERT INTO Employees (id, name, age, gender, department_id) VALUES
(1, 'Ravi Patel', 30, 'Male', 1),
(2, 'Anita Singh', 28, 'Female', 1),
(3, 'Mukesh Kumar', 35, 'Male', 2);

-- Inserting data into Departments table
INSERT INTO Departments (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Store');

-- Inserting data into Products table
INSERT INTO Products (product_id, product_name, price) VALUES
(101, 'Milk', 20.00),
(102, 'Butter', 50.00),
(103, 'Cheese', 100.00);

-- Commit the transaction to make changes permanent
COMMIT;

-- Rollback example (commented out for now)
-- ROLLBACK;

-- Triggers
-- Triggers are special types of stored procedures that automatically execute when a specific event occurs in the database.

-- Example: Update employee count in Departments table after insertion into Employees
DELIMITER //
CREATE TRIGGER UpdateEmployeeCount
AFTER INSERT ON Employees
FOR EACH ROW
BEGIN
    DECLARE dept_employee_count INT;
    SELECT COUNT(*) INTO dept_employee_count FROM Employees WHERE department_id = NEW.department_id;
    UPDATE Departments SET employee_count = dept_employee_count WHERE department_id = NEW.department_id;
END //
DELIMITER ;

-- Example insert into Employees triggering the update
INSERT INTO Employees (id, name, age, gender, department_id) VALUES
(4, 'Kiran Desai', 26, 'Female', 1);

-- Check if trigger updated employee_count in Departments table
SELECT * FROM Departments;

-- Views
-- Views are virtual tables created by a query. They can simplify complex queries and provide a layer of security by restricting access to certain columns.

-- Example: Create a view to display employee information with sales details
CREATE VIEW EmployeeSalesView AS
SELECT E.name AS employee_name, E.age, E.gender, P.product_name, S.sale_date, S.quantity
FROM Employees E
JOIN Sales S ON E.id = S.employee_id
JOIN Products P ON S.product_id = P.product_id;

-- Query the view
SELECT * FROM EmployeeSalesView;
