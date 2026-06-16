class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        # this map will store all the values in [ value , i ]
        # it will be used to compare the diff if it exsits in the map . 

        for i in range(len(nums)):
            # from 0 to 3
            var = nums[i]
            # 3 , 4
            diff = target - var
            # diff = 7 - 3 = 4  ,  7 - 4 = 3
            if diff in map :
                return [map[diff], i]
                # [0 , 1]
            
            # 3 : 0 
            map[var] = i