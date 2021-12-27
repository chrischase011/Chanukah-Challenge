# Chanukah Challenge solved by Christopher Robin Chase 💖
def main():
   
    ans = 0
    c = 0
    s = "1 8"
    i, t = s.split()
    x = int(t)
    for b in range(x):
        b = b + 1
        c = (c + b)
        ans = c + x
        
    print(i, ans)


main()
