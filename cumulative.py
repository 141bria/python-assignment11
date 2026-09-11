import sqlite3
import pandas as pd
import matplotlib as plt
conn=sqlite3.connect("db/lesson.db")

query = """
SELECT 
orders.order_id,
SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items
ON orders.order_id = line_items.order_id
JOIN products
ON line_items.product_id = products.product_id
GROUP BY orders.order_id
"""

order_details = pd.read_sql_query(query,conn)
order_details['cumulative'] = order_details['total_price'].cumsum()
order_details.plot(x="order_id", y="revnue",kind="line",title="Revenue vs Order Id")
plt.show()