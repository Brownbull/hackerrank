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

# Complete the countingValleys function below.
def countingValleys(n, s):
  seaLevel = 0
  endOfHill = 1
  endOfValley = -1
  currentLvl = seaLevel
  hills = 0
  valleys = 0
  for chr in s:
    if chr == 'D':
      currentLvl += -1
    else:
      currentLvl += 1
      if currentLvl == seaLevel:
        valleys += 1
  return valleys
  # seaLevel = 0
  # endOfHill = 1
  # endOfValley = -1
  # currentLvl = seaLevel
  # hills = 0
  # valleys = 0
  # for chr in s:
  #   if chr == 'D':
  #     if currentLvl == endOfHill:
  #       hills += 1
  #     currentLvl += -1
  #   else:
  #     if currentLvl == endOfValley:
  #       valleys += 1
  #     currentLvl += 1
  # return valleys
        
# if __name__ == '__main__':
  # fptr = open(os.environ['OUTPUT_PATH'], 'w')
  # n = int(input())
  # ar = list(map(int, input().rstrip().split()))
n = 9
s = "UDDDUDUU"
result = countingValleys(n, s)
print(result)
  # fptr.write(str(result) + '\n')
  # fptr.close()
    