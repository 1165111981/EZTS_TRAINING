ANT ON RAIL
n=int(input())
l=list(map(int,input().split()))
pos=0 #initialize ant position as 0
res=0
for i in l:       #i will iterate each element present in list
    pos+=i        #[0,1+(-1)=0==1, 1,1+(-1)=0==2, 1]
    if pos==0:
        res+=1
print(res)



#CHOCOLATE JAR AND A B C
l=list(map(int,input().split()))
n=int(input())
a=0            #number of chocolates present near a
for i in l:
    if i%3==0: #ex:9--then reminder is 0,so choclats will be divided among 3 
        a+=i//3
    if i%3>0:
        a+=i//3+1 #evn if we get 2 as reminder , we willadd one ponly (another 1 will go to b)
print(a)

#DIWALI CONTEST
n=int(input())
p=int(input())
time=240-p  #4 hrs=240 mins(time taken to travel frm home to party)
result=0  
i=1    #1st prblm
while time>0:  
    if 5*i<time:          
        time=time-5*i   
        result+=1
        i+=1
    else: 
        break
print(result)



DOG AGE
N=int(input())
print(N*7)



#SPACE COUNTER
inp=input()
space= 0
for char in inp:
    if char==' ':
        space+= 1
print(space)
#-------OR--------
s=input()
print(s.count(' '))



#MATH TEST TO PRINT NEXT PRIME NUMBER OF THE GIVEN PRIME NUMBER
n=int(input())
while True:       #run for an infinte loop to print the next numbers
    n=n+1
    for i in range(2,n):   
        if n%i==0:            #this will become true if the number is divisible by any number(not a prime number)
            break
    else:                   #the number i s the prime number
        print(n)
        break



#BASKETBALL
n = int(input())                      #no. of variables 
inp2= int(input())                    #no. of elements present in subset
l=list(map(int,input().split()))       #making a list of elements 
mx=0                                   #initialize max score as 0
for i in range(len(l)-inp2+1):         ## iterate over possible starting points of subarrays of length inp2
    temp=l[i:i+inp2]                   # get the subarray of length inp2 starting at index i
    s,k=0,1                            # initialize the score (s) and the weight (k)
    for j in temp:                   # iterate over each element in the subarray
        s+=(k*j)                     # add the weighted element to the score
        k+=1                          # increment the weight
    if s>mx:mx=s  
                      # if the current score is greater than the maximum found so far ## update the maximum
print(mx)                  # print the maximum weighted score




#ELECTIONS
n = int(input())                #number of voters
l = list(map(int, input().split()))    #list of votes
d = {}    
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1                 #till here the code is about each party got how many votes.
lis=list(d.items())             #convert the dictionary into list
lis.sort(reverse=True,key=lambda X:X[1])    #it will sort the list(in dict[party:votes],,so we reversed it,,)
if len(lis)==1:            #if there is only party
    print(l[0][0])
else:
    if lis[0][1]==lis[1][1]:      #if two parties get the same number of votes 
        print(-1)                 #then we should print -1
    else:
        print(lis[0][0])         #it will print the party which got the max votes



#MAGICAL STRING
s=str(input())  
x=len(s)
out=0
d={}
for i in s:
    if i in d:        #WE NEED TO CHECHK IF THE I(KEY) IS PRESENT IN DICTIONARY OR NOT
        d[i]+=1
    else:
        d[i]=1
    d.values()
    mxstring=max(d.values())
    out=x-mxstring 
print(out)



#ENCODE THE NUMBER
s=input()
res=''
for i in s:
    res+=str(int(i)*int(i))
print(int(res))




MINIMUM ARRAY SUM(AVERAGE)
N=int(input())
l=list(map(int,input().split()))
l.sort()
avg=(l[-1]+l[-2])/2
res=0
for i in l:
    if i>avg:
        res+=i
print(res)



 MINIMUM KEY PRESSES(1 2...9 00)   
