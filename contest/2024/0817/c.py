N, K = map(int, input().split())
R=list(map(int, input().split()))
# 当てはまるリストを全列挙していくための配列
A=[0]*8 # Nはmax8なので、8個まで要素を入れれるように準備
# 要素を全列挙するための準備
for i in range(N):
    A[i]=R[i]
# Aの各要素に対して(range(A[0]))、1からA[i]の数字をCに配列として入れていく
C=[]
for i0 in range(A[0]):
    if(N==1):
        C.append([i0+1])
    else:
        for i1 in range(A[1]):
            if(N==2):
                C.append([i0+1,i1+1])
            else:
                for i2 in range(A[2]):
                    if(N==3):
                        C.append([i0+1,i1+1,i2+1])
                    else:
                        for i3 in range(A[3]):
                            if(N==4):
                                C.append([i0+1,i1+1,i2+1,i3+1])
                            else:
                                for i4 in range(A[4]):
                                    if(N==5):
                                        C.append([i0+1,i1+1,i2+1,i3+1,i4+1])
                                    else:
                                        for i5 in range(A[5]):
                                            if(N==6):
                                                C.append([i0+1,i1+1,i2+1,i3+1,i4+1,i5+1])
                                            else:
                                                for i6 in range(A[6]):
                                                    if(N==7):
                                                        C.append([i0+1,i1+1,i2+1,i3+1,i4+1,i5+1,i6+1])
                                                    else:
                                                        for i7 in range(A[7]):
                                                            C.append([i0+1,i1+1,i2+1,i3+1,i4+1,i5+1,i6+1,i7+1])
# print(C)
ans=[]
for c in C:
    if(sum(c)%K==0):
        ans.append(c)
for a in ans:
    print(*a)