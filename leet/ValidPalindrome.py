class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = []
        for i in s:
            if i.isalnum():
                normalized.append(i.lower())
        normalized = "".join(normalized)
        b = 0
        e = len(normalized)-1
        while b < e:
            if normalized[b] != normalized[e]:
                return False
            else:
                b += 1
                e -= 1
        return True 