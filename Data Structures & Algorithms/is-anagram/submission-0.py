class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}

        #load hashmap for s
        for ch in s:
            #if found add + 1 to the value. else 0
            freq[ch] = freq.get(ch, 0 ) + 1
        
        #reduce the count using t
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1.

 # Step 3: Check all zero
 #Check if all values in the dictionary are 0”

#If yes → return True
#If any value ≠ 0 → return False
        return all(value == 0 for value in freq.values())