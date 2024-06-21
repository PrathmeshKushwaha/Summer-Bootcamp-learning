-- Inner Join between sales and customers to get customer details for each sale
SELECT sales.sale_id, sales.quantity, sales.sale_date, customers.first_name, customers.last_name, customers.email
FROM sales
INNER JOIN customers ON sales.customer_id = customers.customer_id;

-- Inner Join between sales and products to get product details for each sale
SELECT sales.sale_id, sales.quantity, sales.sale_date, products.product_name, products.category, products.price
FROM sales
INNER JOIN products ON sales.product_id = products.product_id;

-- Inner Join to get all information about sales, including customer and product details
SELECT sales.sale_id, sales.quantity, sales.sale_date, customers.first_name, customers.last_name, customers.email, products.product_name, products.category, products.price
FROM sales
INNER JOIN customers ON sales.customer_id = customers.customer_id
INNER JOIN products ON sales.product_id = products.product_id;

-- Left Join to get all customers and their sales (if any)
SELECT customers.first_name, customers.last_name, sales.sale_id, sales.quantity, sales.sale_date
FROM customers
LEFT JOIN sales ON customers.customer_id = sales.customer_id;

-- Right Join to get all sales and the respective customer details (if any)
SELECT sales.sale_id, sales.quantity, sales.sale_date, customers.first_name, customers.last_name
FROM sales
RIGHT JOIN customers ON sales.customer_id = customers.customer_id;

-- Full Outer Join to get all customers and all sales, combining left and right join
-- Note: MySQL does not directly support FULL OUTER JOIN, so we use UNION of LEFT and RIGHT JOIN.
SELECT customers.first_name, customers.last_name, sales.sale_id, sales.quantity, sales.sale_date
FROM customers
LEFT JOIN sales ON customers.customer_id = sales.customer_id
UNION
SELECT customers.first_name, customers.last_name, sales.sale_id, sales.quantity, sales.sale_date
FROM sales
RIGHT JOIN customers ON sales.customer_id = customers.customer_id;

-- Cross Join to get all combinations of customers and products
SELECT customers.first_name, customers.last_name, products.product_name, products.category
FROM customers
CROSS JOIN products;

-- Aggregate function to get total sales amount for each product
SELECT products.product_name, SUM(sales.quantity * products.price) AS total_sales
FROM sales
INNER JOIN products ON sales.product_id = products.product_id
GROUP BY products.product_name;

-- Aggregate function to get the number of sales for each customer
SELECT customers.first_name, customers.last_name, COUNT(sales.sale_id) AS number_of_sales
FROM sales
INNER JOIN customers ON sales.customer_id = customers.customer_id
GROUP BY customers.customer_id;

-- Using built-in functions to get the highest and lowest priced products
SELECT product_name, price
FROM products
WHERE price = (SELECT MAX(price) FROM products)
UNION
SELECT product_name, price
FROM products
WHERE price = (SELECT MIN(price) FROM products);