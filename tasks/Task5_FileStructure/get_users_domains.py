#!/usr/bin/env python
# coding: utf-8

# In[31]:


import csv
from email_utils import get_email_domain


# In[32]:


file = open('users.csv', 'r', newline="")
reader = csv.reader(file)


# In[33]:


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


# In[34]:


print("Unique Domains: {}".format(domains))
print("Number of Valid Emails: {}".format(len(valid_emails)))
print("Number of Invalid Emails: {}".format(len(invalid_emails)))
print("Invalid Emails: ")
print(invalid_emails)

