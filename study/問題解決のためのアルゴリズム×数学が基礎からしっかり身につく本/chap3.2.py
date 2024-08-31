# ユークリッドの互除法
# m,n = map(int, input().split())
def gcd(m, n):
    # m or nが0になればループは終わる
    # &はビット演算子扱いになる。論理演算の場合はand
    while m >= 1 and n >= 1:
        # m,nの大小で場合わけ
        if m > n:
            m = m % n
        else:
            n = n % m
    # 最終的にはどちらかが0なので、0じゃない方をreturn
    if m > 0:
        return m
    else:
        return n


# 3.2.2 N個の整数の最大公約数を求める
N = int(input())
A = list(map(int, input().split()))
ans = gcd(A[0], A[1])
for i in range(2, len(A)):
    ans = gcd(ans, A[i])
# print(ans)
# 3.2.3 最小公倍数を計算する
# 最小公倍数を返す関数
def lcm(A, B):
	return int(A / gcd(A, B)) * B
# 最初の2つの最小公倍数
ans=lcm(A[0],A[1])
for i in range(2, len(A)):
    # 前回結果と1つ隣の要素の最小公倍数を求めて更新していく
    ans = lcm(ans, A[i])
print(ans)