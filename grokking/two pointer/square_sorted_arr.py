from typing import List


class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        out = []
        while l <= r:
            if nums[l]**2 > nums[r]**2:
                out.insert(0, nums[l]**2) 
                l += 1
            else:
                out.insert(0, nums[r]**2) 
                r -= 1
        return out