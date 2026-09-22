class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        s = 0
        m = 0
        for n in nums:
            if s + n < 0:
                s = 0
                continue
            s += n
            if s > m:
                m = s
        return m