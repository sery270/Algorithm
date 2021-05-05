from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combi = list(combinations(nums, 2))
        # print(combi)
        for c in combi:
            if target == c[0] + c[1]:
                if nums.index(c[0]) == nums.index(c[1]):
                    return [nums.index(c[0]), nums.index(c[1], nums.index(c[0])+1)]
                return [nums.index(c[0]), nums.index(c[1])]