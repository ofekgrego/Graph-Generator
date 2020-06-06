import random
from tkinter import *
import tkinter

numOfLines = 0

labelArray = []
entryArray = []
addButtonArray = []

window = Tk()
window.title("Graph Generator")
canvasFrame = Canvas(window, width=1000, height=800, background="gray")
canvasFrame.pack(side=tkinter.LEFT,fill=BOTH,expand=TRUE)
dataFrame = Frame(window,width=300,height=800)
dataFrame.pack(side=tkinter.RIGHT,fill=Y)

def addButtonPressed(graphNum):
    print(graphNum)

def addGraphPressed():
    global numOfLines
    if numOfLines<7:
        labelArray.append(Label(dataFrame,text="Graph N." + str(numOfLines+1)))
        entryArray.append(Entry(dataFrame,width=5))
        addButtonArray.append(Button(dataFrame, text="Add Value",command=lambda numOfLines=numOfLines: addButtonPressed(numOfLines)))

        labelArray[numOfLines].pack()
        entryArray[numOfLines].pack()
        addButtonArray[numOfLines].pack()

        Label(dataFrame,text="",height=2).pack()
        numOfLines += 1

addGraphButton = Button(dataFrame,text="+",command = addGraphPressed)
addGraphButton.pack(side=tkinter.BOTTOM)

window.mainloop()
