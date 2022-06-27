#!/usr/bin/env python
# coding: utf-8

# In[13]:


## Regulear Expressions ##
# serach for a match in a string

#re.match() = searchs only in  the beginning of the first line of the string and return matched object if found, else return none.
#re.search() = Return a match object if there is  one anywere in the string, including multiline string.
#re.findall() = Return a list containing all matches
#re.split() = Takes a string, spites si at the match pointsm return a list.
#re.sub() = Replaces one or two many matches within a string

# syntac
#re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore


# re can be used in file handaling and writhing


# In[ ]:


"""
* []:  A set of characters
  * [a-c] means, a or b or c
  * [a-z] means, any letter from a to z
  * [A-Z] means, any character from A to Z
  * [0-3] means, 0 or 1 or 2 or 3
  * [0-9] means any number from 0 to 9
  * [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
* \\:  uses to escape special characters
  * \d means: match where the string contains digits (numbers from 0-9)
  * \D means: match where the string does not contain digits
* . : any character except new line character(\n)
* ^: starts with
  * r'^substring' eg r'^love', a sentence that starts with a word love
  * r'[^abc] means not a, not b, not c.
* $: ends with
  * r'substring$' eg r'love$', sentence  that ends with a word love
* *: zero or more times
  * r'[a]*' means a optional or it can occur many times.
* +: one or more times
  * r'[a]+' means at least once (or more)
* ?: zero or one time
  *  r'[a]?' means zero times or once
* {3}: Exactly 3 characters
* {3,}: At least 3 characters
* {3,8}: 3 to 8 characters
* |: Either or
  * r'apple|banana' means either apple or a banana
* (): Capture and group

![Regular Expression cheat sheet]
"""


# In[22]:


import re

txt = 'I love to learn pyhton'
match = re.match('I love to learn',txt, re.I)
print(match)
# IT return an object with span, and match


span = match.span() # as a tuple using span
print(span)


# lets find the start and stop position from the span
start, end = span
print(start, end)

#is a substring we are looking for
substring = txt[start:end]
print(substring)

# not a substrinag
txt = 'I love to learn python'
match = re.match('I like to learn', txt, re.I)
print(match)  # None



# In[23]:


# re.search() 

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first


# In[32]:


#re.findall() = return all the matches as a list

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

#it return a list
matchse = re.findall('language',txt, re.I)
print(matchse)
matches = re.findall('python',txt,re.I)
#matches = re.findall('Python|python',txt)
#matches = re.findall('[Pp]ython',txt)
print(matches)


# In[33]:


# re.sub() = replace a Substring

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_rep = re.sub('[Pp]ython','javascript',txt,re.I)
print(match_rep)


# In[34]:


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


# In[40]:


# re.split() = Splitting Text Using RegEx Split
txt = '''kazi samir is the best programmer in the world.
And he knows how to solve the problems,
That's why is so famous in the world. '''

print(re.split('\n',txt)) # splitting using \n -end of line symbol


# In[44]:


# Writing RegEx Patterns

import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruite. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
#match = re.findall(regex_pattern,txt)
#match = re.findall(regex_pattern,txt, re.I)

regex_pattern = r'[aA]pple' # this means the first letter could be Apple or apple
match = re.findall(regex_pattern,txt)
print(match)


# In[47]:


# If Apple & Banana
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)


# In[49]:


# Escpae character (\\) in RegEx

#regex_pattern = r'\d'   # d is a special character which means digits
regex_pattern = r'\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern,txt)
print(matches)


# In[52]:


# Period(.)

#regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
#regex_pattern = r'[a].+'  # . any character, + any character one or more times 
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
match = re.findall(regex_pattern,txt)
print(match)


# In[54]:


txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''

regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional

matches = re.findall(regex_pattern, txt)
print(matches)  


# In[ ]:


### Quantifier in RegEx

#We can specify the length of the substring we are looking for in a text, using a curly bracket. Let us imagine, we are interested in a substring with a length of 4 characters:


txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']


### Cart ^

* Starts with
  

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']


* Negation

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

## ðŸ’» Exercises: Day 18

### Exercises: Level 1
# 1. What is the most frequent word in the following paragraph?
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.


```sh
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
```

#2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.


points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12


### Exercises: Level 2

#1. Write a pattern which identifies if a string is a valid python variable

    """
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    """

### Exercises: Level 3

#1. Clean the following text. After cleaning, count three most frequent words in the string.


    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
  #  I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    


# In[11]:


a = {'a':1, 'b':2}
b = {'c':3, 'd':4}
c1 = a, b
c2 = {**a, **b}
print(c1)
print(c2)

