class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        if n == 1:
            return s
            
        l = list(range(len(s)))

        am = [
            l[0::2*n-2],
            sum([
                sorted(l[i+1::2*n-2] + l[(i+1)+2*n-2-2*(i+1)::2*n-2])
                for i in range(n-2)
            ], []),
            l[n-1::2*n-2]
        ]

        return ''.join([s[i] for i in sum(am, [])])
        