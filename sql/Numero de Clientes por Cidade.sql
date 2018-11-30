SELECT customer_state, customer_city, COUNT(*), COUNT(*)/total.total*100 as percentagem
FROM customers, (SELECT COUNT(*) as total FROM customers) as total
GROUP BY customer_state, customer_city
ORDER BY COUNT(*) DESC