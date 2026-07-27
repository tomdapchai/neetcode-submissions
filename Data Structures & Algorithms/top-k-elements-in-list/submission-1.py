class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
           hashmap[n] += 1
        
        sort = sorted(hashmap.items(), reverse = True, key = lambda item: item[1])

        return [item[0] for item in sort[0:k]]