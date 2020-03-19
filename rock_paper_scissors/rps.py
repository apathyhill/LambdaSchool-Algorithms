#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  choices = ["rock", "paper", "scissors"]
  arr = []
  if n <= 0:
    return [[]]
  for i in choices:
    arr += [[i]+j for j in rock_paper_scissors(n-1)]
  return arr


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')