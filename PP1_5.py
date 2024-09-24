'''
    Lesson: Typecasting Practice
    Author: Aiden
    Date Created: Sept 23, 2024
    Date Last Modified: Sept 23, 2024
'''
def q1():
  num = input("Input an integer: ")
  num = int(num)
  print(num+3)
  #Write Assignment code here

def q2():
  num1 = input("Input a number: ")
  num1 = (str(num1)+'4')
  num1 = (float(num1))
  print(num1+2)

  #Write Assignment code here

def q3():
  radius = input("Input a radius: ")
  radius = (float(radius))
  print (3.14*radius**2)

  #Write Assignment code here

def q4():
  num2 = input("Input a number: ")
  num2 = (float(num2))
  num2 = (num2*12)
  num2 = (int(num2))
  print(num2)

  #Write Assignment code here

def q5():
  num3 = input("Input an integer: ")
  num3 = (int(num3))
  print(f"Your number + 5 is {num3+5}")
  #Write Assignment code here

#Comment this code out when running tests
#Do not comment this out when running your program normally
'''
q1()
q2()
q3()
q4()
q5()
'''