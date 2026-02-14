'''\
chatloop.py
ACC 399 c1-4
February 14, 2026

A simple chat that illustrates an indeterminate loop a.k.a. "while loop"
'''

import linear as lin

strName = lin.greet()

while True:
    strN0 = input("Please enter an integer (-1 to exit): ")
    if (strN0 == "-1"):
        break
    strN1 = input("Now enter another one: ")

    intN0 = int(strN0)
    intN1 = int(strN1)
    intSum = intN0 + intN1

    print(f"Their sum is: {intSum}\n")

print(f"\nBye {strName} -- Thanks for visiting!\n")
