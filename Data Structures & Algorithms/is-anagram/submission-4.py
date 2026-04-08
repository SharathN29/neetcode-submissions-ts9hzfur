class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}
        for c in s:
            if c not in char_count: 
                char_count[c] = 1
            else:
                curr_count = char_count[c]
                char_count[c] = curr_count + 1
        
        for c in t:
            if c not in char_count: 
                char_count[c] = 1
            else:
                curr_count = char_count[c]
                char_count[c] = curr_count - 1

        for val in char_count.values():
            if val != 0:
                return False
        
        return True