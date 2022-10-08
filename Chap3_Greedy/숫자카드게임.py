import sys
input=sys.stdin.readline
n,m=map(int,input().split())
s=[sorted(list(map(int,input().split()))) for _ in range(n)]
mxnum=float('-inf')

for i in s:
    mxnum=max(i[0],mxnum)
print(mxnum)
