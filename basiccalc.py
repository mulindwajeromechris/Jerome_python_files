from math import*
num_1 = input("enter a number: ")
num_2 = input("enter other number: ")
result = float(num_1) + float(num_2)
print("Sum: " +str(result))

result_2 = sqrt(abs(float(num_1)))
print("Square root: " +str(result_2))

result_3 = float(divmod(num_1, num_2))
print("The quotient is: " +str(result_3))