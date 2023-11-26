import sqlite3
import time


t0 = time.time()
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
data = cursor.execute("SELECT * FROM invest_productinvest").fetchall()
with open("test.txt", "a") as f:
    for d in data:
        f.write(" - ".join(map(str, d[1:])) + "\n")
print(time.time() - t0)
