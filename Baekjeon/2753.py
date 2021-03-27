a = int(input())
print(int(a%4 == 0 and not a%100 == 0 or a%400==0))
