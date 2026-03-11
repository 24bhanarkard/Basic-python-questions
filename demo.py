# math=40
# pi=3.14
# name='prashant jha'
# print(type(math))
# print(type(pi))
# print(type(name))

#_____________________________________________________________
# print(2+2)
# print("2"+"2")
# val1=int(input("enter 1st value"))
# val2=int(input("ENTER 2nd value"))
# print(val1+val2)
#input function accepts only string value

#________________________________________________________________

# print(int(3.14))
# #print(int(10+5j))
# print(int(True))
# print(int(False))
# #print(int("3.14"))
# print(int("3"))
# #print(int("prashant"))
#__________________________________________________________________

# print(float(3))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("5"))
# #print(float("name"))

#__________________________________________________________

# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex(5.6))
# #print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))

#____________________________________________________________

# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))

#__________________________________________________________

#wap for simple interest

# p=100000
# r=10
# n=1
# si=(p*n*r)/100
# print("simple interest:",si)

#____________________________________________________
# #wap to accept degree c and convert   to fahrenheit
# c=float(input("enter temp in celsius"))
# f=(c*1.8)+32
# print("temp in fahrenheit is:",f)

#____________________________________________________

#swapping using 3rd variable
# a=input("enter first no:")
# b=input("enter 2nd no:")
# temp=a
# a=b
# b=temp
# print("1st no is:",a)
# print("2nd no is:",b)

#____________________________________________________

# a=int(input("enter first no:"))
# b=int(input("enter 2nd no:"))
# a=a+b
# b=a-b
# a=a-b
# print("1st no is:",a)
# print("2nd no is:",b)

#____________________________________________________

# h=float(input("enter height in feet"))
# inch=h*12
# cm=inch*2.54
# print("height in inch:",inch)
# print("height in cm:",cm)

#____________________________________________________

# #reverse
# num =123
# a=num%10
# num = num // 10
# b=num%10
# c= num //10
# rev = a*100 + b*10 + c*1
# print(rev)

#____________________________________________________

num = 1234567

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10
num = num // 10

d = num % 10
num = num // 10

e = num % 10
num = num // 10

f = num % 10
num = num // 10

g = num % 10

rev = a*1000000 + b*100000 + c*10000 + d*1000 + e*100 + f*10 + g
print(rev)