N, K = map(int, input().split())
A=list(map(int,input().split()))
A1=A[:-K]
A2=A[-K:]
print(*A2,*A1)