# 최대값
l = [int(input()) for i in range(9)]
# max2 = 0
# for i in range(9) :
#   n = int(input())
#   if max2 < n:
#     max2 = n
#     index = i + 1
# print(max2)
# print(index)

print(max(l),l.index(max(l))+1,sep = '\n')