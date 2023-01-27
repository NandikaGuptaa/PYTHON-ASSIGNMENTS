#ques 1
#marks=a
a=int(input("ENTER YOUR MARKS :"))
if (a<25):
    print("GRADE F")
elif (a >=25 and a<45):
    print("GRADE E")
elif (a>=45  and a<50):
    print("GRADE D")
elif (a >=50 and a<60):
    print("GRADE C")
elif (a >=60 and a<80):
    print("GRADE B")
else:
    print("GRADE A")

#ques 2
year=int(input("ENTER THE YEAR :"))
if year%400==0:
    print("LEAP YEAR")
elif year%100==0:
    print("NOT A LEAP YEAR")
elif year%4==0:
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")

#ques 3
import random
list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,3,4,5,6,7,8,9]
i=1
while i<=10:
    a=random.choice(list1)
    b=random.choice(list2)
    c=a*b

    d=int(input("Q."+str(i)+" "+str(a)+"x"+str(b)+"="))
    if(d==c):
        print("CORRECT.")
    else:
        print("INCORRECT.")
    i=i+1

#ques 4
n=int(input("ENTER NUMBER OF CANDIES :"))
for n in range(0,200):
    if n%5==2:
        if n%6==3:
            if n%7==2:
                print(n," is the number of candies in the bowl.")



