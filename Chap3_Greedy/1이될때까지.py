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

# 책 코드
n,k=25,5
res=0
while True:
    target=(n//k)*k
    res+=(n-target)
    n=target

    if n<k:break
    res+=1
    n//=k
res+=(n-1)
print(res)