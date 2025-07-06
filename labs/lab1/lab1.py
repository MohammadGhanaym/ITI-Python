#!/usr/bin/env python
# coding: utf-8

# #### Task 1:Write a program that counts up  the number of vowels in a string

# In[8]:


vowels = 'aeiouAEIOU'
user_input = input()
vowels_count = 0
for c in user_input:
    if c in vowels:
        vowels_count += 1
print('Number of vowels is ', vowels_count)


# #### Task 2: Write a program that prints the locations of "i" character in any string you added.

# In[10]:


user_input = input()
for idx in range(len(user_input)):
    if user_input[idx] == 'i':
        print(f' i location {idx}')


# #### Task 3: Write a program that generate a multiplication table from 1 to the number passed.

# In[17]:


user_input = int(input('Enter a number: '))
for i in range(1, user_input + 1):
    for j in range(1, i+1):
        print(f'{i}x{j}={i * j}', end=', ')


# #### Task 4: Write a program that build a Mario pyramid like below

# In[26]:


user_input = int(input('Enter a number: '))

for i in range(1, user_input + 1):
    print(' ' * (user_input - i), end='')
    print('*' * i)

