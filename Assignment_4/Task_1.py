#!/usr/bin/env python
# coding: utf-8

# In[12]:


try:
    file = open("sample.txt", "w")
    file.write("This is a simple text file.\nIt contains multiple lines")
    file.close()
    file = open("sample.txt", "r")
    print("Reading file content:\n")
    print(file.read())
    file.close()
except:
    print("File not Found")
          
     


# In[ ]:




