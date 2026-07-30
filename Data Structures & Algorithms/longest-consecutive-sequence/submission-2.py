class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_num = set(nums)
        nums = sorted(set_num)
        window: list[int] = []
        max_w = 1
        l_w = 1
        for i in range(len(nums) - 1):
            print(nums[i + 1], nums[i])
            if nums[i + 1] == nums[i] + 1:
                l_w += 1
            else:
                l_w = 1
            
            max_w = max(max_w, l_w)
        
        return max_w