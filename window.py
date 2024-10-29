from tkinter import *
from target import *


pyCalculatorRoot = Tk()

pyCalculatorRoot.title("PyCalculator Version " + version)
pyCalculatorRoot.geometry('500x500')


#---------- BUTTON PLACEMENT ----------#

def createWindow():

    firstIntegerEntry = Entry(pyCalculatorRoot, width=20)
    secondIntegerEntry = Entry(pyCalculatorRoot, width=20)

    resultOfEquation = Text(pyCalculatorRoot, width = 5, height = 1)

    additionButton = Button(pyCalculatorRoot, text = "+", fg = "black", command = addTwoIntegers(firstIntegerEntry.get(), secondIntegerEntry.get()))
    subtractionButton = Button(pyCalculatorRoot, text = "-", fg = "black", command = subtractTwoIntegers(firstIntegerEntry.get(), secondIntegerEntry.get()))
    divisionButton = Button(pyCalculatorRoot, text = "/", fg = "black", command = divideTwoIntegers(firstIntegerEntry.get(), secondIntegerEntry.get()))
    multiplyButton = Button(pyCalculatorRoot, text = "x", fg = "black", command = multiplyTwoIntegers(firstIntegerEntry.get(), secondIntegerEntry.get()))

    negativeButton = Button(pyCalculatorRoot, text = "+/-", fg = "black", command = setNegative)
    exponentButton = Button(pyCalculatorRoot, text = "eX", fg = "black", command = setExponent)
    percentageButton = Button(pyCalculatorRoot, text = "%", fg = "black", command = findPercentage)
    modulusButton = Button(pyCalculatorRoot, text = "MOD", fg="black", command= findModulus)

    equalsButton = Button(pyCalculatorRoot, text = "=", fg="black", command = answerEquation)



    firstIntegerEntry.grid(column = 1, row = 1)
    secondIntegerEntry.grid(column = 3, row = 1)
    resultOfEquation.grid(column=5, row = 1)

    #mainNumericalEntry = Entry(pyCalculatorRoot, width=50)
    #mainNumericalEntry.place(relx=0.5, anchor=CENTER)
    #mainNumericalEntry.grid(column=1, row=0)


    additionButton.grid(column=1,row=2)
    subtractionButton.grid(column=3,row=2)
    multiplyButton.grid(column=5,row=2)
    divisionButton.grid(column=7,row=2)

    negativeButton.grid(column=1,row=3)
    exponentButton.grid(column=3,row=3)
    percentageButton.grid(column=5,row=3)
    modulusButton.grid(column=7,row=3)

    equalsButton.grid(column=5,row = 5)