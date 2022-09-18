from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = len(nums)
        for i in range(len(nums)):
            
            if i >= k:
                break
                
            if nums[i] == val:
                
                while k != i:
                    k -= 1
                    if nums[k] != nums[i]:
                        nums[i] = nums[k]
                        break
        return k
            