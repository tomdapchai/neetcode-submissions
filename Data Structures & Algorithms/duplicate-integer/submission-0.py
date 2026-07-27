class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap: dict(int, list[int]) = defaultdict(list)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)

            if len(hashmap[nums[i]]) > 1:
                return True
        
        return False
