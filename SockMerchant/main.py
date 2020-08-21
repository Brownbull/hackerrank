#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
  pairs = 0
  socksOnFile = []
  for sock in ar:
    if sock in socksOnFile:
      socksOnFile.remove(sock)
      pairs += 1
    else:
      socksOnFile.append(sock)
  return pairs


# if __name__ == '__main__':
  # fptr = open(os.environ['OUTPUT_PATH'], 'w')
  # n = int(input())
  # ar = list(map(int, input().rstrip().split()))
n = 9
ar = [10,20,20,10,10,30,50,10,20]
result = sockMerchant(n, ar)
print(result)
  # fptr.write(str(result) + '\n')
  # fptr.close()
    