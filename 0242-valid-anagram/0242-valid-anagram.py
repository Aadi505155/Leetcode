Problem Name: Valid Anagram (LeetCode 242)

Pattern Used: Frequency Counting / Hash Map (Counter)

Key Idea: First, check if both strings have the same length. If they don't, they can't be anagrams, so return False immediately. 
Then, use Python's Counter to count how many times each character appears in both strings and see if the counts match.
                                                                                                  
Time Complexity: O(n) (where $n$ is the length of the strings, because counting characters takes linear time)
                                                                                                  
Space Complexity: $O(n)$ (to store the unique characters and their counts in the hash maps)


from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)    



        
