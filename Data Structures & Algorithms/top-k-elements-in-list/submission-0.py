
from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums).most_common(k)
        return [ num for num, _ in counts]
        
