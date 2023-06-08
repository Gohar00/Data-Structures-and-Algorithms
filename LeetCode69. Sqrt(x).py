class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        start = 1
        end = x//2
        while (start <= end):
            mid = (start + end) // 2
    
            if (mid*mid == x):
                return mid
    
            if (mid * mid < x):
                start = mid + 1
                ans = mid
    
            else:

                end = mid-1
    
        return ans
 