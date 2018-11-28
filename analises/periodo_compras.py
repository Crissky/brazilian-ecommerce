import matplotlib.pyplot as plt
import numpy as np
from utils import DatabaseHelper


def extract_date(row):
    return row['order_purchase_timestamp'].date()


def main():
    conn = DatabaseHelper.get_instance()
    with conn.cursor() as cursor:
        sql = 'SELECT DISTINCT(order_purchase_timestamp) FROM orders'
        cursor.execute(sql)
        result = cursor.fetchmany(500)

        dates = list(map(extract_date, result))
        dates.sort()
        tuple(map(print, dates))


if __name__ == '__main__':
    main()
