'''Objective
Today, we’re learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!
Task
Given an array, , of integers, print ‘s elements in reverse order as a single line of space-separated numbers.
Sample Input
4
1 4 3 2
Sample Output
2 3 4 1'''

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
m = map(str,arr[::-1])  #[::-1]->for reversing the list
 
print (" ".join(m))
