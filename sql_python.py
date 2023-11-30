import sqlite3


# Connecting to sqlite
conn = sqlite3.connect('INSTRUCTOR.db')

# Cursor object is used to invoke methods that execute SQLite statements and 
# fetch data from the result sets of the queries. 
cursor_obj = conn.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY\
  NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cursor_obj.execute(table)

cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'),\
                   (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)

statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)

query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)

# Close the connection
conn.close()