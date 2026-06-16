class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # nums = [ 1, 2,2 , 3 , 4 ,5 ]
        hash = set()
        for n in nums :
            if n in hash :
                return True
            hash.add(n)

        return False

