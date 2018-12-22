class Solution(object):
    def largestSumOfAverages(self, A, K):
        cumulative = [0]
        for a in A: cumulative.append(cumulative[-1] + a)
        def average(i, j):
            return (cumulative[j] - cumulative[i]) / (j - i)

        N = len(A)

        # Default values account for K = 0
        dp = [average(i, N) for i in range(N)]

        # Since we already have answers for K = 0, we go from
        # 1 to K - 1
        for k in range(1, K):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]
