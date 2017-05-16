'''
Created on Oct 24, 2010

@author: ola
'''
import Tkinter
import tkMessageBox
import JottoModel

root = Tkinter.Tk()
root.title("Duke Jotto")
entryList = []
spinList = []
buttonList = []
currentIndex = 0
lastGuess = ""

def disable():
    for index in range(len(entryList)):
        entry = entryList[index]
        box = spinList[index]
        button = buttonList[index]
    #for entry,box in zip(entryList,spinList):
        entry.delete(0,Tkinter.END)
        box.selection_clear()
        box.config(values=(0,1,2,3,4,5,6),state=Tkinter.DISABLED)
        button.config(state=Tkinter.DISABLED)
        
def showVictory():
    st = "I have won the game.\n"+\
         "I guessed your word!\n"+\
         "# guesses = "+str(JottoModel.guessCount())
    tkMessageBox.showinfo("Duke Jotto",st)
    disable()
    
def show_nowords():
    st = "I have run out of words.\n"+\
         "something is wrong!\n"
    tkMessageBox.showinfo("Duke Jotto",st)
    disable()

def displayGuess():
    global entryList,currentIndex,lastGuess
    word = JottoModel.getGuess()
    lastGuess = word
    entryList[currentIndex].insert(0,word)
    spinList[currentIndex].config(state=Tkinter.NORMAL)
    buttonList[currentIndex].config(state=Tkinter.NORMAL)
    if currentIndex > 0:
        buttonList[currentIndex-1].config(state=Tkinter.DISABLED)
    currentIndex += 1

def newGame():
    JottoModel.startGame()
    global currentIndex
    currentIndex = 0
    for index in range(len(entryList)):
        entry = entryList[index]
        box = spinList[index]
        button = buttonList[index]
    #for entry,box in zip(entryList,spinList):
        entry.delete(0,Tkinter.END)
        box.selection_clear()
        box.config(values=(0,1,2,3,4,5,6),state=Tkinter.DISABLED)
        button.config(state=Tkinter.DISABLED)
    displayGuess()

def makeMenus():
    global root
    menubar = Tkinter.Menu(root)
    filemenu = Tkinter.Menu(menubar)
    menubar.add_cascade(label='JottoFile',menu=filemenu)
    filemenu.add_command(label='New Game',command=newGame)
    filemenu.add_command(label='Quit',command=root.quit) 
    root.config(menu=menubar)

def processCount(count):
    global lastGuess
    count = int(count)
    if count == 6:
        showVictory()
    else:
        numLeft = JottoModel.processCommon(lastGuess,count)
        print "number of words left is ",numLeft
        if numLeft == 0:
            show_nowords()
        else:
            displayGuess()
    
    
def makeBox(r,c):
    global root
    global entryList,spinList,buttonList
    tfont = ("Helvetica", 14, 'bold')
    entry = Tkinter.Entry(root,font=tfont,width=12)
    if r == 0:
        entry.insert(0,'     ')
    else:
        entry.insert(0,'     ')
    entry.grid(row=r,column=c)
    entryList.append(entry)
    box = Tkinter.Spinbox(root,font=tfont,width=2,
                          values=(0,1,2,3,4,5,6),state=Tkinter.DISABLED)
    box.grid(row=r,column=c+1)
    spinList.append(box)
    button = Tkinter.Button(root,text="GO",
                            font=tfont,command=lambda: processCount(box.get()))
    button.grid(row=r,column=c+2)
    buttonList.append(button)
    disable()

def run_game():
    JottoModel.loadWords("kwords5.txt")
    makeMenus()  
    for row in range(0,20):
        makeBox(row,0)
    
    Tkinter.mainloop()

if __name__ == "__main__":
    run_game()

