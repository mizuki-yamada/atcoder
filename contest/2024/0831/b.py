n=int(input())
list = []
for i in range(n):
    a,b=input().split()
    list.append([int(a), b])
L=[]
R=[]
# 左と右に分ける
for i in list:
    if "L" in i:
        L.append(i[0])
    if "R" in i:
        R.append(i[0])
l_ans=0
r_ans=0
for i in range(1,len((L))):
    l_ans+=abs(L[i]-L[i-1])
for i in range(1,len((R))):
    r_ans+=abs(R[i]-R[i-1])
print(l_ans+r_ans)