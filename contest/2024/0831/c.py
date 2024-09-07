# a,b = map(int, input().split())
# ans=0
# if a==b:
#     ans=1
# elif a<=b:
#     if (a+b)%2==0:
#         ans=3
#     else:
#         ans=2
# else:
#     if (a+b)%2==0:
#         ans=3
#     else:
#         ans=2
# print(ans)

# n=int(input())
# list = []
# for i in range(n):
#     a,b=input().split()
#     list.append([int(a), b])
# L=[]
# R=[]
# # 左と右に分ける
# for i in list:
#     if "L" in i:
#         L.append(i[0])
#     if "R" in i:
#         R.append(i[0])
# l_ans=0
# r_ans=0
# for i in range(1,len((L))):
#     l_ans+=abs(L[i]-L[i-1])
# for i in range(1,len((R))):
#     r_ans+=abs(R[i]-R[i-1])
# print(l_ans+r_ans)

N=int(input())
# 整数が横一列で入力される場合。リストに格納する
A=list(map(int,input().split()))
# 当てはまる全要素をとりあえず列挙
ans=0
for l in range(1,N):
    print("l: ",l)
    print(ans)
    diff=A[l]-A[l-1]
    for r in range(1,N):
        print("r: ",r)
        if l==r:
            ans+=1
        elif r-l==1:
            ans+=1
        else:
            print("diff: ",diff)
            for i in range(l,r):
                print("i: ",i)
                if A[i+1]-A[i] == diff:
                    print("same diff" , A[i+1], ":", A[i])
                    ans+=1

print(ans)