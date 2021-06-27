
'''
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1'''


class Solution:
    def reverse(self, x: int) -> int:
    #def reverse (x):
        sum = 0     #initialization
        sign = 1    
        if x < 0:       #condition_1
            sign = -1
            x= x * sign
            
        while x > 0:    #condition_2
            rem = x % 10    #Determining last digit -> 123%10=3 || 12%10=2 || 1%10=1
            sum = sum * 10 + rem    # 3 as sum=0 || 30+2=32 || 320+1=321
            x = x // 10    #123//10=12 || 12//10=1
            
        if not -2147483648< sum <2147483648:    #constraint
            return 0
        return sign * sum   
