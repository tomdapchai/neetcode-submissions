class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        zero_pos = -1
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                zero_pos = i
            else:
                product *= nums[i]
        
        if zero_count > 0:
            zero_arr = [0] * len(nums)
            if zero_count == 1:
                zero_arr[zero_pos] = product
            return zero_arr


        return [int(product / n) for n in nums]