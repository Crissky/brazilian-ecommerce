SELECT seller_state, COUNT(*) as qtd, COUNT(*)/total.total * 100 AS percentage, total.total
FROM sellers, ( SELECT COUNT(*) AS total FROM sellers ) AS total
GROUP BY seller_state
ORDER BY qtd DESC