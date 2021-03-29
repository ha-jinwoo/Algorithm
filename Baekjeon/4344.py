# 평균은 넘겠지

for i in range(int(input())):
  n,*num = [*map(int,input().split())]
  average = sum(num) / len(num)
  count = 0
  for i in num :
    if i > average :
      count+=1
  print(format(count/len(num)*100,"0.3f")+'%')
  
