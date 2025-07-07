## Lab 1

#### Task 1:Write a program that counts up  the number of vowels in a string


```python
def is_vowel(c):
    vowels = 'aeiou'
    return c.lower() in vowels

user_input = input()
vowels_count = sum(map(is_vowel, user_input))
print(f"Number of vowels is {vowels_count}")
```

     Nour Ghanaym
    

    Number of vowels is 4
    

#### Task 2: Write a program that prints the locations of "i" character in any string you added.


```python
def print_i_locations(text):
    for idx in range(len(user_input)):
        if user_input[idx] == 'i':
            print(f' i location {idx}')
        
user_input = input()
print_i_locations(user_input)
```

     iti
    

     i location 0
     i location 2
    

#### Task 3: Write a program that generate a multiplication table from 1 to the number passed.


```python
def print_mult_table(num):
    for i in range(1, user_input + 1):
        for j in range(1, i+1):
            print(f'{i}x{j}={i * j}')
        print('=' * 10)

user_input = int(input('Enter a number: '))
print_mult_table(user_input)
```

    Enter a number:  5
    

    1x1=1
    ==========
    2x1=2
    2x2=4
    ==========
    3x1=3
    3x2=6
    3x3=9
    ==========
    4x1=4
    4x2=8
    4x3=12
    4x4=16
    ==========
    5x1=5
    5x2=10
    5x3=15
    5x4=20
    5x5=25
    ==========
    

#### Task 4: Write a program that build a Mario pyramid like below


```python
def generate_mario_pyramid(base_size):
    for i in range(1, base_size + 1):
        print(' ' * (base_size - i), end='')
        print('*' * i)


user_input = int(input('Enter a number: '))
generate_mario_pyramid(user_input)
```

    Enter a number:  4
    

       *
      **
     ***
    ****
    

## Lab 2


```python
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
```

        *
       **
      ***
     ****
    *****
    

#### Task 1: Fill an array of 5 elements from the user, sort it in descending and ascending orders then display the output.


```python
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
```

    Enter a number:  12
    Enter a number:  3
    Enter a number:  5
    Enter a number:  2
    Enter a number:  11
    

    Original List:  [12, 3, 5, 2, 11]
    Sorted Descending:  [12, 11, 5, 3, 2]
    Sorted Ascedning:  [2, 3, 5, 11, 12]
    

#### Task 2: Write a program that generate a multiplication table from 1 to the number passed.


```python
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
```

    Enter a number:  5
    

    [[1], [2, 4], [3, 6, 9], [4, 8, 12, 16], [5, 10, 15, 20, 25]]
    

#### Task 3: Ask the user for his name then confirm that he has entered his name (not an empty string/integers). Then proceed to ask him for his email and print all this data (Bonus) check if it is a valid email or not.


```python
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
```

    Please enter your name:  
    Please enter your name:   
    Please enter your name:  123
    Please enter your name:  Nour
    Please enter your email:  nour@.com
    Please enter your email:  nour@com
    Please enter your email:  nour.com
    Please enter your email:  @.com
    Please enter your email:  nour@gmail.com
    

    Nour
    nour@gmail.com
    
