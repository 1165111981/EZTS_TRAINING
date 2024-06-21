#  PATTERN 333222111/332211/321
n= int(input())
for i in range(n):
    for j in range(n,0,-1):
        print(str(j)*(n-1),end='')
    print()



# #SMALLEST NUMBER
a=int(input())
b=int(input())
c=int(input())
print(min(a,b,c))

#FELLIS FUNCTION
n=int(input())
l=[1,1]
for i in range(2,n+1):
    l.append(int(l[i-1]+l[i-2]*7+i/4)%(10**9+7))
print(l[n])


#SPECIAL FIBONACCI SERIES
n=int(input())
l=[1,1]
for i in range(2,n+1):
    l.append(int(l[i-1]*l[i-1]+l[i-2]*l[i-2])%(47)) #append will add the elements at the end of the list(it is only used for the list))
print(l[n])



n=int(input())
l=list(map(int,input().split()))
mx=0
res=[-1,-1]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j] and l[i]+l[j]==18:
            p=l[i]*l[j]
            if p>mx:
                mx=p
            res[0],res[1]=l[i],l[j]
print(res)



#PYRAMID SUM 
n = int(input())
res=n
num=2
for i in range(n-1,0,-1):
    res+=2*i*num
    num+=1
print(res)

#PYRAMID SUM
n=int(input())
res=0
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
        res+=k
    for l in range(2,i+1):
        print(l,end=" ")
        res+=l
    print()
print(res)



