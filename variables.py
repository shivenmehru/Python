#Day 2: 30 Days of python programming

#using snake_case and not camelCase

first_name = "Shiven"
last_name = "Mehru"
full_name = "Shiven Mehru"
country = "India"
city = "New Delhi"
age = 26
year = 2023
is_married = "No"
is_True = False
is_light_on = False
language , level, day = "Python", "Beginner" , 26

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_True))
print(type(is_light_on))
print(type(language))
print(type(level))
print(type(day))


print(len(first_name))
print(len(last_name))

print(min(int(len(first_name)), int(len(last_name))))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one/num_two
remainder = num_two%num_one
exp = num_one ** num_two
floor_division = num_one//num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

radius = 30
area = 3.14 * (30**2)
print(area)
circumference = 2 * 3.14 * 30
print(circumference)

radius_input = input("Enter radius")
print(3.14 * (int(radius_input) ** 2))