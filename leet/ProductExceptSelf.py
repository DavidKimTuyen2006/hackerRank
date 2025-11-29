class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tich = nums[0]
        if nums[0] == 0:
            tichkhac0 = 1
        else:
            tichkhac0 = nums[0]
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
        for i in nums[1:]:
            tich *= i
            if i != 0:
                tichkhac0 *= i
        n = len(nums)
        if tich == 0:
            for i in range(0, n):
                if nums[i] == 0 and zero == 1:
                    nums[i] = tichkhac0
                else:
                    nums[i] = 0
        else:
            for i in range(0, n):
                tmp = nums[i]
                nums[i] = tich / nums[i]
        for i in range(0, n):
            nums[i] = int(nums[i])
        return nums
