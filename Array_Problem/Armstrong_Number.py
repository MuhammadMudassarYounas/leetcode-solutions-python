number=153
nod=len(str(number))
num=number
total=0
while num > 0:
    Last_digit=num%10
    total=total+(Last_digit**nod)
    num=num//10
print(total)
if (number==total):
    print("The number is ArmStrong")
else:
    print("The is not ArmStrong")