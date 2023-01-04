t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    prices = sorted(list(map(int, input().split())))
    g1, g2 = [prices[:m],prices[m:]], [prices[-m:],prices[:-m]]
    #print(g1)
    #print(g2)
    x = abs(sum(g1[1])-sum(g1[0]))
    y = abs(sum(g2[1])-sum(g2[0]))
    print(x) if x>=y else print(y)