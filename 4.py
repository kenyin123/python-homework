import math
num = int(input('Please enter a number:'))
new_num = num
list = []

while num<=0:
    print('error!please enter again!')
    num=int(input())
while num==1:
    print('1既不是质数也不是合数！Please enter again!')
    num=int(input())
m = int(math.sqrt (num))+1
i=2
while i<=m:
    while new_num % i == 0:
        list.append(i)
        new_num=new_num/i
    i=i+1
if new_num>1:
    list.append(new_num)
print(list)
    
