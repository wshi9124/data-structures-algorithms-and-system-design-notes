SELECT * 
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id

SELECT *
FROM orders o, customers c 
WHERE o.customer_id = c.customer_id