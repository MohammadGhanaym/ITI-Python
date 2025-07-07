## lab4: 
- email validation error handling.
    - Use `try` and `except`
- Allow the user to try for 5 times
    - If valid, break. Otherwise, raise error in case the user completed the 5 tries.
  

task: create modules from previous functions.


```python
def is_valid_email(email):
    try:
        if '@' in email:
            username, domain = email.split('@')
            if username and domain:
                *d1, d2 = domain.split('.')
                if ''.join(d1) and d2:
                    return True
    except ValueError:
        print("Invalid Email!")
        return False
        
    return False
```


```python

for _ in range(5):
    email = input('Please enter your email: ')
    if is_valid_email(email):
        break
else:
    raise Exception('You expired your 5 tries')

print(email)
```

    Please enter your email:  nour..com
    Please enter your email:  nour@com
    Please enter your email:  nour@@gmail.com
    

    Invalid Email!
    

    Please enter your email:  nour.com
    Please enter your email:  @.com
    


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    Cell In[19], line 6
          4         break
          5 else:
    ----> 6     raise Exception('You expired your 5 tries')
          8 print(email)
    

    Exception: You expired your 5 tries



```python

```
