from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for text in strs:
            t = self.getFrequencyList(text)
            if t in map:
                map[t].append(text)
            else:
                map[t] = [text]
        return map.values()

    def getFrequencyList(self,text):
        l = [0]*26
        for c in text:
            l[ord(c)-ord('a')]+=1
        return tuple(l)