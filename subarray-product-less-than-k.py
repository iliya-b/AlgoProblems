from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        j = None
        P = None
        res = 0
        for i, n in enumerate(nums):
            if j is None:
                if n < k:
                    j = i
                    P = n
                    res += 1

                continue
            if n >= k:
                j = None
                P = None
                continue
            while P * n >= k and j < i:
                P //= nums[j]
                j += 1

            P *= n
            res += (i - j + 1)
        return res
