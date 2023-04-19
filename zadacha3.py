def remove_brackets(text):
    result1 = ""
    inside_brackets = False
    for char in text:
        if char == '(':
            inside_brackets = True
        elif char == ')':
            inside_brackets = False
        elif not inside_brackets:
            result1 += char
    return result1


user_input = input("Введи текст с круглыми скобками: ")
result = remove_brackets(user_input)
print(result)
