number = ['1', '2', '3', '4']
sum = 0
for n in range (len(number)):
    while n != 0:
        sum = sum * n
        sum += 1
print(sum)
