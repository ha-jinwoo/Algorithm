# 방법 1. 내방법
# def first(num) :

#   n = num
#   for i in str(num) :
#     n+=int(i)
#   if n<10000 :
#     solve(n)

# def solve(num) :
#   l[num] = True
#   n = num
#   for i in str(num) :
#     n+=int(i)
#   if n<10000 :
#     solve(n)

# l = [False for i in range(10000)]
# for i in range(1,10000) :
#   if not l[i] : 
#     first(i)
# for i in range(1,10000) :
#   if not l[i] : print(i)

#방법 2. in 탐색 사용 (log n)
# a=[]
# for x in range(1,10001):
#     s=x
#     for y in str(s):
#         s += int(y)
#     a.append(s)
# for z in range(1,10001):
#     if z not in a:
#         print(z)

#방법 3. 차집합 set 사용

# set_1 = set(range(1,10001))
# set_2 = set()

# for i in range(1,10001) :
#   for j in str(i) :
#     i+=int(j)
#   set_2.add(i)

# set_3 = set_1-set_2

# for i in sorted(set_3):
#   print(i)

# a = set(range(1,10001))
# def f(a):
#    s = str(a)
#    for i in s:
#       a += int(i)
#    return a
# b = set(map(f,a))
# c = sorted(a-b)
# for i in c:
#    print(i)


list_2 = []
for i in range(1,10001) :
  for j in str(i) :
    i+=int(j)
  list_2.append(i);

for i in range(1,10001) :
  if i not in list_2 :
    print(i)

    # a=[]
# for x in range(1,10001):
#     s=x
#     for y in str(s):
#         s += int(y)
#     a.append(s)
# for z in range(1,10001):
#     if z not in a:
#         print(z)