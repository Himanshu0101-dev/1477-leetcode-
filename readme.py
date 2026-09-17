class Solution:
    def minSumOfLengths(self, arr, target: int) -> int:
        n = len(arr)
        prefix = {0: -1}  # prefix sum -> index
        s = 0
        best = [float('inf')] * n
        ans = float('inf')

        for i in range(n):
            s += arr[i]
            if s - target in prefix:
                j = prefix[s - target]
                length = i - j
                if j >= 0:
                    ans = min(ans, length + best[j])
                best[i] = length if i == 0 else min(best[i-1], length)
            else:
                best[i] = best[i-1] if i > 0 else float('inf')
            prefix[s] = i

        return -1 if ans == float('inf') else ans
