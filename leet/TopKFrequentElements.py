class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtb = {}
        for i in nums:
            if i not in hashtb:
                hashtb[i] = []
                hashtb[i].append(0)
            hashtb[i][0] += 1
        sortedHashtb = sorted(hashtb.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(0, k):
            result.append(sortedHashtb[i][0])
        return result
