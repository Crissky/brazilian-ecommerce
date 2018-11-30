SELECT customer_state, COUNT(*) as qtd, COUNT(*)/total.total * 100 AS percentage, total.total
FROM customers, ( SELECT COUNT(*) AS total FROM customers ) AS total
GROUP BY customer_state
ORDER BY qtd DESC

#SELECT COUNT(*) as qtd
#FROM customers
