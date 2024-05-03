#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
  size=(len(a))
  iterate=True
  num=0
  while iterate==True:
      iterate=False
      for i in range(1,size):
          if a[i]<a[i-1]:
            a[i],a[i-1]=a[i-1],a[i]
            num+=1
            iterate=True
  print("Array is sorted in "+str(num)+" swaps.")
  print("First Element: "+str(a[0]))
  size-=1
  print("Last Element: "+str(a[size]))              
          

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)