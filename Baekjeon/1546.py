#평균

n = int(input())
num = [*map(int,input().split())]
print( sum(num)*100/max(num)/len(num) )
