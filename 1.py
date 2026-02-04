import numpy as np
a = []
b = []
for i in range(5):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(3):
    row = list(map(int, input().split()))
    b.append(row)
a = np.array(a)
b = np.array(b)
c = a @ b
print(c)