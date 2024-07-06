import colorama
from colorama import Fore, Style

y = False
num1 = float(input("Enter first number: "))

while y == False:
  x = str(input("Choose function; +, -, *, / " + Fore.WHITE))
  
  if x in ["+", "-", "*", "/"]:
    y = True
  else:
    print(Fore.RED,"Error, please use the above format!")
    y = False


num2 = float(input("Enter second number: "))


if x == "+":
  print("Your answer is: " + str(num1 + num2) + "!")
elif x == "-":
  print("Your answer is: " + str(num1 - num2) + "!")
elif x == "/":
  print("Your answer is: " + str(num1 / num2) + "!")
elif x == "*" or x == "x":
  print("Your answer is: " + str(num1 * num2) + "!") 

print("Thank you for using Harry's Calculator")