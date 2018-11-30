SELECT customer_state, 
MONTHNAME(order_purchase_timestamp) as Mes,
YEAR(order_purchase_timestamp) as Ano,
COUNT(*) as order_qtd,
AVG(datediff(order_estimated_delivery_date, order_delivered_customer_date)) as data_entrega_X_estimado
FROM orders NATURAL JOIN customers
WHERE order_status = "delivered"
GROUP BY customer_state, Mes, Ano
ORDER BY customer_state, order_purchase_timestamp
