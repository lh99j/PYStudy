num = int(input())
num1 = None
strnum = ""
trynum = 0


if num < 10:
    str1 = str(num) + str(0)
    num = int(str1)

a =[]

for i in str(num):
    a.append(i)


while True:
    if num == 0:
        trynum = 1
        break
    
    num1 = int(a[0]) + int(a[1])

    temp = int(a[1])
    if num1 >= 10:
        num1 = num1 - 10

    strnum = str(temp) + str(num1)

    a.clear()
    for i in strnum:
        a.append(i)

    trynum += 1

    if num == int(strnum):
        break

print(trynum)