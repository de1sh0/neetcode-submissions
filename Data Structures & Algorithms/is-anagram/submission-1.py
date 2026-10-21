class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Create a frequency dictionary for characters in string s
        freq = {}
        
        # Count the frequency of each character in s
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        
        # Decrease the frequency based on characters in t
        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        return True
        