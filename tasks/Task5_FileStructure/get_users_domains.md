```python
import csv
from email_utils import get_email_domain
```


```python
file = open('users.csv', 'r', newline="")
reader = csv.reader(file)
```


```python
valid_emails = []
invalid_emails = []
domains = set()

for row in reader:
    try:
        domains.add(get_email_domain(row[1]))
        valid_emails.append(row[1])
    except Exception as e:
        if str(e) == 'Invalid email address':
            invalid_emails.append(row[1])
```


```python
print("Unique Domains: {}".format(domains))
print("Number of Valid Emails: {}".format(len(valid_emails)))
print("Number of Invalid Emails: {}".format(len(invalid_emails)))
print("Invalid Emails: ")
print(invalid_emails)
```

    Unique Domains: {'yahoo.com', 'iti.gov.eg', 'example.org', 'outlook.com', 'hotmail.com', 'gmail.com'}
    Number of Valid Emails: 81
    Number of Invalid Emails: 20
    Invalid Emails: 
    ['email', 'mohamed81@', 'lamyaa16yahoo@.com', 'saeed90iti@eg', 'saeed79@hotmail,com', 'zeinab55@', 'rana66iti@eg', 'mariam13@', 'naglaa3@gmail', 'sara75@hotmail,com', 'ahmed44@gmail', 'youssef73yahoo@.com', 'ahmed28@gmail', 'omar34@gmail', 'mariam60yahoo@.com', 'khaled26@gmail', 'ahmed83@hotmail,com', 'ahmed48iti@eg', 'naglaa8yahoo@.com', 'ahmed89@gmail']
    
