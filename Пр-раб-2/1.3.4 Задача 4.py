# Валидность скобок
all_brackets=["{", "}", "[", "]", "(", ")"]
left=all_brackets[::2]
#right=all_brackets[1::2]

def isCorrectBrackets(data):
    if len(data) % 2 !=0:
        return False
    stack=[]
    for i in data:
        if i in left:
            stack.append(i)
        else:
            if all_brackets[all_brackets.index(i)-1] != stack[-1]:
                return False
            stack.pop(-1)
    if len(stack)>0:
        return False
    return True


x = "[{}({})]"
print(isCorrectBrackets(x))
x = "{]"
print(isCorrectBrackets(x))
x = "{"
print(isCorrectBrackets(x))
x = "{[()"
print(isCorrectBrackets(x))