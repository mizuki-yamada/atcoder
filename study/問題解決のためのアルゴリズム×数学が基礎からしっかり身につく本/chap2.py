# 2.1.3
A=list(map(int,input().split()))
ans=1
for i in range(len(A)):
    ans*=A[i]
print(ans)

# ビット演算
a=14
b=11
print(a&b)
print(a|b)
print(a^b)