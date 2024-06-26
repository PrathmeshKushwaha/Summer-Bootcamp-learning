-- Drop existing tables if they exist
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Sales;

-- Create Employees table
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    position VARCHAR(50) NOT NULL
);

-- Create Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Create Sales table
CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    employee_id INT,
    sale_date DATE NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(id)
);

-- Insert sample data into Employees table
INSERT INTO Employees (id, name, age, gender, position) VALUES
(1, 'Ravi Patel', 30, 'Male', 'Sales Manager'),
(2, 'Anita Singh', 28, 'Female', 'Sales Executive'),
(3, 'Mukesh Kumar', 35, 'Male', 'Store Manager');

-- Insert sample data into Products table
INSERT INTO Products (product_id, product_name, price) VALUES
(101, 'Milk', 20.00),
(102, 'Butter', 50.00),
(103, 'Cheese', 100.00);

-- Stored Procedure to insert a new employee
DELIMITER //
CREATE PROCEDURE InsertEmployee(
    IN employee_name VARCHAR(50),
    IN employee_age INT,
    IN employee_gender VARCHAR(10),
    IN employee_position VARCHAR(50)
)
BEGIN
    DECLARE new_id INT;
    SELECT COALESCE(MAX(id), 0) + 1 INTO new_id FROM Employees;
    INSERT INTO Employees (id, name, age, gender, position) VALUES (new_id, employee_name, employee_age, employee_gender, employee_position);
END //
DELIMITER ;

-- Call the InsertEmployee procedure
CALL InsertEmployee('Kiran Desai', 26, 'Female', 'Accountant');

-- Function to get the price of a product by ID
DELIMITER //
CREATE FUNCTION GetProductPrice(product_id INT) RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE product_price DECIMAL(10, 2);
    SELECT price INTO product_price FROM Products WHERE product_id = product_id;
    RETURN product_price;
END //
DELIMITER ;

-- Call the GetProductPrice function
SELECT GetProductPrice(102) AS ProductPrice;

-- Function to get the number of sales for a product
DELIMITER //
CREATE FUNCTION CountProductSales(product_id INT) RETURNS INT
BEGIN
    DECLARE sales_count INT;
    SELECT COUNT(*) INTO sales_count FROM Sales WHERE product_id = product_id;
    RETURN sales_count;
END //
DELIMITER ;

-- Call the CountProductSales function
SELECT CountProductSales(101) AS SalesForProduct101;

-- Procedure to record a new sale
DELIMITER //
CREATE PROCEDURE RecordSale(
    IN sale_product_id INT,
    IN sale_employee_id INT,
    IN sale_date DATE,
    IN sale_quantity INT
)
BEGIN
    DECLARE new_sale_id INT;
    SELECT COALESCE(MAX(sale_id), 0) + 1 INTO new_sale_id FROM Sales;
    INSERT INTO Sales (sale_id, product_id, employee_id, sale_date, quantity) 
    VALUES (new_sale_id, sale_product_id, sale_employee_id, sale_date, sale_quantity);
END //
DELIMITER ;

-- Call the RecordSale procedure
CALL RecordSale(101, 1, '2024-06-13', 50);

-- Function to calculate the total sales amount for a product
DELIMITER //
CREATE FUNCTION TotalSalesAmount(product_id INT) RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE total_amount DECIMAL(10, 2);
    SELECT SUM(quantity * price) INTO total_amount
    FROM Sales
    JOIN Products ON Sales.product_id = Products.product_id
    WHERE Sales.product_id = product_id;
    RETURN total_amount;
END //
DELIMITER ;

-- Call the TotalSalesAmount function
SELECT TotalSalesAmount(101) AS TotalSalesAmountForProduct101;

-- Cursor to iterate over employee names
DELIMITER //
CREATE PROCEDURE PrintEmployeeNames()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE emp_name VARCHAR(50);
    DECLARE cur CURSOR FOR SELECT name FROM Employees;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    OPEN cur;
    
    read_loop: LOOP
        FETCH cur INTO emp_name;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SELECT emp_name;
    END LOOP;
    
    CLOSE cur;
END //
DELIMITER ;

-- Call the PrintEmployeeNames procedure
CALL PrintEmployeeNames();
