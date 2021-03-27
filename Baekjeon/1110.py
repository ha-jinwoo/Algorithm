# 더하기 사이클

n = int(input())
check = n
count=0
while 1 :
  sum =  n//10+n%10
  n = n%10*10 + sum%10
  count+=1
  if check == n : break

print(count)