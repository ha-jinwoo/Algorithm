# S = input()
# cnt = 0
# from itertools import permutations
# S = set(''.join(i) for i in permutations(S))
# for s in S:
#     last_word = s[0]
#     for word in s[1:]:
#         if word == last_word:
#             break
#         last_word = word
#     else:
#         cnt += 1
        
# print(cnt)

from math import factorial
from collections import Counter
from itertools import permutations
import sys
input=sys.stdin.readline
s=input().rstrip('\n')
tmp=[]
c=Counter(s)
res=0
for sub in permutations(s,len(s)):
    for i in range(1,len(sub)):
        if sub[i]==sub[i-1]:
            break
    else:
        res+=1
for k in c.values():
    res//=factorial(k)
print(res)