t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    ni = list(map(int, input().split()))
    unique = len(set(ni))
    if unique>=m:
        print('JANI')
    else:
        print('RAMYA')
