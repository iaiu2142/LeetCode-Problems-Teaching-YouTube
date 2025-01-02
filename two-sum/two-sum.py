class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            u = target - nums[i]
            if u in dic:
                return [dic[u],i]
            dic[nums[i]] = i