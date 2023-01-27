#ques 1
str=input("ENTER THE STRING :")
reverse_of_str= str[::-1]
print(reverse_of_str)

#ques 2
lower_limit=int(input("ENTER LOWER RANGE LIMIT:"))
upper_limit=int(input("ENTER UPPER RANGE LIMIT:"))
n = int(input("ENTER THE NUMBER : "))
for i in range(lower_limit,upper_limit+1):
    if(i%n==0):
        print(i)

#ques 3
a = int(input("ENTER 1st SIDE OF TRIANGLE = "))
b = int(input("ENTER 2nd SIDE OF TRIANGLE = "))
c = int(input("ENTER 3rd SIDE OF TRIANGLE = "))
s = (a + c + b) / 2

area=((s)*(s-a)*(s-b)*(s-c))**0.5
if (a>0 and b>0 and c>0):
    if ((a+b>=c) and (b+c>=a) and (a+c>=b) ):
      print("TRIANGLE IS VALID")
      print ("AREA BY HERON'S FORMULA = ",area)
    else:
      print("TRIANGLE IS NOT VALID")
else:
    print("TRIANGLE IS NOT VALID")

#ques 4
n = 5
for i in range(n):
    for j in range(i):
        print("* ", end=" ")
    print(" ")
for i in range(n, 0, -1):
    for j in range(i):
        print("* ", end=" ")
    print(" ")

#ques 5
size = 5
letter = 65
for i in range(0, size + 1):
    for j in range(0, i):
        character = chr(letter)
        print(character, end='')
        letter += 1
    print()

#ques 6
lower_limit=int(input("ENTER THE LOWER LIMIT OF RANGE : "))
upper_limit=int(input("ENTER THE UPPER LIMIT OF RANGE : "))
for num in range(lower_limit,upper_limit + 1):
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count = count + 1
            break

    if count == 0 and num != 1:
        print("%d" % num)
    else:
        pass

#ques 7
for i in range(1,500):
    if (i%11==0) :
        if(i%7==0):
            print(i)

#ques 8
for n in range(11):
  n=int(input("ENTER A NUMBER :"))
  if n%2==0:
    print("EVEN")
  else:
    print("ODD")
  if n>0:
    print("POSITIVE NUMBER")
  elif n==0:
    print("ZERO")
  else:
    print("NEGATIVE NUMBER")

#ques 9
a = input(str("enter a line : "))


def word_count(line):
    counts = dict()
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(word_count(a))