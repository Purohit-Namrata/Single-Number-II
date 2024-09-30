from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        b=0

        for i in nums:
            a=(a^i)&(~b)
            b=(b^i)&(~a)
        return a
    
s=Solution()
output=s.singleNumber([2,2,3,2])
print("Single number in the array is ",output)