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
#
# print("-------------------------------------------------------------------------")
#
# # finding centimeters to inches
#
# centimeters = int(input("Enter value in inches: "))
# inches = (2.54 * centimeters)
# print("Value in centimeters:", inches)
#
# print("-------------------------------------------------------------------------")
#
# # finding kilograms to miligrams
#
# kilograms = int(input("Enter value in kilograms: "))
# miligrams = (1000000 * kilograms)
# print("Value in miligrams:", miligrams)
#
# print("-------------------------------------------------------------------------")
#
# # finding meters to kilometers
#
# meters = int(input("Enter value in meters: "))
# calculate_kilometers = (meters / 1000)
# kilometers = round(calculate_kilometers, 0)  # round function to make rounded value
# print("Value in kilometers:", kilometers)
#
# print("-------------------------------------------------------------------------")
#
# # finding kilometers to miles
#
# kilometers = int(input("Enter value in kilometers: "))
# miles = (kilometers / 1.6)
# print("Value in miles:", miles)
#
# print("-------------------------------------------------------------------------")
#
# # working with list
#
# list = ['Someone1', 'Someone2', 'Someone3']
# print(list)
# list.append('Someone4')  # adds Someone4
# print(list)
# list.pop(1)
# print(list)  # removes Someone2
#
# print("-------------------------------------------------------------------------")
#
# # generating a random password
#
# import random
#
# l = 8  # l for length
# def RandomPassword(l):
#     symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"  # all elements we want to use in password
#     password = ""
#     for i in range(l):
#         password += random.choice(symbols)  # choosing random elements from "symbols"
#     return password
#
# if True:
#     password = RandomPassword(l)
#     print("Random password:", password)  # printing our password
#
# print("-------------------------------------------------------------------------")
#
# print("-------------------------------------------------------------------------")
#
# name = input("Insert your name: ")
# print(f"Welcome {name}!")
#
# print("-------------------------------------------------------------------------")
#
# name = "Viktor "
# surname = "Zaborovets"
#
# print(name + surname)
#
# print("-------------------------------------------------------------------------")
#
# age = int(input("Insert your age: "))
#
# if age < 18:
#     print("You are still too young")
# else:
#     print("You can vote")
#
# print("-------------------------------------------------------------------------")
#
# for num in range(21):
#     if num % 2 == 0:
#         print(num)
#
# print("-------------------------------------------------------------------------")
#
# list = ['apple', 'pineapple', 'not apple', 'not pineapple']
# for list in list:
#     print(list)
#
# print("-------------------------------------------------------------------------")
#
# number1 = int(input("Insert first number: "))
# number2 = int(input("Insert second number: "))
# print(number1 + number2)
#
# print("-------------------------------------------------------------------------")

import tkinter as tk
from tkinter import font


def add_numbers():
    result = float(num1.get()) + float(num2.get())
    result_label.config(text="Result: " + str(result))


def subtract_numbers():
    result = float(num1.get()) - float(num2.get())
    result_label.config(text="Result: " + str(result))


root = tk.Tk()
root.title("Simple Calculator")

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=12)

root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(expand=True)

num1 = tk.Entry(frame, font=("Arial", 14))
num1.pack()

num2 = tk.Entry(frame, font=("Arial", 14))
num2.pack()

button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add", command=add_numbers, font=("Arial", 14), width=10, height=2)
add_button.pack(side=tk.LEFT, padx=5)

subtract_button = tk.Button(button_frame, text="Subtract", command=subtract_numbers, font=("Arial", 14), width=10,height=2)
subtract_button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(frame, font=("Arial", 14))
result_label.pack()

root.mainloop()
