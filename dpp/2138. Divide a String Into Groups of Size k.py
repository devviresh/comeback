class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        for i in range(0, n-k+1, k):
            res.append(s[i : i + k])
        if n % k != 0:
            res.append(s[n - (n % k) :] + fill * (k - (n % k)))
        return res
