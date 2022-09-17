### Problem Statement #######
#https://leetcode.com/problems/unique-paths

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return math.factorial(m + n - 2) // (math.factorial(m-1) * math.factorial(n-1))

### Explanation ########3

# The problem looks very intimidating first, but rather it's very simple. Note down the requirement is we can only take right and down, whatever path we choose
# we will have same number of rights and downs in every path, for example in the case of 3x2 grid, we will have precisely 2 downs and 1 right in every path as RDD, DDR
# and DRD. So now  we know if we have MxN grid then there are M-1 downs and N-1 rights. Thus we have to find all unique arrangements, which is very each if you 
# know fundamental counting principal. 
