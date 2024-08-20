num_1 = float(input("enter first number: "))
op = input("enter operator: ")
num_2 = float(input("enter second number: "))
if op == "+":
    print("the sum: ", +num_1 + num_2)
elif op == "-":
    print("the difference: ", +num_1 - num_2)
elif op == "/":
    print("the quotient: ", +num_1/num_2)
elif op == "*":
    print("the product: ", +num_1*num_2)
else:
    print("ERROR")