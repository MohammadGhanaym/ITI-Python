#!/usr/bin/env python
# coding: utf-8

# In[14]:


l = [' ', ' ', ' ', ' ', ' ']

for i in range(1, len(l) + 1):
    l[-i] = '*'
    print(''.join(l))


# #### Task 1: Fill an array of 5 elements from the user, sort it in descending and ascending orders then display the output.

# In[3]:


nums = []
while len(nums) < 5:
    x = input('Enter a number: ').strip()
    if x.isdigit():
        nums.append(int(x))
    else:
        print("Wrong input! Please enter a number")

print('Nums: ', nums)
print('Sorted Descending: ', sorted(nums, reverse=True))
print('Sorted Ascedning: ', sorted(nums))


# #### Task 2: Write a program that generate a multiplication table from 1 to the number passed.

# In[10]:


n = input('Enter a number: ')
while not n.isdigit():
    n = input("Please enter a number: ")
    
n = int(n)

tables = []
for i in range(1, n+1):
    mult_table = []
    for j in range(1, i+1):
        mult_table.append(j * i)
    tables.append(mult_table)

del mult_table

print(tables)


# #### Task 3: Ask the user for his name then confirm that he has entered his name (not an empty string/integers). Then proceed to ask him for his email and print all this data (Bonus) check if it is a valid email or not.

# In[ ]:


name = ''
while len(name) == 0 or name[0].isdigit() or name.isdigit():
    name = input("Please enter your name: ").strip()

email = ''
while len(email) == 0 or email[0].isdigit() or email.isdigit():
    email = input("Please enter your email: ").strip()
    # validate email
    validate_email = email.split('@')
    print(validate_email)
    flag = 1
    if len(validate_email) == 2 and validate_email[0].isalnum(): # check that there is one @ and the first part is alphanumeric
        validate_email = validate_email[1].split('.')
        if len(validate_email) == 2 and validate_email[0].isalpha() and validate_email[0].isalpha():
            flag = 0
            
    if flag:
        print('Invalid Email!')
        email = ''
        
print(name)
print(email)


# In[ ]:


omat

