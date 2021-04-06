# count = 0
# def d (num) :
#   global count
#   if num < 100 : 
#     count+=1
#     return
#   sub = int(str(num)[1]) - int(str(num)[0]) 
#   for i in range(1,len(str(num))-1) :
#     if not sub == int(str(num)[i+1]) - int(str(num)[i]) :
#       return
#   count+=1

# for i in range(1,int(input())+1) :
#   d(i)
# print (count)

num = int(input())
hansu = 0

for n in range(1, num+1) :
  if n <= 99 : # 1부터 99까지는 모두 한수
    hansu += 1 
    
  else :     
    nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
    if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
      hansu+=1