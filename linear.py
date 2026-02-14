'''\
linear.py
ACC 399 c1-4
February 14, 2026

A linear chat illustrating:
 + variables
 +  + string
 +  + integer
 + functions
 + logic
 +  + Boolean variables
 +  +  + [ True, False ]
 +  +  + [   1 ,    0  ]
 +  + Conditional statements
 +  +  + if
 +  +  + if - else
 +  +  + if - elif - ... - else
'''

def greet():
    print("Hi!")
    strFirst = input("What is your name? ")

    # if (strFirst in ["Malia", "Pua", "Kimo", "Nalu"]):
    #         print("Aloha e ", strFirst, ".  Me ke pumehana.", sep='')
    # elif (strFirst in ["Colette", "Margot", "Jacques", "Olivier"]):
    #      print("Salut ", strFirst, ".  Enchanté.", sep='')
    # else:
    #     print("Hi ", strFirst, ", nice to meet you!", sep='')

    print("Hi ", strFirst, ", nice to meet you!", sep='')

    return strFirst

def numericalInputs():
    strN0 = input("Please enter an integer: ")
    strN1 = input("Now enter another one: ")
    
    # print("Their combo is:", strN0 + strN1)
    print(f"Their combo is: {strN0 + strN1}")

    intN0 = int(strN0)
    intN1 = int(strN1)
    intSum = intN0 + intN1
    # print("Their sum is: ", intSum)
    print(f"Their sum is: {intSum}")

    # if (intSum % 2 == 0):
    #     print("The sum is even.")
    # else:
    #     print("The sum is odd.")

    return intSum

    
print("The value of __name__ is", __name__)

if (__name__ == "__main__"):
    strName = greet()
    iResult = numericalInputs()
    print(f"Bye {strName} -- See you next time! (The sum was {iResult}.)")
