SELECT customer_state, FORMAT(SUM(freight_value), 2) as sum_freight, COUNT(*) as qtd, order_status
FROM customers NATURAL JOIN orders NATURAL JOIN order_items
WHERE order_status = "delivered"
GROUP BY customer_state
ORDER BY qtd DESC
