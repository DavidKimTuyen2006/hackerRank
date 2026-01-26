class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        b = 0
        e = b+1 
        while True:
            if numbers[b] + numbers[e] == target:
                return [b+1,e+1]
            elif e < len(numbers) - 1:
                e += 1
            else:
                b += 1
                e = b + 1 
## solutions này đúng nhưng là giải pháp brute force nên bị runtime 
## giải pháp khác 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        b = 0
        e = len(numbers) - 1
        while True:
            if numbers[b] + numbers[e] == target:
                return [b+1, e+1]
            elif numbers[b] + numbers[e] > target:
                e -= 1
            else: 
                b += 1