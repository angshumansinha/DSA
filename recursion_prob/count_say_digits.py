#with recursion
from collections import Counter
digit={0:'Zero', 1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
response=[]
reverse=0
def say_digits(num):
    if num==0:
        return
    rem=num%10
    #print(digit[rem])
    num=num//10
    #print(num)
    say_digits(num)
    response.append(digit[rem])

say_digits(22334)
l1=list(Counter(response).values())
for x in 