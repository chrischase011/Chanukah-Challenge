# Another implementation


n = int(input())

while(n != 0):
    x = int(input())
    i = 0
    f = 0
    answer = 0
    while(i != x):
       i = i + 1
       f = f + i
       answer = f + x

    print(answer)
    n = n-1
