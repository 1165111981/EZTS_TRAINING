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



# TARGET SUM
nums=list(map(int,input().split()))
target=int(input())
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
            break  




# PRINTING THE REVERSE ORDER OF A STRING
s=input().split
print(*s[::-1])



#PEAK ELEMENT FINDER(FINDING INDEX OF THE MAX NUMBER)
n=int(input())
l=list(map(int,input().split()))
for i in range(1,len(l)-1):
    if 1[i]>l[i-1] and l[i]>1[i+1]:
        print(i)
        break 


# TOYS REMAINING
total=int(input())
donated=int(input())
remaining_toys = total-donated
print(remaining_toys)