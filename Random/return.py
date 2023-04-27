def suma():
    print("calculator")
    print("This calculator only can use sum")

    num1 = int(input("Firts number: "))
    num2 = int(input("Second number: "))

    suma_operation = num1 + num2
    return suma_operation

suma = suma()
print(f"result: {suma}")