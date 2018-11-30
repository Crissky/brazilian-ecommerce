SELECT customer_state, customer_city, FORMAT(SUM(payment_value), 2) as sum_price_plus_freight, COUNT(*) as qtd, order_status
FROM customers NATURAL JOIN orders NATURAL JOIN order_payments
WHERE order_status = "delivered"
GROUP BY customer_state, customer_city
ORDER BY qtd DESC
