```python
from user_validation import is_valid_email, is_valid_name
from textfunc import is_vowel, print_i_locations
from multtable import print_mult_table, get_mult_table
from mariopyramid import mario_from_num, mario_from_list
from listsort import print_sorted_arr
```


```python
user_input = input('Enter a text: ')
vowels_count = sum(map(is_vowel, user_input))
print(f"Number of vowels is {vowels_count}")
print_i_locations(user_input)
```

    Enter a text:  Hello, Itians
    

    Number of vowels is 5
     i location 9
    


```python
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
    


```python
user_input = int(input('Enter a number: '))
mario_from_num(user_input)
```

    Enter a number:  5
    

        *
       **
      ***
     ****
    *****
    


```python
l = [' ', ' ', ' ', ' ', ' ']
mario_from_list(l)
```

        *
       **
      ***
     ****
    *****
    


```python
nums = []
while len(nums) < 5:
    x = input('Enter a number: ').strip()
    if x.isdigit():
        nums.append(int(x))
    else:
        print("Wrong input! Please enter a number")

print_sorted_arr(nums)
```

    Enter a number:  10
    Enter a number:  3
    Enter a number:  11
    Enter a number:  3
    Enter a number:  4
    

    Original List:  [10, 3, 11, 3, 4]
    Sorted Descending:  [11, 10, 4, 3, 3]
    Sorted Ascedning:  [3, 3, 4, 10, 11]
    


```python
n = input('Enter a number: ')
while not n.isdigit():
    n = input("Please enter a number: ")
    
n = int(n)

tables = get_mult_table(n)
print(tables)
```

    Enter a number:  5
    

    [[1], [2, 4], [3, 6, 9], [4, 8, 12, 16], [5, 10, 15, 20, 25]]
    


```python
name = ''
while not is_valid_name(name):
    name = input("Please enter your name: ").strip()

email = ''
while not is_valid_name(email) or not is_valid_email(email):
    email = input("Please enter your email: ").strip()
        
print(name)
print(email)
```

    Please enter your name:  123
    Please enter your name:   
    Please enter your name:  
    Please enter your name:  Nour
    Please enter your email:  nour@@gmail.com
    

    Invalid Email!
    

    Please enter your email:  nour.com
    Please enter your email:  nour@.com
    Please enter your email:  nour@gmail.com
    

    Nour
    nour@gmail.com
    
