class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        dict = Counter(word)
        st = sorted(dict.values())
        res = float("inf")
        for i in range(len(st)):
            de = sum(st[:i])
            for j in range(len(st)-1,i,-1):
                if st[j]-st[i]>k:
                    de += st[j]-st[i]-k
                else:
                    break
            res = min(de,res)
        return res