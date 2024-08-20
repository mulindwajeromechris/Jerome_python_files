friends = ["sam", "ken","Ben", "Max", "Ben", "Tom"]
numbers = [1,2,3,4,5]
print(friends)
print(numbers)

friends.extend(numbers)
print(friends)

numbers.extend(friends)
print(numbers)

friends = ["sam", "ken", "Max", "Ben", "Tom"]
numbers = [5,4,1,3,2]
friends.append("Big")
numbers.append(6)
print(friends)
print(numbers)

friends.insert(2, "Pat")
print(friends)

friends.remove("Max")
print(friends)
friends.pop()
print(friends)
print(friends.count("Ben"))
print(friends.index("Ben"))

numbers.sort()
print(numbers)

numbers_2 = numbers.reverse()
print(numbers)

friends_3 = friends.copy()
print(friends_3)