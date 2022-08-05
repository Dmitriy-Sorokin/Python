a = int(input('Write int one '))
b = int(input('Write int two '))

try:
    result = int(a/b)
except ZeroDivisionError:
    result = 0
    print('На ноль делить нельзя')

print('Result : ' + str(result))
result_2 = a + b
print(result_2)

# ZeroDivisionError  ValueError