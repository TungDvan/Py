def digitSum(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

a = [123, 456, 789, 1234]
b = [digitSum(x) for x in a]
print(b)