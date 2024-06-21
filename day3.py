# MINIMUM ARRAY SUM(AVERAGE)
N=int(input())
l=list(map(int,input().split()))
l.sort()
avg=(l[-1]+l[-2])/2
res=0
for i in l:
    if i>avg:
        res+=i
print(res)



#  MINIMUM KEY PRESSES(1 2...9 00)   
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

# HEAD AND TAIL
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