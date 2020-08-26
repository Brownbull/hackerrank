#!/bin/python3
"""
HackerRank 
Warm-up Challenges
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
  lenC = len(c)
  idx = 0
  steps = 0

  while (lenC - 1) != idx:
    steps += 1
    if (lenC - (idx + 2)) > 0:
      if c[idx + 2] == 0:
        idx += 2
      else:
        idx += 1
    else: 
      idx += 1
  return steps

        
# if __name__ == '__main__':
  # fptr = open(os.environ['OUTPUT_PATH'], 'w')
  # n = int(input())
  # ar = list(map(int, input().rstrip().split()))
n = 7
s = [0,0,1,0,0,1,0]
result = jumpingOnClouds(n, s)
print(result)
  # fptr.write(str(result) + '\n')
  # fptr.close()
    