s=input()
i,res=0,0
while i<len(s):
    if i+1<len(s) and s[i]=='0' and s[i+1]=='0':   #i+1=check if there is next number or not...s[i]==s[i+1]==0.(checks the number n next number is 0 (to get 00 as one number))
           i+=2
    else:
        i+=1 
res+=1



#ARDUINO
l=list(map(int,input().split()))
d,maxx=0,0         #distanve covered          
for i in l:      
    d+=i         
    if abs(d)>maxx:    #(abs(-7) it will make -7 as 7 only)     
            maxx=abs(d)  
print(maxx)       #so printing 7


#SPECIAL STRING((MINIMUM ASCII DISTANCE))
A=input()
S=input()
total=0
for i in A:     #i is the index of A
    mn=100;d=0    #d is the distance
    for j in S:       #j is index of S string
        d=abs(ord(i)-ord(j))  #ord function stores the ascii value of alphabets
        if d<mn:
            mn=d
    total+=mn
print(total)


n=int(input())
res=0
cur=1000
comma=1
while cur<=n:
    next=cur*1000
    nums=min(n-cur+1,next-cur)
    res+=nums*comma
    cur=next
    comma+=1
print(res)

HEAD AND TAIL
S=input()
sc,hc=0,0
for i in S:
    if i=='H':
        sc+=2
        hc+=1
        if hc==3:
            break
    else:sc-=1 
    hc=0
print(sc)


l=['a','b','c','d']
print(min(l))


s=input()
p=int(input())
k=int(input())
start=max(0,p-k-1)
end=min(len(s),p+k)
print(min(list(s[start:end])))



s=input()
v='aeiou'
mx=0
for i in s:
    if s.count(i)>mx:
        mx=s.count
        vowel=i
print(vowel)


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
    l_sum+=arr[i]:
print(-1)


MAXX SUBARRAYYYYYYY
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





#MISSING ALPAHBETS
inp = input()
count=[0]*26
missl= []
for char in 'abcdefghijklmnopqrstuvwxyz':
    if char not in inp:
        missl.append(char)
# print(*missl,end='')   this * is used for conerting a list into string
missletters=''.join(missl)
print(missletters)



TARGET SUM
nums=list(map(int,input().split()))
target=int(input())
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
            break  




PRINTING THE REVERSE ORDER OF A STRING
s=input().split
print(*s[::-1])



#PEAK ELEMENT FINDER(FINDING INDEX OF THE MAX NUMBER)
n=int(input())
l=list(map(int,input().split()))
for i in range(1,len(l)-1):
    if 1[i]>l[i-1] and l[i]>1[i+1]:
        print(i)
        break 


TOYS REMAINING
total=int(input())
donated=int(input())
remaining_toys = total-donated
print(remaining_toys)


PATTERN 333222111/332211/321
n= int(input())
for i in range(n):
    for j in range(n,0,-1):
        print(str(j)*(n-1),end='')
    print()



#SMALLEST NUMBER
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




#2 ARRAY ADD THE ELEMENTS AND PRINT THE MAXIMUM AMONG THEM
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


#SOLVE THE EQUATION
n=int(input())
res=0
for a in range(1,n):
    for b in range(1,n):
        for c in range(1,n):
            if a*a+b*b+c*c+a*b+b*c+c*a==n:
                res+=1
print(res)

n,a,b=map(int,input().split())
res=set()
for i in range(n):
    for j in range(n):
        if n-a*i-b*j>0:
            res.add(n-a*i-b*j)
print(len(res))



#BORING ARRAY
n=int(input())
l=list(map(int,input().split()))
l.sort
s=0
i,j=0,len(l)-1
while i<j:
        s+=abs(l[i]-l[j])
        i+=1
        j-=1
print(s)




n=int(input())
l=list(map(int,input().split()))
p=int(input())
res=0
primes=[]
for i in range(2,int(n**0.5)+2):
    while n%i==0:#to check how manuy repeated numbers r there{for 8=we need 3 2's}
        primes.append(i)
        n/=2
print(primes)
for i in set(primes):
    if i<len(l):
        res+=primes.count(i)*l[i]
print(res)