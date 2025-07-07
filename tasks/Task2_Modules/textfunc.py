#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_vowel(c):
    vowels = 'aeiou'
    return c.lower() in vowels


def print_i_locations(text):
    for idx in range(len(text)):
        if text[idx] == 'i':
            print(f' i location {idx}')

