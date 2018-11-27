
-- Retorna Id do comprador, Status da Ordem, quantidade, estado, tipo de pagamento, parcelas, valor da compra

select cus.customer_id, ord.order_status, count(ord.order_status), cus.customer_state, count(customer_state), pay.payment_type, pay.payment_installments, pay.payment_value from orders ord, customers cus, order_payments pay
	where ord.customer_id = cus.customer_id and 
    ord.order_id = pay.order_id and
    ord.order_status <> 'invoiced' and ord.order_status <> 'unavailable'
    group by ord.order_status, cus.customer_state
    order by cus.customer_state


-- Retorna dados das compras canceladas

select cus.customer_id, ord.order_status, count(ord.order_status) as Qtd_compras, cus.customer_state, pay.payment_type, pay.payment_installments, pay.payment_value from orders ord, customers cus, order_payments pay
	where ord.customer_id = cus.customer_id and
    ord.order_id = pay.order_id and
    ord.order_status ='canceled'
    group by cus.customer_state