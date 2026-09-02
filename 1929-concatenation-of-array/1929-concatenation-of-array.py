Problem Name: Concatenation of Array

Pattern Used: Array Traversal

Key Idea:
Traverse the array twice and append every element
to the answer array.

Time Complexity: O(n)
Space Complexity: O(n)



class Solution(object):
    def getConcatenation(self, nums):
     ans = []
     for n in range(2):
        for n in nums:
            ans.append(n)
     return ans



    

        
        
