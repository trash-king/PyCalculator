from tkinter import *
from target import *
import os


pyCalculatorRoot = Tk()

pyCalculatorRoot.title("PyCalculator Version " + version)
pyCalculatorRoot.geometry('500x500')

additionButton = Button(pyCalculatorRoot, text = "+", fg = "black", command = addTwoIntegers)
subtractionButton = Button(pyCalculatorRoot, text = "-", fg = "black", command = subtractTwoIntegers)
divisionButton = Button(pyCalculatorRoot, text = "/", fg = "black", command = divideTwoIntegers)
multiplyButton = Button(pyCalculatorRoot, text = "x", fg = "black", command = multiplyTwoIntegers)

negativeButton = Button(pyCalculatorRoot, text = "+/-", fg = "black", command = setNegative)
exponentButton = Button(pyCalculatorRoot, text = "eX", fg = "black", command = setExponent)
percentageButton = Button(pyCalculatorRoot, text = "%", fg = "black", command = findPercentage)
modulusButton = Button(pyCalculatorRoot, text = "MOD", fg="black", command= findModulus)

mainNumericalEntry = Entry(pyCalculatorRoot, width=50)
mainNumericalEntry.place(relx=0.5, anchor=CENTER)
mainNumericalEntry.grid(column=1, row=0)


additionButton.grid(column=1,row=2)
subtractionButton.grid(column=3,row=2)
multiplyButton.grid(column=5,row=2)
divisionButton.grid(column=7,row=2)

negativeButton.grid(column=1,row=3)
exponentButton.grid(column=3,row=3)
percentageButton.grid(column=5,row=3)
modulusButton.grid(column=7,row=3)

pyCalculatorRoot.mainloop()
