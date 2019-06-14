from tkinter import Tk, Entry, Label, Button, Radiobutton, IntVar
from time import sleep
from data import acid_rain
import os


class MainEngine(object):

    def __init__(self):
        # initialize tkinter window parameters
        self.root = Tk()
        self.root.title("Acid Rain")
        self.root.geometry("640x480")
        self.root.resizable(0, 0)

        # initialize some engine variables
        self.radioVar = IntVar() # for difficulty option feature
        self.diffCount = 4
        self.diffTime = 80
        self.gameStarted = False

        # call the third phase of initialization
        self.initSecond()


    # 2nd phase of initialization: create widgets
    def initSecond(self):
        ## initialize widgets for difficulty selection
        self.diffLabel = Label(self.root, text="Select the difficulty.")

        # difficulty select options with radiobuttons
        # function difficultySelection will be called if the player hit the diffBtn
        self.radioBtn1 = Radiobutton(text="Easy", variable=self.radioVar, value=1)
        self.radioBtn2 = Radiobutton(text="Normal", variable=self.radioVar, value=2)
        self.radioBtn3 = Radiobutton(text="Hard", variable=self.radioVar, value=3)
        self.diffBtn = Button(self.root, text="Select", command=self.difficultySelection, width=5, height=1)
        
        ## initialize widgets for the game
        self.labelScore = Label(self.root, text="Score: ")
        self.labelLife = Label(self.root, text="Life: ")
        self.labelLineTop = Label(self.root, text="- " * 68)
        self.labelLineBot = Label(self.root, text="- " * 68)
        self.inputEntry = Entry(self.root)

        # inputResponse will be called if the player hit <Return> key
        self.root.bind('<Return>', self.inputResponse)

        # call the third phase of initialization
        self.initThird()


    # 3rd phase of initialization: difficulty selection
    def initThird(self):
        ## difficulty selection, showing all relevant widgets
        self.diffLabel.pack()
        self.radioBtn1.pack()
        self.radioBtn2.pack()
        self.radioBtn3.pack()
        self.diffBtn.pack()

        # execute the game
        self.root.mainloop()

    
    def difficultySelection(self):
        ## get option parameters from an external option file
        # set a directory for the resource file
        pathCurrentDir = os.path.dirname(__file__)  # current script directory
        pathRelDir = "resource/options.txt"
        pathAbsDir = os.path.join(pathCurrentDir, pathRelDir)
        optionFile = open(pathAbsDir, encoding="utf-8")

        # lists for difficulty parameters from the property
        optionDiffCount = []
        optionDiffTime = []

        # find the option parameters and bind to lists
        # these will bind the important parameter only as integer by using slicing
        for optionLine in optionFile.readlines():
            if "DiffCountEasy:" in optionLine:
                optionDiffCount.append(int(optionLine[15:-1]))
            elif "DiffCountNorm:" in optionLine:
                optionDiffCount.append(int(optionLine[15:-1]))
            elif "DiffCountHard:" in optionLine:
                optionDiffCount.append(int(optionLine[15:-1]))
            elif "DiffTimeEasy:" in optionLine:
                optionDiffTime.append(int(optionLine[14:-1]))
            elif "DiffTimeNorm:" in optionLine:
                optionDiffTime.append(int(optionLine[14:-1]))
            elif "DiffTimeHard:" in optionLine:
                optionDiffTime.append(int(optionLine[14:-1]))


        if self.radioVar.get() == 1:
            self.diffCount = optionDiffCount[0]
            self.diffTime = optionDiffTime[0]

        elif self.radioVar.get() == 2:
            self.diffCount = optionDiffCount[1]
            self.diffTime = optionDiffTime[1]

        elif self.radioVar.get() == 3:
            self.diffCount = optionDiffCount[2]
            self.diffTime = optionDiffTime[2]


        self.gameStart()


    def gameStart(self):
        # remove all widgets for difficulty selection
        self.radioBtn1.destroy()
        self.radioBtn2.destroy()
        self.radioBtn3.destroy()
        self.diffBtn.destroy()
        self.diffLabel.destroy()

        # initialize the game
        self.gameStarted = True
        self.labelScore.place(x=10, y=5)
        self.labelLife.place(x=550, y=5)
        self.labelLineTop.place(x=10, y=25)
        self.labelLineBot.place(x=10, y=430)
        self.inputEntry.place(x=240, y=450)
        


    def inputResponse(self, event):

        if self.gameStarted == True:
            print(self.inputEntry.get())

        else:
            pass


    def inGame(self):
        pass


test3 = MainEngine()