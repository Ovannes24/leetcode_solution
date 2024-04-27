class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = len(s)
        lss = len(set(s))

        if ls==lss:
            return lss

        for i in range(lss):
            for j in range(ls-(lss-i)+1):
                ts = s[j:j+(lss-i):1]
                # print(ls, lss, i, j, ts)
                if len(set(ts)) == lss-i:
                    return lss-i

        return 0
