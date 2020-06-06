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
showHideButtonArray = []
showHideFuncArray = []
infoArray = []
colorArray = ["#32a852","#2c8c96","#472c9e",
            "#e3fa39","#fa9639","#fa3939","#ad0096"]

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
            if showHideFuncArray[i] == False:
                maxHeight = height-(padding*2)
                spaceBetweenPoints = (width-(padding*2))/len(infoArray[i])
                maxPlace = max(infoArray[i])
                eachPlaceHeight = (height-padding*2)/max(maxPlace,1)

                for j in range(len(infoArray[i])-1):
                    canvasFrame.create_line((j)*spaceBetweenPoints+padding,maxHeight-infoArray[i][j]*eachPlaceHeight+padding,
                    (j+1)*spaceBetweenPoints+padding,maxHeight-infoArray[i][j+1]*eachPlaceHeight+padding,
                    width=3,fill=colorArray[i])

def configure(event):
    global width, height
    width = event.width
    height = event.height
    makingGraph()

def showHideGraphPressed(graphNum):
    if showHideFuncArray[graphNum] == False:
        showHideFuncArray[graphNum] = True
    else:
        showHideFuncArray[graphNum] = False
    makingGraph()

def addButtonPressed(graphNum):
    if entryArray[graphNum].get() == "":
        infoArray[graphNum].append(infoArray[graphNum][graphNum-1])
    else:
        infoArray[graphNum].append(int(entryArray[graphNum].get()))
    makingGraph()


def addGraphPressed():
    global numOfLines
    if numOfLines<7:
        labelArray.append(Label(dataFrame,text="Graph N." + str(numOfLines+1)))
        entryArray.append(Entry(dataFrame,width=5))
        addButtonArray.append(Button(dataFrame, text="Add Value",command=lambda numOfLines=numOfLines: addButtonPressed(numOfLines)))
        showHideButtonArray.append(Button(dataFrame,text="Show/Hide Graph", command=lambda numOfLines=numOfLines: showHideGraphPressed(numOfLines)))

        labelArray[numOfLines].pack()
        entryArray[numOfLines].pack()
        addButtonArray[numOfLines].pack()
        showHideButtonArray[numOfLines].pack()
        infoArray.append([0])
        showHideFuncArray.append(False)

        Label(dataFrame,text="",height=2).pack()
        numOfLines += 1

addGraphButton = Button(dataFrame,text="+",command = addGraphPressed)
addGraphButton.pack(side=tkinter.BOTTOM)

canvasFrame.bind("<Configure>", configure)

window.mainloop()
