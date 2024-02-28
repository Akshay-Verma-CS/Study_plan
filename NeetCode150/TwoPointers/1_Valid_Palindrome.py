import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^A-Za-z0-9]+','',s).lower()
        l,r=0,len(string)-1
        while l<=r:
            if string[l]!=string[r]:
                return False
            else:
                l+=1;r-=1
        return True