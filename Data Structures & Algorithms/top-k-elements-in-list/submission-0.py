class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] +=1
        
        counter_sorted = sorted(counter, key=counter.get, reverse=True)
        
        return counter_sorted[:k]
        