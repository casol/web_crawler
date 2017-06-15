import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='22listopad', db='mysql')

cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT content FROM pages WHERE id=23")
print(cur.fetchone())
cur.close()
conn.close()
