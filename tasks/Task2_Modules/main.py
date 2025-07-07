#!/usr/bin/env python
# coding: utf-8

# In[4]:


from user_validation import is_valid_email, is_valid_name
from textfunc import is_vowel, print_i_locations
from multtable import print_mult_table, get_mult_table
from mariopyramid import mario_from_num, mario_from_list
from listsort import print_sorted_arr


# In[2]:


user_input = input('Enter a text: ')
vowels_count = sum(map(is_vowel, user_input))
print(f"Number of vowels is {vowels_count}")
print_i_locations(user_input)


# In[4]:


user_input = int(input('Enter a number: '))
print_mult_table(user_input)


# In[3]:


user_input = int(input('Enter a number: '))
mario_from_num(user_input)


# In[4]:


l = [' ', ' ', ' ', ' ', ' ']
mario_from_list(l)


# In[6]:


nums = []
while len(nums) < 5:
    x = input('Enter a number: ').strip()
    if x.isdigit():
        nums.append(int(x))
    else:
        print("Wrong input! Please enter a number")

print_sorted_arr(nums)


# In[2]:


n = input('Enter a number: ')
while not n.isdigit():
    n = input("Please enter a number: ")
    
n = int(n)

tables = get_mult_table(n)
print(tables)


# In[5]:


name = ''
while not is_valid_name(name):
    name = input("Please enter your name: ").strip()

email = ''
while not is_valid_name(email) or not is_valid_email(email):
    email = input("Please enter your email: ").strip()
        
print(name)
print(email)

