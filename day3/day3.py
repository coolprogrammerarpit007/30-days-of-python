# # 30 Days of Python Programming
# # DAY-3 Exercise

# person_age = 25
# person_height = 180.5
# complex_number = 5+7j
# base = float(input("Enter base of triangle: "))
# height = float(input("Enter height of triangle: "))
# area = (base * height) * 0.5
# print(f"Area of Triangle is: {area}")
# side_a = float(input("Enter Side A of triangle: "))
# side_b = float(input("Enter Side B of triangle: "))
# side_c = float(input("Enter Side C of triangle: "))
# print(f"Perimeter of Triangle is: {side_a+side_b+side_c}")
# rectangle_width = float(input("Width of Rectangle: "))
# rectangle_height = float(input("Height of Rectangle: "))
# area_of_rectangle = rectangle_width * rectangle_height
# print(f"Area of Rectangle: {area_of_rectangle}")
# perimeter_of_rectangle = 2 * (rectangle_width + rectangle_height)
# print(f"Perimeter of rectangle: {perimeter_of_rectangle}")
# print(len('python') > len('dragon'))
# print('on' in 'python' and 'on' in 'dragon')


# Calculate pay of the person
# hours = int(input("Enter Hours: "))
# rate_per_hour = int(input("Enter rate per hour: "))
# print(f"Your weekly earning is: {hours * rate_per_hour}")

# script to calculate number of seconds a person can live.
# number_of_years = int(input("Enter number of years: "))
# print(f"You have lived for: {number_of_years * 365 * 24 * 60 *60} seconds.")
# Script to print this pattern.
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1,6):
    print(f"{i} 1 {i * 1} {i ** 2} {i ** 3}")