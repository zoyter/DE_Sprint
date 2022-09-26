# целоче числов  римское

data = {1: 'IVX', 10: 'XLC', 100: 'CDM', 1000: 'M  '}

def intToRome(number):
    result = ''
    for i in (1000, 100, 10, 1):
        if number // i != 0:
            a, b, c = data[i]
            S = (a, a * 2, a * 3, a + b, b, b + a, b + 2 * a, b + 3 * a, a + c)
            result += S[number // i - 1]
            number = number - (number // i) * i
    return result


x = 3
print(intToRome(x))
x = 9
print(intToRome(x))
x = 1945
print(intToRome(x))
x = 2048
print(intToRome(x))