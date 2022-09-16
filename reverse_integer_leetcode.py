######### PROBLEM STATEMENT ################33
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:

      sign = 1 if x>0 else -1
      x = sign *x
      output = 0 
      
      while x != 0:
        output = output*10 + x%10
        x = x // 10
      
      output = output * sign
      if (output <= 2**31 -1) and (output >= -2**31):
        return output
      else:
        return 0 
