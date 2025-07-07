#!/usr/bin/env python
# coding: utf-8

# ## Lab 1

# #### Task 1:Write a program that counts up  the number of vowels in a string

# In[2]:


def is_vowel(c):
    vowels = 'aeiou'
    return c.lower() in vowels

user_input = input()
vowels_count = sum(map(is_vowel, user_input))
print(f"Number of vowels is {vowels_count}")


# #### Task 2: Write a program that prints the locations of "i" character in any string you added.

# In[3]:


def print_i_locations(text):
    for idx in range(len(user_input)):
        if user_input[idx] == 'i':
            print(f' i location {idx}')
        
user_input = input()
print_i_locations(user_input)


# #### Task 3: Write a program that generate a multiplication table from 1 to the number passed.

# In[7]:


def print_mult_table(num):
    for i in range(1, user_input + 1):
        for j in range(1, i+1):
            print(f'{i}x{j}={i * j}')
        print('=' * 10)

user_input = int(input('Enter a number: '))
print_mult_table(user_input)


# #### Task 4: Write a program that build a Mario pyramid like below

# In[9]:


def generate_mario_pyramid(base_size):
    for i in range(1, base_size + 1):
        print(' ' * (base_size - i), end='')
        print('*' * i)


user_input = int(input('Enter a number: '))
generate_mario_pyramid(user_input)


# ## Lab 2

# In[11]:


def lst_to_mario(lst):
    '''
    print the mario pyramid based on a list of empty string
    Args:
        lst (list): list of empty strings
    Returns:
        None
    '''
    for i in range(1, len(l) + 1):
        l[-i] = '*'
        print(''.join(l))

l = [' ', ' ', ' ', ' ', ' ']
lst_to_mario(l)


# #### Task 1: Fill an array of 5 elements from the user, sort it in descending and ascending orders then display the output.

# In[14]:


def print_sorted_arr(nums):
    print('Original List: ', nums)
    print('Sorted Descending: ', sorted(nums, reverse=True))
    print('Sorted Ascedning: ', sorted(nums))

nums = []
while len(nums) < 5:
    x = input('Enter a number: ').strip()
    if x.isdigit():
        nums.append(int(x))
    else:
        print("Wrong input! Please enter a number")

print_sorted_arr(nums)


# #### Task 2: Write a program that generate a multiplication table from 1 to the number passed.

# In[15]:


def get_mult_table(n):
    tables = []
    for i in range(1, n+1):
        mult_table = []
        for j in range(1, i+1):
            mult_table.append(j * i)
        tables.append(mult_table)
    
    return tables

n = input('Enter a number: ')
while not n.isdigit():
    n = input("Please enter a number: ")
    
n = int(n)

tables = get_mult_table(n)
print(tables)


# #### Task 3: Ask the user for his name then confirm that he has entered his name (not an empty string/integers). Then proceed to ask him for his email and print all this data (Bonus) check if it is a valid email or not.

# In[19]:


def is_valid_email(email):
    if '@' in email:
        username, domain = email.split('@')
        if username and domain:
            d1, *d2 = domain.split('.')
            if d1 and d2:
                return True
    return False


def is_valid_name(name):
    return name and not name.isdigit()


name = ''
while not is_valid_name(name):
    name = input("Please enter your name: ").strip()

email = ''
while not is_valid_name(email) or not is_valid_email(email):
    email = input("Please enter your email: ").strip()
        
print(name)
print(email)

