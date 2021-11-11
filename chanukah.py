# Chanukah Challenge solved by Christopher Robin Chase 💖
def main(n = int(input())):
    
    while(n != 0):
        ans = 0
        c = 0
        s = input()
        i, t = s.split()
        x = int(t)
        for b in range(x):
            '''
            if(x == 1):
                ans = x + 1
                break
            '''
            b = b + 1
            c = (c + b)
            ans = c + x
        
        print(i, ans)
        n = n - 1


main()
