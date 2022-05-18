nums = [1,1,1,1,1,1,0,0,1,1,1,1]
weird = [1,1,1,1,1,1,2,3,4,4,5,1,2,0,0] 
from itertools import groupby
a = [key for key, _group in groupby(nums)]
print(a)
print(sum(a[1:]))

b = [list(v) for k,v in groupby(weird, key = lambda x: x != 0) if k != 0]
print(len(b))
print(b[0][-1] - b[0][0] + b[1][-1])

