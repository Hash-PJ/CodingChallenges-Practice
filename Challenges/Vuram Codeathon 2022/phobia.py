t = int(input())
ls = ""
for _ in range(t):
    n = int(input())
    if '17' in str(n) or n%17==0:
        ls += "Panic Attack\n"
    else:
        ls += "Happy Face\n"
print(ls)