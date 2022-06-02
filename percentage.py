import pyfiglet
dicru = pyfiglet.figlet_format("CYBER DICRU")
print(dicru)
m1 = int(input("enter 1 number = "))
m2 = int(input("enter 2 number = "))
m3 = int(input("enter 3 number = "))
m4 = int(input("enter 4 number = "))
m5 = int(input("enter 5 number = "))
m6 = int(input("enter 6 number = "))
m7 = int(input("enter 7 number = "))
m8 = int(input("enter 8 number = "))
m9 = int(input("enter 9 number = "))
m10 = int(input("enter 10 number = "))
p = (m1+m2+m3+m4+m5+m6+m7+m8+m9+m10)*100/1000
print("your pecentage is = ",p)
p = int(input("enter your given percentage"))
if p >= 40 :
     print("yes you are passed")
else:
     print("nice you are failed")
