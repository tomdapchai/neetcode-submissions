class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a + b + c = 0 => a + b = -c
        # O(n^2)
        nums.sort()
        print(nums)
        res: list[list[int]] = []
        for i in range(len(nums)):
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                if l == i:
                    l += 1
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                if r == i:
                    r -= 1
                if l >= r:
                    break
                if nums[l] + nums[r] + nums[i] == 0:
                    dup = False
                    for x in res:
                        x.sort()
                        tmp = [nums[l], nums[r], nums[i]]
                        tmp.sort()
                        if tmp == x:
                            dup = True
                    if not dup:
                        res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1                

        return res


        