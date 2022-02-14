import numpy as np
import scipy as sp

n = int(input("enter the number of variables: "))

##### Coefficient of maximizaton function #####

p_type = int(input("enter the type of problemns : 1 for max, 0 for min :"))

if p_type == 1:
  p_type = -1
elif p_type == 0:
  p_type = 1

C = []

print("enter coefficient of variables")

for i in range(0, n):
  x = int(input())
  x = p_type*x
  C.append(x)

##### coefficients of constraint matrix #####

n2 = int(input("enter the number of constraints eqs"))

A = []

for i in range(0, n2):
  l1 = []
  print("enter the coefficients of constraint equation: ")
  for j in range(0, n):
    x = int(input())
    l1.append(x)
  A.append(l1)

##### Constant matrix #####

B = []

for i in range(0, n2):
  x = int(input())
  B.append(x)

##### Implementation of revsed simplex method #####

from scipy.optimize import linprog
res = linprog(C, A_ub=A, b_ub=B, method='revised simplex', options={"disp": True})
print(res)