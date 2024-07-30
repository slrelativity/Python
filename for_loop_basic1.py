for i in range(151):
    print(i)

for x in range(5, 1001, 5):
    print(x)

for y in range(1, 101):
    if y % 10==0:
        print ("Coding Dojo")
    elif y % 5==0:
        print ("Coding")
    else:
        print(y)


sum_of_odd = 0
for b in range(0,500000):
    if b % 2 !=0:
        sum_of_odd +=b
print(sum_of_odd)


low_num =2
high_num=12
mult=3

for a in range(low_num, high_num):
    if a % mult==0:
        print(a)