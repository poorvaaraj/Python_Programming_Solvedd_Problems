#Question no:1.1
n = 6
for i in range(n,0,-1):
    print('*' * i)

print('---------------------------------------------')
#Question no:1.2
a = 6
for b in range(0,a):
    print('*' * b)
print('---------------------------------------------')

#Question no:1.3
ascii_value = 65

for i in range(5):
    for j in range(i + 1):
        print(chr(j + 65), end=" ")
        ascii_value += 1

    print("\n")




print('---------------------------------------------')
#Question no:1.4


ascii_value = 65

for i in range(5):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")

    ascii_value += 1
    print("\n")


print('---------------------------------------------')
#Question no:3
from datetime import date, datetime
name = input("Enter your name:")
birthdate = (input('Enter date(yyyy-mm-dd): '))
birthdate = birthdate.split('-')
#print(birthdate)
year, month, day = [int(item) for item in birthdate]

age = 2022-year
print("Hi", name, "Good Morning..!!, You are", age, "yrs old. ")