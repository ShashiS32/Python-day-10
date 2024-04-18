import random

operation = input("What operation would you like to do?\n(Multiplication , Division , Addition , or Subtraction) ").lower()
num1 = float(input("What is you first number? "))
num2 = float(input("What is you second number? "))
digits = int(input("How many decimal places would you like to round to? "))


def addition(num1 , num2):
  answer = float(num1) + float(num2)
  print(round(answer , digits))

def subtraction(num1 , num2):
  answer = float(num1) - float(num2)
  print(round(answer , digits))

def multiplication(num1 , num2):
  answer = float(num1) * float(num2)
  print(round(answer , digits))

def division(num1 , num2):
  if num2 == 0:
    print("Undefined")
  else:
    answer = float(num1) / float(num2)
    print(round(answer , digits))
  


if operation == "addition":
  addition(num1 , num2)
elif operation == "subtraction":
  subtraction(num1 , num2)
elif operation == "multiplication":
  multiplication(num1 , num2)

elif operation == "division":
  division(num1 , num2)

else:
  print ("Invalid Choice")
  