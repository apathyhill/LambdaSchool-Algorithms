#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  L = len(items)
  cache = [[{"Value":0, "Chosen":[]} for i in range(capacity+1)] for j in range(L+1)] 
  for i in range(L+1): 
    for j in range(capacity+1): 
      if i == 0 or j == 0:
        pass
      elif items[i-1].size <= j:
        new_val = cache[i-1][j-items[i-1].size]["Value"] + items[i-1].value
        new_chosen = cache[i-1][j-items[i-1].size]["Chosen"] + [items[i-1].index]
        if new_val > cache[i-1][j]["Value"]:
          cache[i][j]["Value"] = new_val
          cache[i][j]["Chosen"] = new_chosen
        else:
          cache[i][j] = cache[i-1][j]
      else: 
        cache[i][j] = cache[i-1][j]
  return cache[L][capacity]
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')