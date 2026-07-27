class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            if hashmap[nums[i]] != [] and nums[i] + nums[hashmap[nums[i]]] == target:
                return [hashmap[nums[i]], i]
            hashmap[nums[i]] = i
            if hashmap[target - nums[i]] != [] and i != hashmap[target - nums[i]]:
                return [hashmap[target - nums[i]], i]
            