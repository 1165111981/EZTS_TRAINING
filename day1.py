# ANT ON RAIL
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



# DOG AGE
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