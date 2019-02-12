## Algorithms
- Euclid's algorithm
```
# Find gcd of two numbers m, n
def gcd(m,n):
    if m < n:
        (m,n) = (n,m)
    if (m%n) == 0:
        return(n)
    else:
        return (gcd(n, m%n))
  ```  
- Binary Search - O(log n)

## Notes
```
# Find the intersection of two list
list1 = [8, 6, 10, 1, 2]
list2 = [5, 6, 2, 55, 99]
print (list(set(list1) & set(list2))) 
```
## Efficiency 
- measures time taken by an algorithm as a function T(n) with respect to input size n
- worst case efficiency - when value is not found
- BigO notation
- Linear scan is O(n) for arrays and lists
- binary search - O(log n) for sorted arrays
- Polynomial time algorithm



## Links
- https://www.youtube.com/watch?v=bum_19loj9A
- https://www.youtube.com/watch?v=9MmC_uGjBsM&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf
- https://www.youtube.com/watch?v=92S4zgXN17o&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P
- https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
- https://www.youtube.com/watch?v=c1IW9S2bR2w&index=1&list=PLib7LoYR5PuDxi8TxxGKxMgf8b-jtoS3i
