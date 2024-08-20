Day_conversions = {
1 : "Monday",
"Tue" : "Tuesday",
"Wed" : "Wednesday",
"Thur" : "Thursday",
"Fri" : "Friday",
"Sat" : "Saturday",
"Sun" : "Sunday",
}

print(Day_conversions["Wed"])
print(Day_conversions.get("Thur"))
print(Day_conversions.get("Jan", "Not valid"))
print(Day_conversions[1])