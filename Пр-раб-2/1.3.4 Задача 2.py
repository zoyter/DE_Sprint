# Палиндром
def isPalindrom(data):
    data = data.replace(" ","")
    if data == data[::-1]:
        return True
    return False

x = "taco cat"
print(isPalindrom(x))
x = "rotator"
print(isPalindrom(x))
x = "black cat"
print(isPalindrom(x))