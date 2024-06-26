import os
os.system("cls")
# def convertToCelsius(x):
#     return  (x - 32) * (5 / 9)


# def convertToFahrenheit(x):
#     return   x * (9 / 5) + 32


# assert convertToCelsius(0) == -17.77777777777778
# assert convertToCelsius(180) == 82.22222222222223
# assert convertToFahrenheit(0) == 32
# assert convertToFahrenheit(100) == 212
# assert convertToCelsius(convertToFahrenheit(15)) == 15

# def fizzbuzz(number):
#     for i in range(1, number + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FIZZBUZZ", end=" ")
#         elif i % 3 == 0:
#             print("FIZZ", end=" ")
#         elif i % 5 == 0:
#             print("BUZZ", end=" ")
#         else:
#             print(i, end=" ")
    
# fizzbuzz(35)

# def ordinalSuffix(n):

#     if n % 100 in (11, 12, 13):
#         return f"{n}th"
#     elif n % 10 == 1:
#         return f"{n}st"
#     elif n % 10 == 2:
#         return f"{n}nd"
#     elif n % 10 == 3:
#         return f"{n}rd"
#     else:
#         return f"{n}th"

# assert ordinalSuffix(0) == '0th'
# assert ordinalSuffix(1) == '1st'
# assert ordinalSuffix(2) == '2nd'
# assert ordinalSuffix(3) == '3rd'
# assert ordinalSuffix(4) == '4th'
# assert ordinalSuffix(10) == '10th'
# assert ordinalSuffix(11) == '11th'
# assert ordinalSuffix(12) == '12th'
# assert ordinalSuffix(13) == '13th'
# assert ordinalSuffix(14) == '14th'
# assert ordinalSuffix(101) == '101st'


# x = 121
# y = str(x)
# print(y[-2:])

def ordinalSuffix(n):
    n = str(n)
    if n[-2:] in ('11', '12', '13'):
        return f"{n}th"
    elif n[-1] == '1':
        return f"{n}st"
    elif n[-1] == '2':
        return f"{n}nd"
    elif n[-1] == '3':
        return f"{n}rd"
    else:
        return f"{n}th"

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'