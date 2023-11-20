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
#
# import tkinter as tk
# from tkinter import font
#
#
# def perform_operation(operation):
#     if operation == 'add':
#         result = float(num1.get()) + float(num2.get())
#     elif operation == 'subtract':
#         result = float(num1.get()) - float(num2.get())
#     elif operation == 'multiply':
#         result = float(num1.get()) * float(num2.get())
#     elif operation == 'divide':
#         num2_value = float(num2.get())
#         if num2_value != 0:
#             result = float(num1.get()) / num2_value
#         else:
#             result = "Error: Division by zero"
#     elif operation == 'power':
#         result = float(num1.get()) ** float(num2.get())
#     elif operation == 'clear':
#         num1.delete(0, tk.END)
#         num2.delete(0, tk.END)
#         result_label.config(text="Result:")
#         return
#     else:
#         result = "Error: Invalid operation"
#
#     result_label.config(text=f"Result: {result}")
#
#
# root = tk.Tk()
# root.title("Calculator")
# root.geometry("800x300")
#
# comic_sans_font = font.Font(family='Comic Sans MS', size=12)
#
# background_color = '#F3EEEA'
# button_color = '#B0A695'
# button_hover_color = '#776B5D'
# text_color = 'white'
# result_background = '#776B5D'
#
# frame = tk.Frame(root, bg=background_color)
# frame.pack(expand=True, fill='both', padx=10, pady=10)
#
# num1 = tk.Entry(frame, font=comic_sans_font, bd=0, highlightthickness=2, highlightcolor=button_color)
# num1.pack(pady=10, padx=20, ipady=5, fill='x')
#
# num2 = tk.Entry(frame, font=comic_sans_font, bd=0, highlightthickness=2, highlightcolor=button_color)
# num2.pack(pady=10, padx=20, ipady=5, fill='x')
#
# button_frame = tk.Frame(frame, bg=background_color)
# button_frame.pack(pady=10)
#
# button_style = {
#     'font': comic_sans_font,
#     'width': 10,
#     'height': 2,
#     'bg': button_color,
#     'fg': text_color,
#     'activebackground': button_hover_color,
#     'bd': 0,
# }
#
#
# def create_button(parent, text, operation):
#     button = tk.Button(parent, text=text, command=lambda: perform_operation(operation), **button_style)
#     button.pack(side=tk.LEFT, padx=5)
#     return button
#
#
# add_button = create_button(button_frame, "Add", 'add')
# subtract_button = create_button(button_frame, "Subtract", 'subtract')
# multiply_button = create_button(button_frame, "Multiply", 'multiply')
# divide_button = create_button(button_frame, "Divide", 'divide')
# power_button = create_button(button_frame, "Power", 'power')
#
# clear_button = create_button(button_frame, "Clear", 'clear')
# clear_button.config(bg='red')
#
# result_label = tk.Label(frame, font=comic_sans_font, bg=result_background, fg='white', padx=10, pady=5, bd=3, relief='ridge')
# result_label.pack(pady=10)
#
# root.mainloop()

import tkinter as tk
import math

def calculate():
    try:
        expression = entry.get()
        # Replace 'x' with '*' for multiplication
        expression = expression.replace('x', '*')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def press(key):
    entry.insert(tk.END, key)

def backspace():
    entry.delete(len(entry.get()) - 1)

def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def power():
    try:
        value = float(entry.get())
        result = value ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Enhanced Calculator")

# Background color
root.configure(bg='#F3EEEA')

entry = tk.Entry(root, width=40, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button colors and font color
button_color = '#d1c4ba'
font_color = '#F3EEEA'

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    '√', 'x²', '⌫', '.'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=12, height=2, bg=button_color, fg=font_color, font=('Arial', 14, 'bold'), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif button == 'C':
        tk.Button(root, text=button, width=12, height=2, bg=button_color, fg=font_color, font=('Arial', 14, 'bold'), command=clear).grid(row=row, column=col, padx=5, pady=5)
    elif button == '√':
        tk.Button(root, text=button, width=12, height=2, bg=button_color, fg=font_color, font=('Arial', 14, 'bold'), command=square_root).grid(row=row, column=col, padx=5, pady=5)
    elif button == 'x²':
        tk.Button(root, text=button, width=12, height=2, bg=button_color, fg=font_color, font=('Arial', 14, 'bold'), command=power).grid(row=row, column=col, padx=5, pady=5)
    elif button == '⌫':
        tk.Button(root, text=button, width=12, height=2, bg=button_color, fg=font_color, font=('Arial', 14, 'bold'), command=backspace).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=12, height=2, bg=button_color, fg=font_color, font=('Arial', 14, 'bold'), command=lambda key=button: press(key)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()