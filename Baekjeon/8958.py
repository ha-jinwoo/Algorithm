for i in range(int(input())) : 
  sum = 0
  count = 0
  for j in input() :
    if j=='O'  :
      count+=1
      sum+=count
    else :
      count=0
  print(sum)