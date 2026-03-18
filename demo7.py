# #password encoding : detect no of special characters and whitespaces
# text=input("enter your password : ")
# number=0
# for i in text:
#     if not i.isalnum(): #isalnum()is used to detect aplhabets and numbers
#         number=number+1

# print(number)
#___________________________________________________________________________________________

# #find the intersection of 3 arrays
# a=[1,2,3]
# b=[2,3,4]
# c=[3,4,5]

# for i in a:
#     if i in b and i in c:
#             print("common no is : ",i)
    
#____________________________________________________________________________________________

#move zeros to the end

# a=[1,2,3,0,7,0,8,0,8,9]
# for i in a:
#       if i==0:
#             a.remove(i)
#             a.append(i)

# print(a)

#___________________________________________________________________________________________

#find the second largest element :

# a=[23,45,90,87,19,23,78,65,44]
# a.sort()
# print(a)
# print("second largest element is : ",a[-2])

#___________________________________________________________________________________________

#wap to calculate and return the sum of dist between adjacent numbers in an array of 
# positive integrs
N=int(input("enter n : "))
sum=0
mylist=[]
for i in range(N):
    a=int(input("enter element value : "))
    mylist.append(a)
for j in range(len(mylist)):
    if j+1 in range(len(mylist)):
        sum+= abs(mylist[j]-mylist[j+1])

print(sum)