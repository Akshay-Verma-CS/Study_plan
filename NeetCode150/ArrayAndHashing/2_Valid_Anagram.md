# Intuition
the frequency of characters should be same in both string.

# Approach
if both have different length then they will definitely not have similar frequency then no need to check each string
then Counter in python gives a map of frequency of each character
e.g Counter("abcb") => Counter({"a":1,"b":2,"c":1})
if both maps are similar it means the frequency of each character in s is similar to frequency of each character in t.

# Complexity
- Time complexity:
Counter has O(n) complexity for creation

the soln is O(2n)

which will be O(n) by removing constant

- Space complexity:
O(2n)
# Code
```
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        if ns != nt:
            return False
        return Counter(s) == Counter(t)   
        
```