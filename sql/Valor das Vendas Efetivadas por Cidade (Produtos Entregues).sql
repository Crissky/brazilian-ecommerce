SELECT customer_state, customer_city, FORMAT(SUM(price), 2) as sum_price, COUNT(*) as qtd, order_status
FROM customers NATURAL JOIN orders NATURAL JOIN order_items
WHERE order_status = "delivered"
GROUP BY customer_state, customer_city
ORDER BY qtd DESC
