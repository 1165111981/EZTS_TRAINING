#NUMBER OF COMBINATIONS LENDING TO PRODUCT
m=list(map(int,input().split()))
count=0
target=int(input())       
m.sort()    #sorting the list
for k in range(len(m)-2): # we write m-2 beacyse we will have k and i but j will point to i which will be false
    i=k+1    
    j=len(m)-1 #j is the last element
    while(i<j):       
        if m[i]*m[j]*m[k]==target: #check product of i j k is equal to target or not
            count+=1
            i+=1    #i shou;d increment 
            j-=1       #j should decrement
        elif m[i]*m[j]*m[k]<target:  # target is less than product
            i+=1      #increment only i
        else:
            j-=1     #target is more than product 
print(count)




#EUILIBRIUM CODE
arr=list(map(int,input().split()))
total=sum(arr)
l_sum=0
for i in range(len(arr)):
    total-=arr[i]
    if l_sum==total:
        print(i+1)
    elif l_sum==arr[i]:#sum+=arr[i]
        print(-1)


# MAXX SUBARRAYYYYYYY
nums=list(map(int,input().split()))  
res=0
if len(nums)==1:    #if we want to include negative values then we need to take these
    print(nums[0])
temp=0
res=nums[0]
for i in nums:
    temp+=i
    if temp<i:
        temp=i
    if res<temp:
        res=temp
print(res)







#GCD LCM
a=int(input())
b=int(input())
lcmm=0
gcdd=0
while (b>0):
    a,b=b,a%b
    print(gcdd)
lcmm=(a*b)//gcdd
print(lcmm)

#PIZZAA PARTYY
N=int(input())
Y=int(input())
res=0
for i in range(Y,N+1):
    if N%i==0:
        while i:
            res+=i%10
            i=i//10
        break
print(res)



##REDUCE TILL ZERO(ANOTHER METHOD TO FIND THE GCD OF A NUMBER)
x=int(input())
y=int(input())
t=0
while y>0:
    if x<y:
        x,y=y,x
    elif x>=y:
        t=x-y
        x=y
        y=t
print(x)



#NEARESTS CORNER
n=input()
s=input().split()
idx=s.index(n)
z=float('inf') #we dont know the last(max)value so we r initializing a infinte value 
for i in range(len(s)):
    if s[i] == "-":
        z=min(z,abs(i-idx)-1)
    if i==0 or i==len(s)-1:
       z=min(z,abs(i-idx))
print(z)
