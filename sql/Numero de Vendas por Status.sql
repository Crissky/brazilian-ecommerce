SELECT order_status, COUNT(*) as qtd, COUNT(*)/total.total * 100 AS percentage
FROM orders, ( SELECT COUNT(*) AS total FROM orders ) AS total
GROUP BY order_status
ORDER BY qtd DESC
