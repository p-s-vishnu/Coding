from typing import List


class Solution:
    def two_sum(self, arr: List[int], target: int) -> List[int]:
        """
        If array is sorted
        Time: O(n)
        Space: O(1)
        """
        left, right = 0, len(arr) - 1
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == target:
                return [left, right]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return []

    def two_sum2(self, nums: List[int], target: int) -> List[int]:
        """
        If the array is not in sorted order
        Time: O(n)
        Space: O(n)
        """
        d = {}
        for idx, n in enumerate(nums):
            if n not in d:
                d[target - n] = idx
            else:
                return [d[n], idx]
        return []