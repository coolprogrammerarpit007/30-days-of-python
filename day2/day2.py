# Day 2: 30 days of python programming


first_name = 'Arpit'
print(type(first_name))
last_name = 'Mishra'
print(type(last_name))
full_name = first_name + " " + last_name
print(type(full_name))
country = "India"
print(type(country))
city = "Jaipur"
print(type(city))
current_age = 25
print(type(current_age))
birth_year = 1999
print(type(birth_year))
is_married = False
print(type(is_married))
is_True = True
print(type(is_True))
is_legit_on = True
print(type(is_legit_on))
favourite_cricketer,favourite_tennis_player,favourite_footballer = "Virat Kohli","Novak Djokovic","Cristiano Ronaldo"
print(f"Number of letters in the first-name: {len(first_name)}")
print(len(first_name),len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one -num_two
product = num_one * num_two
division = num_one/num_two
remainder = num_two%num_one
exp = num_one ** num_two
floor_division = num_one/num_two
circle_radius = 30
area_of_circle = 3.14 * circle_radius ** 2
circum_of_circle = 2 * 3.14 * circle_radius
user_circle_radius = float(input("Enter Radius: "))
print(f"Area of circle: {3.14 *  user_circle_radius * user_circle_radius}")
user_first_name = input("Enter First Name: ").capitalize()
user_last_name = input("Enter Last name: ").capitalize()
user_country = input("Enter Country: ").capitalize()
user_age = int(input("Enter age: "))
print(f"User name is: {user_first_name + " " + user_last_name}. he is {user_age} years old, from {user_country}")



