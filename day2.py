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