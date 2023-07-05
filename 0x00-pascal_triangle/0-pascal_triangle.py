#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    ''' 
     Function to find Pascal's Triangle integers 
  
         Parameters: 
             n (int): The number of row's of Pascal's triangle 
  
         Returns: 
             pascal_triangle (list): Binary string of the sum of a and b 
     '''
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
 
