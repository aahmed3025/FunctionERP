# delete_table.py

import psycopg2

conn = psycopg2.connect(database="myerpdb", user="postgres", password="dbpassword", host="localhost")

cur = conn.cursor()
cur.execute("DROP TABLE erp_customer;")
conn.commit() 
conn.close()

print("Table deleted")