class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_map = {}

        for n in nums:
            if n not in count_map:
                count_map[n] = 0
            count_map[n] += 1
        
        appear_more = []
        for n, v in count_map.items():
            if v > len(nums) / 3:
                appear_more.append(n)
        return appear_more
