-- Count total number of employees
SELECT COUNT(*) AS total_employees FROM employees;

-- Find the total sales amount
SELECT SUM(quantity * price) AS total_sales_amount
FROM sales
JOIN products ON sales.product_id = products.product_id;

-- Find the average salary of employees
SELECT AVG(salary) AS average_salary FROM employees;

-- Find the maximum and minimum product prices
SELECT MAX(price) AS max_price, MIN(price) AS min_price FROM products;

-- Find the number of products in each category
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category;

-- Find the total sales for each customer
SELECT customers.first_name, customers.last_name, SUM(quantity * price) AS total_spent
FROM sales
JOIN customers ON sales.customer_id = customers.customer_id
JOIN products ON sales.product_id = products.product_id
GROUP BY customers.customer_id;

-- Find the total quantity sold for each product
SELECT products.product_name, SUM(quantity) AS total_quantity_sold
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY sales.product_id;