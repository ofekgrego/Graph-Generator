import random
from tkinter import *
import tkinter

numOfLines = 0
padding = 60
width = 1000
height = 800

labelArray = []
entryArray = []
addButtonArray = []
infoArray = []

window = Tk()
window.title("Graph Generator")
canvasFrame = Canvas(window, width=1000, height=800, background="gray")
canvasFrame.pack(side=tkinter.LEFT,fill=BOTH,expand=TRUE)
dataFrame = Frame(window,width=300,height=800)
dataFrame.pack(side=tkinter.RIGHT,fill=Y)

canvasFrame.create_line(padding,height-padding,width-padding,height-padding, width=3)
canvasFrame.create_line(padding,padding,padding,height-padding, width=3)

def makingGraph():
    canvasFrame.delete("all")
    canvasFrame.create_line(padding,height-padding,width-padding,height-padding, width=3)
    canvasFrame.create_line(padding,padding,padding,height-padding, width=3)
    if numOfLines>0:
        for i in range(len(infoArray)):
            maxHeight = height-(padding*2)
            spaceBetweenPoints = (width-(padding*2))/len(infoArray[i])
            maxPlace = max(infoArray[i])
            eachPlaceHeight = (height-padding*2)/maxPlace

            for j in range(len(infoArray[0])-1):
                canvasFrame.create_line((j)*spaceBetweenPoints+padding,maxHeight-infoArray[i][j]*eachPlaceHeight+padding,(j+1)*spaceBetweenPoints+padding,maxHeight-infoArray[i][j+1]*eachPlaceHeight+padding)

def configure(event):
    global width, height
    width = event.width
    height = event.height
    makingGraph()


def addButtonPressed(graphNum):
    if entryArray[graphNum].get() == "":
        infoArray[graphNum].append(infoArray[graphNum][graphNum-1])
    else:
        infoArray[graphNum].append(int(entryArray[graphNum].get()))
    print(infoArray)
    makingGraph()


def addGraphPressed():
    global numOfLines
    if numOfLines<7:
        labelArray.append(Label(dataFrame,text="Graph N." + str(numOfLines+1)))
        entryArray.append(Entry(dataFrame,width=5))
        addButtonArray.append(Button(dataFrame, text="Add Value",command=lambda numOfLines=numOfLines: addButtonPressed(numOfLines)))

        labelArray[numOfLines].pack()
        entryArray[numOfLines].pack()
        addButtonArray[numOfLines].pack()
        infoArray.append([0,5,3])

        Label(dataFrame,text="",height=2).pack()
        numOfLines += 1

addGraphButton = Button(dataFrame,text="+",command = addGraphPressed)
addGraphButton.pack(side=tkinter.BOTTOM)

canvasFrame.bind("<Configure>", configure)

window.mainloop()
