#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# prime number 

num1 = int(input("Enter the number: "))
for i in range(2,num1):
    if (num % i) == 0:
        print("The given number is prime number: ")
        break
    else:
        print("The given number is prime")
       
else:
    print("The given number is not prime")


# In[ ]:




