
##### Types of values
- strings are immutable, slicing of strings, concatenating strings
- int vs float: division always produces a float
- boolean: True/False {not, and, or}
- comparisons: ==, !=, <=, >=
- Lists: 
  - sequence of values, need not be uniform
  - extract values by position, can be sliced
  - for lists, a single position returns a value, slice returns a list
  - list can contain other lists - nesting
  - lists are mutable
- for immutable values, assignment makes a fresh copy of a value
- for mutable values, assignment does not make a fresh copy
- How can we make a copy of a list: take a full slice - list1[:]
- list1 == list2 (two different list with same values)
- list2 is list3 ( list2 and list3 refer to same object)
- concatenation(+) always produces a new list  
- numeric 0 is False, empty sequence "", [], is False - everything else is True
- loops: for i in [1,2,3,4]:


## Links
* https://docs.python.org/3/tutorial/index.html
* Dive into Python 3, Mark Pilgrim
http://www.diveintopython3.net/
* Think Python, 2nd Edition, Allen B. Downey
http://greenteapress.com/wp/think-python-2/
