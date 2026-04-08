class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        
        for c in t:
            char_count[c] = char_count.get(c, 0) - 1

        return all(val == 0 for val in char_count.values())