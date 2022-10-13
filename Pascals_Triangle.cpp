class Solution:
    def generate(self, n: int) -> List[List[int]]:        
        def helper(n):
            if n:
                helper(n-1)                 # generate above row first
                ans.append([1]*n)           # insert current row into triangle
                for i in range(1, n-1):     # update current row values using above row
                    ans[n-1][i] = ans[n-2][i] + ans[n-2][i-1]
        ans = []
        helper(n)
        return ans
