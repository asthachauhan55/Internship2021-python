#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input())
    if n%2!=0:
        print("Weird")
    if n%2==0 and (n in range (2,6) or n>20):
        print "Not",
        print "Weird"
    

