class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        # return false if lengths of the 2 strings aren't equal
        if len(s) != len(t):
            return False
        
        # checks if sorted strings match 
        return sorted(s) == sorted(t)