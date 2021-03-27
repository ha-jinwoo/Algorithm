# 알람시계

a,b = map(int,input().split())
# print((a-(b<45)%24),(b-45)%60)
b-=45
if b<0:
  b+=60
  a-=1
  if a<0 :
    a+=24
print(a,b)
