Problem Name: Contains Duplicate (LeetCode 217)
Pattern Used: Hash Set / Array Traversal
Key Idea: Traverse the array and use a hash set to keep track of numbers we've already seen. If we hit a number that's already in the set, we found a duplicate.
Time Complexity: O(n)
Space Complexity: O(n)


class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)  
        return False      

                 

        
