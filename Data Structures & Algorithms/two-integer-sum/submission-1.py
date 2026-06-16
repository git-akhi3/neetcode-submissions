class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sets = {}
        for i in range(len(nums)):
            var = target - nums[i]

            if var in sets:
                print(var)
                return [sets[var], i]
            
            sets[nums[i]] = i