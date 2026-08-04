class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter 

        # if Counter(s)==Counter(t):
        #     return True
        # return False
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)