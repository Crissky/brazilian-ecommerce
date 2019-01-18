import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (11, 7)

reviews = pd.read_csv('../e-commerce/olist_order_reviews_dataset.csv')
reviews.head()

orders = pd.read_csv('../e-commerce/olist_orders_dataset.csv')
orders.head()

order_reviews = pd.merge(orders, reviews, on='order_id')[
    ['order_purchase_timestamp', 'order_delivered_customer_date', 'review_score']]
order_reviews.head()

order_reviews['delta_time'] = pd.to_datetime(
    order_reviews['order_delivered_customer_date']) - pd.to_datetime(order_reviews['order_purchase_timestamp'])
order_reviews = order_reviews[order_reviews['delta_time'].notnull()]
order_reviews.head(10)

x = order_reviews['delta_time'].dt.days.corr(order_reviews['review_score'])
df = order_reviews.groupby(order_reviews['delta_time'].dt.days).count()
df.head(10)

fig, ax = plt.subplots()
fig.suptitle('Entregas por período de tempo')
plt.xticks(np.arange(0, 300, 10))
ax.plot(df['review_score'])
plt.show()
