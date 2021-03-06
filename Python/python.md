
vdo 16: https://www.youtube.com/watch?v=J_Cw3G5v460&index=10&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf
##### Types of values
- strings are immutable, slicing of strings, concatenating strings
- int vs float: division always produces a float
- boolean: True/False {not, and, or}
- comparisons: ==, !=, <=, >=
- List: 
  - sequence of values, need not be uniform
  - extract values by position, can be sliced
  - for lists, a single position returns a value, slice returns a list
  - list can contain other lists - nesting
  - lists are mutable
  - list.append(x), list.remove(x), l.sort(), l.reverse(), l.index(x), l.rindex(x)
  - list.extend(list2)
  - x in list returns True if x is found in list
- for immutable values, assignment makes a fresh copy of a value
- for mutable values, assignment does not make a fresh copy
- How can we make a copy of a list: take a full slice - list1[:]
- list1 == list2 (two different list with same values)
- list2 is list3 ( list2 and list3 refer to same object)
- concatenation(+) always produces a new list  
- numeric 0 is False, empty sequence "", [], is False - everything else is True
- loops: for i in [1,2,3,4]:
- functions:
  - passing values - mutable and immutable
- range:
  - range(i, j), range(j), range(i,j,k)
 
 ##### Array vs List
 - Array
    - Single block of memory, elements of uniform type, indexing is fast - constant i, inserting in b/w is expensive
 - List
    - Values scattered in memory, each element points to the next - linked list, flexible size, accessing cost is proportional to i, inserting or deleting an element is easy
  
  
 
 ```
# find all prime numbers upto n
def factors(n):
    fl =[];
    for i in range(1, n+1):
        if n%i == 0:
            fl = fl + [i]
    return (fl)    

def isprime(n):
    return(factors(n) == [1,n])

def findprime(n):
    primelist = []
    for i in range(1, n+1):
        if isprime(i):
            primelist = primelist + [i]
    return primelist 

print(findprime(10))
```
  
 ### decorators
 ```
 import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
 ```  
  
  
  
  

## Links
* https://docs.python.org/3/tutorial/index.html
* Dive into Python 3, Mark Pilgrim
http://www.diveintopython3.net/
* Think Python, 2nd Edition, Allen B. Downey
http://greenteapress.com/wp/think-python-2/
* https://realpython.com/primer-on-python-decorators/
