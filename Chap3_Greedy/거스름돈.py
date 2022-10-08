# 점원: 500, 100, 50, 10 무한
# 거슬러 줄 수 있는 최소 동전 개수
clerk=[500,100,50,10]
input=1260
cnt=0
for i in clerk:
    mok,nam=divmod(input,i)
    if mok>0:
        cnt+=mok
        input=input-i*mok
print(cnt)

# 책 코드
input=1260
cnt=0
for i in clerk:
    cnt+=input//i #몫을 더함
    input%=i      #나머지
print(cnt)