############ PROBLEM STATEMENT ##############################
# https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_check_dictionary = {}
        output_list = []

        for index, element in enumerate(nums):
            if target - element in sum_check_dictionary:

                output_list = [sum_check_dictionary[target - element], index]
                break
            
            else:

                sum_check_dictionary[element] = index
        return output_list


############ Explanation #############33

# In order to find two elements whose sum equal the target, I need to find if first element is in the list, then check for target - first_element in the list
 