import sys
input=sys.stdin.readline
n,k=map(int,input().split())
cnt=0

while True:
    if n==1:break
    if n%k==0:
        n=n//k
    else:
        n-=1
    cnt+=1
print(cnt)