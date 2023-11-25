# print('-----------------------------------------------------')
#
# # Prompt user to input age and provide a message based on the input
# age = int(input("Insert your age: "))
# if age < 18:
#     print("You are still too young")
# else:
#     print("You are welcome")
#
# print('-----------------------------------------------------')
#
# # Create a list, sort it, and print the largest element in the list
# list1 = [1, 5, 7, 1, 6, 9, 2, 7, 3]
# list1.sort()
# print("Largest element is:", list1[-1])
#
# print('-----------------------------------------------------')
#
# # Prompt user to input a number and display its multiplication table up to 10
# number = int(input("Input a number: "))
#
# multiply1 = number * 1
# multiply2 = number * 2
# multiply3 = number * 3
# multiply4 = number * 4
# multiply5 = number * 5
# multiply6 = number * 6
# multiply7 = number * 7
# multiply8 = number * 8
# multiply9 = number * 9
# multiply10 = number * 10
#
# print(f"{number} * 1 = {multiply1}")
# print(f"{number} * 2 = {multiply2}")
# print(f"{number} * 3 = {multiply3}")
# print(f"{number} * 4 = {multiply4}")
# print(f"{number} * 5 = {multiply5}")
# print(f"{number} * 6 = {multiply6}")
# print(f"{number} * 7 = {multiply7}")
# print(f"{number} * 8 = {multiply8}")
# print(f"{number} * 9 = {multiply9}")
# print(f"{number} * 10 = {multiply10}")
#
# print('-----------------------------------------------------')
#
# # Prompt user to input a sentence and display its reversed form
# sentence = input("Write any sentence: ")
# reversed = sentence[::-1]
# print("Reversed sentence: ", reversed)
#
# print('-----------------------------------------------------')
#
# # Define a factorial function and calculate the factorial of a provided number
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# num = int(input("Enter a number to calculate its factorial: "))
#
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     fact = factorial(num)
#     print("The factorial of", num, "is", fact)
#
# print('-----------------------------------------------------')
#
# # Prompt user to input a number and determine if it's even or odd
# even_or_not = int(input("Enter a number: "))
# if even_or_not % 2 == 0:
#     print(even_or_not, "is an even number")
# else:
#     print(even_or_not, "is an odd number")
#
# print('-----------------------------------------------------')
#
# # Create lists, concatenate them, and display the individual lists and the concatenated list
# list2 = [1, 2]
# list3 = [3, 4]
# list4 = list2 + list3
# print(list2)
# print(list3)
# print(list4)
#
# print('-----------------------------------------------------')
import tkinter as tk

def click():
    global count
    count += 1
    label.config(text=f"Clicked: {count} times", fg="#BBAB8C", bg="#FAEED1", font=("Comic Sans MS", 24, "bold"))

def reset():
    global count
    count = 0
    label.config(text="Click the button to start clicking", fg="#BBAB8C", bg="#FAEED1", font=("Comic Sans MS", 22, "bold"))

count = 0

root = tk.Tk()
root.title("Python Clicker")
root.configure(bg="#FDF7E4")

frame = tk.Frame(root, padx=100, pady=80, bg="#FDF7E4")
frame.pack()

label = tk.Label(frame, text="Click the button to start clicking", fg="#BBAB8C", bg="#FAEED1", font=("Comic Sans MS", 22, "bold"), pady=40)
label.pack()

click_button = tk.Button(frame, text="Click Me!", command=click, width=30, height=2, bg="#FAEED1", fg="#BBAB8C", font=("Comic Sans MS", 20, "bold"))
click_button.pack(pady=30)

reset_button = tk.Button(frame, text="Reset", command=reset, width=30, height=2, bg="#FAEED1", fg="#BBAB8C", font=("Comic Sans MS", 20, "bold"))
reset_button.pack()

root.mainloop()

