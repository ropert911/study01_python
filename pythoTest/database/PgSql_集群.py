import psycopg2

#port="5432" 可以不写，连接属性 可读写
conn = psycopg2.connect(host="192.168.20.48,192.168.20.47,192.168.20.49", dbname="pm", user="postgres", password='sks123.com',target_session_attrs="read-write")
print("Opened database successfully")

cur = conn.cursor()

# 创建
cur.execute('''CREATE TABLE if not exists COMPANY
       (ID INT PRIMARY KEY   NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print("Table created successfully")
conn.commit()

# #增加
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
# conn.commit()
# print("Records created successfully");

#删除
cur.execute("DELETE from COMPANY where ID=2;")
conn.commit


#修改
cur.execute("UPDATE COMPANY set SALARY = 26000.00 where ID=1")
conn.commit
print("Total number of rows updated :", cur.rowcount)

#查询
data = cur.execute("select * from COMPANY")
rows = cur.fetchall()
for row in rows:
    print (" ", row[0]," ",row[2]," ",row[3]," ",row[4])

#查询
data = cur.execute("SELECT pg_is_in_recovery()")
rows = cur.fetchall()
for row in rows:
    print (" ", row)

#conn.commit()
conn.close()