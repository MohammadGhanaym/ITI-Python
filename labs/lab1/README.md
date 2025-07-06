#### Task 1:Write a program that counts up  the number of vowels in a string


```python
vowels = 'aeiouAEIOU'
user_input = input()
vowels_count = 0
for c in user_input:
    if c in vowels:
        vowels_count += 1
print('Number of vowels is ', vowels_count)
```

     Nour Ghanaym
    

    Number of vowels is  4
    

#### Task 2: Write a program that prints the locations of "i" character in any string you added.


```python
user_input = input()
for idx in range(len(user_input)):
    if user_input[idx] == 'i':
        print(f' i location {idx}')
```

     iti
    

     i location 0
     i location 2
    

#### Task 3: Write a program that generate a multiplication table from 1 to the number passed.


```python
user_input = int(input('Enter a number: '))
for i in range(1, user_input + 1):
    for j in range(1, i+1):
        print(f'{i}x{j}={i * j}', end=', ')
```

    Enter a number:  5
    

    1x1=1, 2x1=2, 2x2=4, 3x1=3, 3x2=6, 3x3=9, 4x1=4, 4x2=8, 4x3=12, 4x4=16, 5x1=5, 5x2=10, 5x3=15, 5x4=20, 5x5=25, 

#### Task 4: Write a program that build a Mario pyramid like below


```python
user_input = int(input('Enter a number: '))

for i in range(1, user_input + 1):
    print(' ' * (user_input - i), end='')
    print('*' * i)
```

    Enter a number:  4
    

       *
      **
     ***
    ****
    
