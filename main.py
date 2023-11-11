# # finding the perimeter of a rectangle
# length = 5
# width = 2
# print(f'{length * 2 + width * 2}cm - perimeter')
#
# # finding the total cost of 3 full complected computers
# cost_mouse = 12
# cost_keyboard = 15
# cost_computer = 51
#
# total_cost = cost_computer + cost_mouse + cost_keyboard
# print(f'{total_cost * 3}$ - total cost of 3 full complected computers')
#
# # celsius to another temperature scale converter
# celsius = int(input("Enter the temperature in celsius: "))
# fahrenheit = (1.8 * celsius) + 32.
# print("Temperature in fahrenheit :", fahrenheit)
#
# celsius = int(input("Enter the temperature in celsius: "))
# kelvin = celsius + 273.15
# print("Tempeature in kelvin:", kelvin)

#finding centimeters to inches
centimeters = int(input("Enter value in inches: "))
inches = (2.54 * centimeters)
print("Value in centimeters:", inches)

#finding kilograms to miligrams
kilograms = int(input("Enter value in kilograms: "))
miligrams = (1000000 * kilograms)
print("Value in miligrams:", miligrams)

#finding meters to kilometers
meters = int(input("Enter value in meters: "))
calculate_kilometers = (meters /1000)
kilometers = round(calculate_kilometers,0) #round function to make rounded value
print("Value in kilometers:", kilometers)

#finding kilometers to miles
kilometers = int(input("Enter value in kilometers: "))
miles = (1.61 * kilometers)
print("Value in miles:", miles)

#working with list
list = ['Someone1', 'Someone2', 'Someone3']
print(list)
list.append('Someone4') #adds Someone4
print(list)
list.pop(1)
print(list) #removes Someone2


