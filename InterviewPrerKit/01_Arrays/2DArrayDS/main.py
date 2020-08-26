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
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Complete the hourglassSum function below.
def hourglassSum(arr):
  posX = 0
  posY = 0

  lenX = len(arr)
  lenY = len(arr[0])
  limitX = lenX - 2
  limitY = lenY - 2

  sumHourGlass = 0
  maxHourGlass = 'F'

  for x in range(0, limitX):
    for y in range(0, limitY):
      sumHourGlass = \
        arr[x][y] + arr[x][y+1] + arr[x][y+2] + \
        arr[x+1][y+1] + \
        arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
      if maxHourGlass == 'F':
        maxHourGlass = sumHourGlass
      else:
        maxHourGlass = max(maxHourGlass, sumHourGlass)
  return maxHourGlass

  #     print("{},{}: {}".format(x,y, arr[x][y]), end="\t")
  #   print("")

  # print("lenX: {}\tlenY: {}".format(lenX, lenY))

arr = [
  [1 ,1 ,1 ,0 ,0 ,0],
  [0 ,1 ,0 ,0 ,0 ,0],
  [1 ,1 ,1 ,0 ,0 ,0],
  [0 ,0 ,2 ,4 ,4 ,0],
  [0 ,0 ,0 ,2 ,0 ,0],
  [0 ,0 ,1 ,2 ,4 ,0]
  ]
arr = [
[-1 , 1 ,-1 , 0 , 0 ,0],
[ 0 ,-1 , 0 , 0 , 0 ,0],
[-1 ,-1 ,-1 , 0 , 0 ,0],
[ 0 ,-9 , 2 ,-4 ,-4 ,0],
[-7 , 0 , 0 ,-2 , 0 ,0],
[ 0 , 0 ,-1 ,-2 ,-4 ,0]
  ]
result = hourglassSum(arr)
print(result)

    