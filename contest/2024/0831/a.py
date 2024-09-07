a,b = map(int, input().split())
ans=0
if a==b:
    ans=1
elif a<=b:
    if (a+b)%2==0:
        ans=3
    else:
        ans=2
else:
    if (a+b)%2==0:
        ans=3
    else:
        ans=2
print(ans)