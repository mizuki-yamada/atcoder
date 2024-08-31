# 3.1 素数判定法
# 2 以上の整数 N に対し、N が素数であれば true、素数でなければ false を返す関数
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n=int(input())
if isPrime(n):
    print("素数です")
else:
    print("何かで割り切れます")

def isPrime2(n):
    LIMIT=int(n**0.5)
    for i in range(2,LIMIT+1):
        if n % i == 0:
            return False
    return True

if isPrime(n):
    print("素数です")
else:
    print("何かで割り切れます")

# 約数列挙
def yakusuuRekkyo(n):
    ans=[]
    LIMIT=int(n**0.5)
    for i in range(1,LIMIT+1):
        if n % i == 0:
            ans.append(i)
            # //でわると商が整数だけのものを求めることができる
            if n//i != i:
                ans.append(n//i)
    ans.sort()
    print(*ans)
yakusuuRekkyo(n)

# 3.1.2
def main(n):
    ans=[]
    LIMIT=int(n**0.5)
    for i in range(2,LIMIT+1):
        while n % i == 0:
            n/=i
            ans.append(i)
    # 最後に残る数字
    if n >= 2:
        ans.append(int(n))
    print(*ans)
main(n)