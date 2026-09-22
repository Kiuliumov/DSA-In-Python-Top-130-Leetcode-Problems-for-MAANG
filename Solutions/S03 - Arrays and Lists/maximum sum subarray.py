class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        s = nums[0]
        m = nums[0]

        for i in range(1, len(nums)):
            s = max(nums[i], s + nums[i])
            m = max(m, s)

        return m