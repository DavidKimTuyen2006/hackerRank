class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        b = 0
        e = len(nums) - 1
        for i in range(0, len(nums)-1):
            while True:
                if i != b and i != e and nums[i] + nums[b] + nums[e] == 0:
                    tmp = []
                    tmp.append(nums[i])
                    tmp.append(nums[e])
                    tmp.append(nums[b])
                    ans.append(sorted(tmp))
                    b = 0
                    e = len(nums) - 1
                    break
                elif b == len(nums) - 1:
                    break                   
                elif e == b:
                    e = len(nums) -1
                    b += 1
                else:
                    e -= 1
        return ans
# cách này đã thành công như lại không đc accept vì đã xảy ra trùng lặp 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                 continue
            l = i + 1
            r = n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans
# cách này đã fix đc vấn đề trùng lặp cũng như thời gian giải ngắn hơn do k cần phải duyệt hết mãng