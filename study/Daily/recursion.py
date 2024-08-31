# 再帰を学ぶ
"""
ポイント
- 関数の仕様を明確にする
    - 終了条件を考える、みたいな話とつながる
- 既に実装済みであるかのように考える
    - returnに関数が含まれるので、実装されている前提で考えるのが考えやすい、という理論

"""
memo = []

def memo(n):
    memo=  [0]* (n+1)
    print(memo)
    if (n == 0):
        memo[0] = 0
    elif (n == 1):
        memo[1] = 0
    elif (n == 2):
        memo[2] = 1
    else:
        if (memo[n] != 1):
            return memo[n]
        else:
            memo[n] = memo[n - 1] + memo[n - 2] + memo[n - 3]
            print(memo)

memo(10)

# def main():
#     memo = [-1] * 10
#     ans = memo(10)
#     # print(ans)


# def function(n):

#     ans = 0
#     if (n == 0):
#         ans = 0
#     elif (n == 1):
#         ans = 0
#     elif (n == 2):
#         ans = 1
#     else:
#         ans = function(n - 1) + function(n - 2) + function(n - 3)
#     return ans

# main()
