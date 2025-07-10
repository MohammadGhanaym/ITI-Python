#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
from email_utils import get_email_domain


# In[7]:


file = open('users.csv', 'r', newline="")
reader = csv.reader(file)


# In[8]:


valid_emails = []
invalid_emails = []
domains = set()

reader = list(reader)
for row in range(1, len(reader)):
    try:
        domains.add(get_email_domain(reader[row][1]))
        valid_emails.append(reader[row][1])
    except Exception as e:
        if str(e) == 'Invalid email address':
            invalid_emails.append(reader[row][1])


# In[9]:


print("Unique Domains: {}".format(domains))
print("Number of Valid Emails: {}".format(len(valid_emails)))
print("Number of Invalid Emails: {}".format(len(invalid_emails)))
print("Invalid Emails: ")
print(invalid_emails)

