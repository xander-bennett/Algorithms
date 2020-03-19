#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  selections = ['rock','paper','scissors']
  combinations = []
  if n <= 0:
    return [[]]
  if n == 1:
    return [[i] for i in selections]
  else:
    for j in rock_paper_scissors(n-1):
      combinations.append((j + [selections[0]]))
      combinations.append((j + [selections[1]]))
      combinations.append((j + [selections[2]]))
    return combinations


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')