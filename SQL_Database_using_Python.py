#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Install & load sqlite3
get_ipython().system('pip install sqlite3  # #Uncomment the code to install sqlite3')
import sqlite3


# In[34]:


# Connecting to sqlite
# connection object
conn = sqlite3.connect('INSTRUCTOR.db')


# In[35]:


# cursor object
cursor_obj = conn.cursor()


# In[13]:


# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")


# In[14]:


# Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""

cursor_obj.execute(table)
 
print("Table is Ready")


# In[15]:


cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')


# In[16]:


cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')


# In[17]:


statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)


# In[18]:


# Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)


# In[19]:


# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)


# In[26]:


# executing an update statement that changes the Rav's CITY to MOOSETOWN
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)


# In[27]:


import pandas as pd
#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)

#print the dataframe
df


# In[28]:


#print just the LNAME for first row in the pandas data frame
df.LNAME[0]


# In[29]:


#use the shape method to see how many rows and columns are in the dataframe
df.shape


# In[36]:


# Close the connection
cursor_obj.close()
conn.close()

