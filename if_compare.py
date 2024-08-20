w = float(input("enter the waist: "))
print(w)

a = w < 25 
b = w >=25 
c = w <= 35


if a:
    print("the waist is extra small")
elif b and c:
    print("medium size waist")
else:
    print("extra large waist")

w = float(input("your waist: "))
print(w)
def waist(w):
    if w < 25:
        return " very small"
    elif w >= 25 and w <= 35:
        return "Medium size"
    elif w >= 35 and w <= 40:
        return "Large size"
    else:
        return "Extra large"
print(waist(w))
    
    




        