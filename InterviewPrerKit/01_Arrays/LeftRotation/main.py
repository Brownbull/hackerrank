#!/bin/python3
"""
HackerRank 
Warm-up Challenges
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""
import math
import os
import random
import re
import sys
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
# Complete the rotLeft function below.
def rotLeft(a, d):
  retArr = a[:]
  lenArr = len(a)

  for i in range(0, lenArr):
    pos = (i - d) if i >= d else lenArr + i - d
    retArr[pos] = a[i]
  return retArr

n = 5
d = 4
arr = [1,2,3,4,5]
result = rotLeft(arr, d)
for a in result:
  print(str(a))