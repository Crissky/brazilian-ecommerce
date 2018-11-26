import matplotlib.pyplot as plt
import numpy as np
from utils import DatabaseHelper


def extract_review_price(row):
    return (
        row['review_comment_message'].replace('\r\n', ''),
        row['price']
    )


def main():
    conn = DatabaseHelper.get_instance()

    with conn.cursor() as cursor:
        sql = 'SELECT * FROM order_reviews NATURAL JOIN order_items NATURAL JOIN sellers'
        cursor.execute(sql)
        result = cursor.fetchmany(100)
        print(result)
        review_messages = map(extract_review_price, result)
        list(map(print, list(review_messages)))

        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()


if __name__ == '__main__':
    main()
