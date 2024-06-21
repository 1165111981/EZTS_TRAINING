#  2 ARRAY ADD THE ELEMENTS AND PRINT THE MAXIMUM AMONG THEM
n=int(input())
A=list(map(int,input().split()))
S=list(map(int,input().split()))
mx=0
# for i in range(n):
#     s=A[i]+S[i]
#     mx=max(mx,s)
# print(mx)
for i in range(n):
    mx=max(mx,A[i]+S[i])
print(mx)
    


n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(n):
    la=l[:i+1]
    ra=l[i+1:]
    res=abs(sum(la)-sum(ra))
    m.append(res)
print(m)


n=int(input())
l=list(map(int,input().split()))
right=sum(l)
res=[]
left=0
for i in range(n):
    left+=l[i]
    right-=l[i]
    res.append(abs(right-left))
print(res)