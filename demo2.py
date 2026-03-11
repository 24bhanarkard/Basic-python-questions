#mylist = ["prashant", "ashish","komal","ankush","ashish", 77,"sandip", 60.52, "prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

#_______________________________________________________________________

# mylist.append('harsh')
# mylist.append("laxman")
# print(mylist)
# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist = mylist.copy() #cloning
# print(mylist)
# print(newlist)

#____________________________________________________________________________

# mylist = [['prashant', 'jha'],['85.56'],[440022,"yyy"]]
# print("example of multidimesnsional list :")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

#_____________________________________________________________________________

# list1=["prashant","jha"]
# print(list1*2)

# list2 =[50, 25.50]
# print(list1+list2)

# list3 = [50, 25.50, 'prashant']
# del list3[2]
# print(list3)

# list4 = [50, 25.50, 'prashant']
# del list4
# print(list4)#error bcoz list is already deleted so wont be able to print

# list5 = [50, 25.50, 'prashant']
# list5.clear();
# print(list5)

# name="prashant"
# print(name)
# myname=list(name)  #typecasting
# print(myname)

#____________________________________________________________________________
# mylist = [44,22,77,0,9,88]
# mylist.sort()
# print(mylist)

# mylist = [44,22,77,0,9,88]
# mylist.sort()(reverse=True)
# print(mylist)

# default sorting method for numbers is ascending order
# default sorting method for string is alphabetical order
# we should know that list should contain homogeneous data otherwise we will get type-KeyError
# python first sorts number then string follows 

#_____________________________________________________________________________

# math=10
# phy=10
# chem =78
# print(id(math)) #returns address of variable
# print(id(phy))  #same value will get same address of variable
# print(id(chem))

#__________________________________________________________________________________

#aliasing=assisgning one variable refernce to another
# mylist=[44,22,77,0,9,88]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))

#___________________________________________________________________________________

#looping
#there are 2 types of special opertaors introducded in python - membership &
#membership - in and not in __________-used to check if a value is present or not
# name = 'prashant'
# print('Z' not in name)

# for i in range(1,6):
#     print(i)

# for i in range(6):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(1,10,2): #ascending
#     print(i)

# for i in range(20,10,-2): #descending
#     print(i)

# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10) 
# print(" ")

# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19) 

#___________________________________________________________________________-

#pos neg or zero

# no = int(input("enter any digit :"))
# if no>0:
#     print('positive')
# if no<0:
#     print('negative')
# if no ==0:
#     print('zero')

#________________________________________________________________________________

#wap to accept days and check thw working days and weekends

# day = input("enter day:")

# if day=='monday' or 'tuesday' or 'wednesday' or 'thursday' or 'friday':
#     print("weekday")
# else:
#     print("weekend")

#____________________________________________________________________________________

#wap to accept 3 paper marks and caclualte total, percentage and if percent>=60 :
#  thn eligible for placement

# a=int(input("enter marks of subj 1:"))
# b=int(input("enter marks of subj 2:"))
# c=int(input("enter marks of subj 3:"))

# sum=a+b+c
# print("total is:",sum)

# percent=(sum/300)*100
# print("percentage is : ",percent)

# if(percent>60):
#     print("eligible for placement")
# else:
#     print("not eligible for placement")

#_________________________________________________________________________________________

#wap to accept 5 diff values in 5 diff variables and check max value by using simple if statement

a=int(input("enter no:"))
b=int(input("enter no:"))
c=int(input("enter no:"))
d=int(input("enter no:"))
e=int(input("enter no:"))

if(a>b and a>c and a>d and a>e):
    print("a is greatest")
if(b>c and b>d and b>e and b>a):
    print("b is greatest")
if(c>d and c>e and c>a and c>b):
    print("c is greatest")
if(d>e and d>a and d>b and d>c):
    print("d is greatest")
if(e>a and e>b and e>c and e>d):
    print("e is greatest")