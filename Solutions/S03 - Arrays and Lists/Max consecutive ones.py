class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current_streak = 0
        max_streak = 0
        for n in nums:
            if n == 1:
                current_streak += 1
                max_streak = current_streak if current_streak > max_streak else max_streak
                continue
            current_streak = 0
        return max_streak