import matplotlib.pyplot as plt
import numpy as np
from utils import DatabaseHelper


def extract_category_installments(row):
    if row['Categoria'] == '':
        row['Categoria'] = 'sem_categoria'

    return (
        row['Categoria'],
        row['Parcelas']
    )


def main():
    conn = DatabaseHelper.get_instance()

    with conn.cursor() as cursor:
        sql = 'SELECT ' \
            'ROUND(SUM(payment_value), 2) AS Total, ' \
            'FLOOR(AVG(payment_installments)) AS Parcelas, ' \
            'product_category_name AS Categoria ' \
            'FROM ' \
            'order_items ' \
            'NATURAL JOIN ' \
            'order_payments ' \
            'NATURAL JOIN ' \
            'products ' \
            'GROUP BY Categoria ' \
            'ORDER BY Parcelas DESC'

        cursor.execute(sql)
        result = cursor.fetchmany(25)

        category_installments = tuple(map(extract_category_installments, result))

        # categories = [a[0] for a in category_installments]
        categories = tuple(map(lambda a: a[0], category_installments))
        # installments = [a[1] for a in category_installments if a != 1]
        installments = tuple(filter(lambda a: a[1] != 1, category_installments))
        installments = tuple(map(lambda a: a[1], installments))

        plt.rcdefaults()
        fig, ax = plt.subplots()

        y_pos = np.arange(len(categories))
        error = np.random.rand(len(categories))

        ax.barh(y_pos, installments, xerr=error, align='center', color='red', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(categories)
        ax.invert_yaxis()
        ax.set_xlabel('Parcelas')
        ax.set_title('Categorias mais parceladas')

        plt.show()


if __name__ == '__main__':
    main()
