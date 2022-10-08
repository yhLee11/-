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
    #(n==k로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target=(n//k)*k
    res+=(n-target)
    n=target
    #n이 k보다 작을때(더 이상 나눌 수 없을 때) break
    if n<k:break
    #k로 나누기
    res+=1
    n//=k
res+=(n-1)
print(res)