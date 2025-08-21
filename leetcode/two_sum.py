from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in number_dict:
                return [number_dict[comp], i]
            else:
                number_dict[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9

r = Solution().twoSum(nums, target)
print(r)
