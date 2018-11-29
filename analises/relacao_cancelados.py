import matplotlib.pyplot as plt
import numpy as np
from utils import DatabaseHelper

plt.style.use('ggplot')


listaEstados=[]
cancelamentos=[]
def extract_state(row):
    return (
        row['customer_state'].replace(',', '') ,
        listaEstados.append(row['customer_state'].replace(',', ''))
    )

def extract_qtd(row):
    return (
        row['Qtd_compras'],
        cancelamentos.append(row['Qtd_compras'])
    )


def main():
    conn = DatabaseHelper.get_instance()
    with conn.cursor() as cursor:
        sql = 'select cus.customer_id, ord.order_status, count(ord.order_status) as Qtd_compras, cus.customer_state, pay.payment_type, pay.payment_installments, pay.payment_value from orders ord, customers cus, order_payments pay where ord.customer_id = cus.customer_id and ord.order_id = pay.order_id and ord.order_status ="canceled" group by cus.customer_state'
        cursor.execute(sql)
        result = cursor.fetchmany(23)
        review_qtd = map(extract_qtd, result)
        estados = map(extract_state, result)
        list(estados)
        list(review_qtd)

        plt.rcdefaults()
        fig, ax = plt.subplots()

        y_pos = np.arange(len(listaEstados))
        performance = cancelamentos
        error = np.random.rand(len(listaEstados))

        ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(listaEstados)
        ax.invert_yaxis()
        ax.set_xlabel('Valores')
        ax.set_title('Estados que mais cancelaram compras')

        print('')
        plt.show()

if __name__ == '__main__':
    main()
