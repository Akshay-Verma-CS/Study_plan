class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        m = {}
        i = 0
        j = 0
        maxLen = 0
        while j < len(s):
            if s[j] in m and m[s[j]] > i:
                i = m[s[j]]
            maxLen = max(maxLen,j - i + 1)
            m[s[j]] = j + 1
            j+=1
        return maxLen