# for i in range(1,5):
#     if i==3:
#         break
#     print(i)

#_______________________________________________________________________________________________________

# for i in range(1,5):
#     if i==3:
#         continue
#     print(i)

#_______________________________________________________________________________________________________

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)

#________________________________________________________________________________________________________

# i=1
# while i<=5:
#     print(i)
#     i=i+1

#________________________________________________________________________________________________________

# username = ""
# password = ""

# while username != "admin" or password != "hello":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

# print("Login successful")

#_______________________________________________________________________________________________

# n = int(input("enter number:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("the sum of first ",n," number is :",sum)

#_________________________________________________________________________________________________

#remove duplicate characters

# name=input("enter your name:")
# newname=""
# for i in name:
#     if i not in newname:
#         newname+=i
# print(newname)

#________________________________________________________________________________________________

#reverrse a string using a loop
#name=input("enter your name:")

#________________________________________________________________________________________________

# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("this is my purchased cart item ")
#         continue
#     print(i)

#__________________________________________________________________________________________________-

#palindrome

# name=input("enter a name:")
# newname=name[::-1]
# if name==newname:
#     print("palindrome")
# else:
#     print("not a palindrome")

#______________________________________________________________________________________________

# #anagram - check if both words have same and equal letters like listen=silent
# a=input("enter word 1:")
# b=input("enter word 2:")
# #do by sorting

#_______________________________________________________________________________________________

#adding key value pair to a dictionary
# my_dict = {}
# my_dict['name'] = 'Dikshant'
# my_dict['age'] = 20
# print("After adding key-value pairs:", my_dict)

#__________________________________________________________________________________________________

#remove a key value pair 

# my_dict = {}
# my_dict['name'] = 'Dikshant'
# my_dict['age'] = 20
# print("After adding key-value pairs:", my_dict)

#___________________________________________________________________________________________________

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, end=" ")
#     print()

#____________________________________________________________________________________________________

# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

#_____________________________________________________________________________________________________

# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()

#____________________________________________________________________________________________________

n=int(input("enter the number of rows :"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*", end=" ")
    print()