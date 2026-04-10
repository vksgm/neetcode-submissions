class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26 #Array

        #load hashmap for s
        for ch in s:
            #Go to the index corresponding to this character and increase its count
            # here ord() gives ASCII value so to normalize it, we subtract with ord('a') = 97
            # means it will be index specific 0th index -> z
            #                                 25th index ->z
            #then for the corresponding index increment the value with 1.
            freq[ord(ch) - ord('a')] += 1
        
        #reduce the count using t
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

 # Step 3: Check all zero
 #Check if all values in the dictionary are 0”

#If yes → return True
#If any value ≠ 0 → return False
        return all(value == 0 for value in freq)