# #function
# def msg():
#     print("hello world")
#     n1=int(input("enter the value of n1:"))
#     n2=int(input("enter the value of n2"))
#     print("add= ",n1+n2)

# msg()

#______________________________________________________________________

# def add():
#     n1=int(input("enter the value of n1:"))
#     n2=int(input("enter the value of n2:"))
#     sum=n1+n2
#     mul=n1*n2
#     sub=n1-n2
#     div=n1/n2
#     return sum,mul,sub,div

# result=add()
# print(result)

#_______________________________________________________________________________

#types of arguement
# 1.positional arguement
# 2. keyword arguement
# 3. default arguemnt
# 4. variable length arguement / variable no of arguement

#_________________________________________________________________________________

#positional
# def PersonalInfo(fname,lname):
#     print("first name=",fname)
#     print("last last=",lname)

# PersonalInfo("prashant","jha")

#___________________________________________________________________________
#keyword arguement
# def PersonalInfo(fname,lname):
#     print("first name=",fname)
#     print("last last=",lname)

# fname="prashant"
# lname="jha"
# PersonalInfo(fname,lname)

#___________________________________________________________________________
#default arguement

# def cityName(city="nagpur"):
#     print(city)

# cityName("mumbai")
# cityName("delhi")
# cityName()


#at times, when you write cityName(), it will throw an error, so to resolve this you can set a 
# default value when no parameter is passed such as def cityName(city="nagpur"):.
#this will print nagpur when no argeument is passed.

#___________________________________________________________________________
#variable length arguement

# def studentName(*name):
#     print(name)

# studentName("prashant","rahul","sandip","ashish")

#*name is used here to accept multiple arguements ina  form of tuple. you really dont 
# need to define every single arguement to pass it down.
#___________________________________________________________________________

#triplets
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
#     # Write your code here
#     alice=bob=0
#     for i,j in zip(range(len(a)),range(len(b))):
#         if a[i]>b[j]:
#             alice +=1
#         if a[i]<b[j]:
#             bob +=1
#         if a[i]==b[j]:
#             pass
#     return alice, bob

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

#___________________________________________________________________________________

# mylist=[2,3,4,5,6,7,8,0]
# #search the element 7
# n=len(mylist)
# print(n)

# def searchElement(target):
#     for i in range(len(mylist)):
#         print(mylist[i])

#         if target ==mylist[i]:
#             print("element found at index no : ",i)

# searchElement(0)

#___________________________________________________________________________________

mylist=[2,3,4,5,6,7,8,0]
#search the element 7
n=len(mylist)
print(n)

def searchElement(target):
    for i in range(len(mylist)):

        if target ==mylist[i]:
            return i
    return -1
result = searchElement(0)
if result!=-1:
    print("element found at index number : ",result)
else:
    print("element not found ")