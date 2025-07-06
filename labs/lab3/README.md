#### Task 1: Validate email


```python
def is_valid_email(email):
    if '@' in email:
        username, domain = email.split('@')
        if username and domain:
            d1, *d2 = domain.split('.')
            if d1 and d2:
                return True
    return False
```


```python
email = ''
while not is_valid_email(email):
    email = input('Enter your email: ')

print(email)
```

    Enter your email:  nour.@.com
    Enter your email:  nour@com
    Enter your email:  nour.com
    Enter your email:  nour@gmail.com
    

    nour@gmail.com
    

#### Task2: Auth Users


```python
users = [
    {'name':'omar', 'pass':'123'},
    {'name':'nour', 'pass':'456'}
    ]

name = input('Enter your name: ')
for user in users:
    if name == user['name']:
        password = input("Enter your password: ")
        if password == user['pass']:
            print("Welcome,", name)
            break
        else:
            print("Incorrect Password")
            break
    else:
        continue
else:
    print("You are not a user, please sign up.")
```

    Enter your name:  ahmed
    

    You are not a user, please sign up.
    

#### Task3: Get users domains

#### Task4: Validate list of emails


```python
emails = [
    'nour@gmail.com',
    'omar@iti.gov.eg',
    'mohammad@outlook.com',
    'ibrahim@yahoo.com',
    'sayed@.com',
    '@yahoo.com'
    ]

valid_emails = filter(is_valid_email, emails)
users_domains = []


users_domains = list(map(lambda email: email.split('@')[1], emails))

print(users_domains)
```

    ['gmail.com', 'iti.gov.eg', 'outlook.com', 'yahoo.com', '.com', 'yahoo.com']
    
