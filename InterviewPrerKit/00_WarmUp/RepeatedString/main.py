#!/bin/python3
"""
HackerRank 
https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
  lenS = len(s)
  idxS = 0
  counterOfA = 0

  reptS = int(n/lenS)
  restS = int(n%lenS)

  for chr in s:
    if chr == 'a':
      counterOfA += 1
  
  counterOfA = counterOfA * reptS
  
  while idxS < restS:
    if s[idxS] == 'a':
      counterOfA += 1
    idxS += 1

  return counterOfA

        
# if __name__ == '__main__':
  # fptr = open(os.environ['OUTPUT_PATH'], 'w')
  # n = int(input())
  # ar = list(map(int, input().rstrip().split()))
n = 10
s = "aba"
result = repeatedString(s, n)
print(result)
  # fptr.write(str(result) + '\n')
  # fptr.close()
    