#!/usr/bin/env python
# coding: utf-8
1. What does an empty dictionary code look like?
ANS-

An empty dictionary's code in Python looks like this: {}. 
It consists of a pair of curly braces with nothing inside, which indicates that the dictionary is empty.2. What is the value of a dictionary value with the key 'foo'and the value 42?
ANS-

If a dictionary has a key 'foo' with the value 42, then the value of the dictionary at key 'foo' is 42.

In Python, dictionaries are used to store key-value pairs. Each key in the dictionary maps to a specific value, and you can access the value associated with a particular key by using the key as an index in the dictionary.

For example, if spam is a dictionary with the key-value pair {'foo': 42}, you can access the value 42 associated with the key 'foo' using the following syntax:

value = spam['foo']

This will assign the value of 42 to the variable value.
3. What is the most significant distinction between a dictionary and a list?

ANS-

Storage of values: A dictionary stores values by associating them with keys, while a list stores values by assigning them to positions in a sequence.

Accessing values: In a list, elements are ordered and accessed by their position or index within the list. In contrast, dictionary elements are not ordered, and they are accessed by their keys, which can be of any hashable type.

Duplicates: While lists allow for duplicates, dictionaries require unique keys, since a key can only be associated with a single value.

Mutability: Both dictionaries and lists are mutable, which means that their contents can be changed. However, the way in which their contents are changed differs. For lists, elements can be added, removed, or modified at specific positions. For dictionaries, values can be added, removed, or modified by specifying their associated keys.

Usage: Dictionaries are typically used for lookup operations, where a value is retrieved based on a corresponding key. Lists, on the other hand, are used for sequential operations, where elements are accessed and processed in a specific order.
4. What happens if you try to access spam['foo']  if spam is {bar':100}?
ANS-

This is because spam['foo'] is trying to access the value associated with the key 'foo' in the dictionary spam,
but there is no key 'foo' in the dictionary, only a key 'bar'. 
Therefore, Python raises a KeyError to indicate that the key you are trying to access does not exist in the dictionary.5. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and
&#39;cat&#39; in spam.keys()?

ANS-
The expressions 'cat' in spam and 'cat' in spam.keys() are equivalent in their behavior and would produce the same result. Both expressions check whether the string 'cat' is a key in the dictionary spam.

In Python, when you use the in operator with a dictionary, it checks whether the specified value is a key in the dictionary, not a value in the dictionary. Therefore, 'cat' in spam and 'cat' in spam.keys() both check if 'cat' is a key in spam.

The keys() method returns a list of all the keys in a dictionary, so 'cat' in spam.keys() explicitly checks if 'cat' is in that list of keys. However, because the in operator checks if a value is in a list, it is not necessary to explicitly call keys() to check if a key exists in the dictionary.



6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
'cat' in spam.values()?

ANS-

The expressions 'cat' in spam and 'cat' in spam.values() have different behaviors.

'cat' in spam checks whether 'cat' is a key in the dictionary spam. 
If 'cat' is a key in spam, the expression will return True. 
If 'cat' is not a key in spam, the expression will return False.

On the other hand, 'cat' in spam.values() checks whether 'cat' is a value in the dictionary spam. 
If 'cat' is a value in spam, the expression will return True. 
If 'cat' is not a value in spam, the expression will return False.

For example, suppose spam is a dictionary with the following key-value pairs: {'name': 'Alice', 'age': 30, 'pet': 'cat'}.

Then, 'cat' in spam would return False because 'cat' is not a key in the dictionary, while 'cat' in spam.
values() would return True because 'cat' is a value associated with the key 'pet'.7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'

Ans-
spam.setdefault('color', 'black')8. How do you 'pretty print' dictionary values using which module and function?
# In[3]:


#ANS-
import pprint

my_dict = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}

pprint.pprint(my_dict)


# In[ ]:





# In[ ]:





# In[ ]:




