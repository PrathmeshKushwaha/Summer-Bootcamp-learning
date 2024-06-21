-- Orders Table in 1NF
CREATE TABLE Orders_1NF (
    OrderID INT,
    CustomerName VARCHAR(50),
    CustomerPhone VARCHAR(20),
    ProductID INT,
    ProductName VARCHAR(50),
    Quantity INT,
    Price DECIMAL(10, 2)
);

-- Inserting sample data
INSERT INTO Orders_1NF (OrderID, CustomerName, CustomerPhone, ProductID, ProductName, Quantity, Price)
VALUES
(1, 'Suresh Kumar', '9876543210', 101, 'Milk', 2, 45.00),
(1, 'Suresh Kumar', '9876543210', 102, 'Butter', 1, 200.00),
(2, 'Rita Singh', '9123456780', 103, 'Cheese', 5, 300.00);

-- 2NF form

-- Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    CustomerPhone VARCHAR(20)
);

-- Orders Table in 2NF
CREATE TABLE Orders_2NF (
    OrderID INT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10, 2)
);

-- Inserting sample data into Customers table
INSERT INTO Customers (CustomerID, CustomerName, CustomerPhone)
VALUES
(1, 'Suresh Kumar', '9876543210'),
(2, 'Rita Singh', '9123456780');

-- Inserting sample data into Orders table
INSERT INTO Orders_2NF (OrderID, CustomerID, ProductID, Quantity)
VALUES
(1, 1, 101, 2),
(1, 1, 102, 1),
(2, 2, 103, 5);

-- Inserting sample data into Products table
INSERT INTO Products (ProductID, ProductName, Price)
VALUES
(101, 'Milk', 45.00),
(102, 'Butter', 200.00),
(103, 'Cheese', 300.00);


-- 2NF TO 3NF

-- No changes needed from 2NF to 3NF as there are no transitive dependencies
-- Customers Table (same as 2NF)
CREATE TABLE Customers_3NF (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    CustomerPhone VARCHAR(20)
);

-- Orders Table in 3NF (same as 2NF)
CREATE TABLE Orders_3NF (
    OrderID INT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customers_3NF(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Products Table (same as 2NF)
CREATE TABLE Products_3NF (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10, 2)
);

-- Inserting sample data into Customers table
INSERT INTO Customers_3NF (CustomerID, CustomerName, CustomerPhone)
VALUES
(1, 'Suresh Kumar', '9876543210'),
(2, 'Rita Singh', '9123456780');

-- Inserting sample data into Orders table
INSERT INTO Orders_3NF (OrderID, CustomerID, ProductID, Quantity)
VALUES
(1, 1, 101, 2),
(1, 1, 102, 1),
(2, 2, 103, 5);

-- Inserting sample data into Products table
INSERT INTO Products_3NF (ProductID, ProductName, Price)
VALUES
(101, 'Milk', 45.00),
(102, 'Butter', 200.00),
(103, 'Cheese', 300.00);

