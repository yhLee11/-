import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
s=list(map(int,input().split()))
s.sort(reverse=True)
s=s[:2]
ans=0
kcnt,mcnt=0,0
idx=0
while True:
    if mcnt==m:break
    if idx==0 and kcnt==k:
        kcnt=0
        idx=1
    elif idx==1 and kcnt==1:
        kcnt=0
        idx=0
    ans+=s[idx]
    kcnt+=1
    mcnt+=1
print(ans)

# 책 코드
first=s[0]
second=s[1]
res=0
while True:
    for i in range(k):
        if m==0:
            break
        res+=first
        m-=1
    if m==0:break
    res+=second
    m-=1
print(res)

# 개선 코드 - 반복수열 이용
n,m,k=5,8,3
first=s[0]
second=s[1]
cnt=int(m/(k+1))*k
cnt+=m%(k+1) # first가 반복되는 횟수

res=0
res+=(cnt)*first
res+=(m-cnt)*second
print(cnt,m-cnt)
print(res)