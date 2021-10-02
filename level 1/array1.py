num1 = int(input())
num2 = int(input())
num3 = int(input())

result = num1 * num2 * num3

plusnum = 0
a = 0
for i in range(10):
    for j in str(result):
        if int(plusnum) == int(j):
            a += 1
    plusnum += 1
    print(a)
    a = 0
    




