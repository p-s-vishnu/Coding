from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Time: 
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

    def remove_duplicates(self, nums):
        nums[:] = sorted(list(set(nums)))
        return len(nums)