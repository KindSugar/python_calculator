#Калькулятор

while True:
    a = input("Первое число: ")
    b = input("Второе число: ")
    c = input ("Введите знак:")

    if c == "+":
        try:
            print(float(a) + float(b))
        except:
            print("Error!")
    elif c == "-":
        try:
            print(float(a) - float(b))
        except:
            print("Error!")
    elif c == "*":
        try:
            print(float(a) * float(b))
        except:
            print("Error!")
    elif c == "**":
        try:
            print(float(a) ** float(b))
        except:
            print("Error!")
    elif c == "/":
        try:
            print(float(a) / float(b))
        except:
            print("Error!")





