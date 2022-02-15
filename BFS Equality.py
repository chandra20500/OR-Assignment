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
    x = float(input())
    l1.append(x)
  A.append(l1)
  print(A)

##### Constant matrix #####

B = []
print("Enter the constants of constraint equation: ")
for i in range(0, n2):
  x = float(input())
  B.append(x)

##### Implementation of simplex method #####

from scipy.optimize import linprog
res = linprog(C, A_eq=A, b_eq=B, options={"disp": True})
print(res)