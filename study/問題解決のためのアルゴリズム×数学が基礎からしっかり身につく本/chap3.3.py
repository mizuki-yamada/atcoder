# 3.3.3
# 再帰で階乗を書いてみる
def recursion (n):
    while n==1:
        recursion(n)
        n-=1
print