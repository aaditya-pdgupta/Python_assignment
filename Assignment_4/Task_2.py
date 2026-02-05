#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text1 = input("Enter text to write to the file: ")

file = open("output.txt", "w")
file.write(text1 + "\n")
file.close()

print("Data successfully written to output.txt.\n")

text2 = input("Enter additional text to append: ")

file = open("output.txt", "a")
file.write(text2 + "\n")
file.close()

print("Data successfully appended.\n")

file = open("output.txt", "r")
print("Final content of output.txt:")
print(file.read())
file.close()


# In[ ]:




