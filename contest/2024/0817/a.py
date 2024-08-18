A, B, C = map(int, input().split())
if (B > C):
    if (C <= A <= B):
        print("Yes")
    else:
        print("No")
else:
    if (B < A < C):
        print("No")
    else:
        print("Yes")
