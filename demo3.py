# nested if else : 
# if condition 1: 
#     if conditiion2:
#         statement
#     else
#         statement
# else
#     if consfition2
#         statement
#     else
#         statement

#_________________________________________________________________________
#wap to accept 3 paper marks and check max marks usning nested if else : 

# a=int(input("enter marks of subject 1: "))
# b=int(input("enter marks of subject 2: "))
# c=int(input("enter marks of subject 3: "))

# if(a>b):
#     if(a>c):
#         print("a is greatest")
#     else:
#         print("c is greatest")
# else:
#     if(b>c):
#         if(b>a):
#             print("b is greatest")
#         else:
#             print("c is greatest")

#_________________________________________________________________________
#wap to accept 3 paper marks and check in marks usning nested if else : 

# a=int(input("enter marks of subject 1: "))
# b=int(input("enter marks of subject 2: "))
# c=int(input("enter marks of subject 3: "))

# if(a<b):
#     if(a<c):
#         print("a is smallest")
#     else:
#         print("c is smallest")
# else:
#     if(b<c):
#         if(b<a):
#             print("b is smallest")
#         else:
#             print("c is smallest")
#________________________________________________________________________________

#else if ladder syntax : 

# if condition:
#     statement
# elif condition :
#     statement
# elif condition:
#     statement
# else:
#     #default block

#___________________________________________________________________________________


#wap to accept percentage and if per>90 grade a, per>80 grade b, per>60 grade c, per<60 fail 

# a=float(input("enter your percentage: "))
# if(a>90):
#     print("grade a")
# elif(a>=80 and a<90 ):
#     print("grade b")
# elif(a>=60 and a<80):
#     print("grade c")
# else:
#     print("fail")

#_____________________________________________________________________________________

#dictionary

# mydict = {
#     "name":"prashant",
#     "professional":"developer",
#     "empid":1001
# }
# print(mydict)
# print(type(mydict))


#_________________________________________________________________________________________

mydict={
    101: "prashant",
    102: "aashish",
    "103":"mohini",
    "104":"truvani",
    101 : "ashish",
    104 : "ashish"
}

print(mydict)

#print with the help of key : 
a= mydict[102]
print(a)

#replace old value by new value
mydict[102]="peter"
print(mydict)

#only print key
for x in mydict:
    print(x)

#only print values
for x in mydict.values():
    print(x)

#print key and values both
for x,y in mydict.items():
    print(x,y)

#add a new key value pair
mydict["mobile_no"] = 4646463738
print(mydict)


mydict = {
    101:"prashant",
    "professional":"developer",
    "empid":1001
}
mydict.pop(101)
print(mydict)
#__________________________________________________________________________________________

#slicing

# name =    "prashantjha"
# #indexing = 012345678910
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])
# #print(name[15]) out of range...

# s = "help4code is the best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python")) #gives default value -1 if word is absent.
# print(s.find("programming"))

# s="prashant","aashish","sanndeep"
# m = ' |'.join(s)
# print(m)


# s = "Python is a High Level Programming Langage"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print('subjects marks :')
# phy=50
# chem=60
# math=70
# print("physics={} chemistry={} math={}".format(phy,chem,math))
# print("physics={0} chemistry={2} math={2}".format(phy,chem,math))
# print("physics={x} chemistry={z} math={z}".format(x=phy,y=chem,z=math))
# total = phy,chem,math
# print("total marks",f"{total}")
# print("roll no", "7".zfill(4))

#______________________________________________________________________________________

# print('prashantjha777'.isalnum())
# print('orashantjh'.isalpha())
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("hello".startswith("he"))
# print("hello".endswith("lo"))

#__________________________________________________________________________________________

#bodmas
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

#_______________________________________________________________________________________

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

#____________________________________________________________________________-
# name="prashant"
# v=0
# c=0

# for i in name:
#    print(i)

#____________________________________________________________________

name = "prashant"
data = ['a','e','i','o','u']
v = 0
c = 0

for i in name:
    if i in data:
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)


#_____________________________________________________________________

