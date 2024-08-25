N=int(input())
A=list(map(int,input().split()))
count=0
positive_count = sum(1 for n in A if n > 0)

# ここを!=1にしていたので、TLEが発生した（全て0になる場合を見逃していた）
while positive_count > 1:
    A.sort(reverse=True)
    A[0]-=1
    A[1]-=1
    count+=1
    positive_count = sum(1 for n in A if n > 0)
print(count)