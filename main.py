from tkinter import Tk, Entry, Label, Button, Radiobutton, IntVar, END
from time import sleep
from data import acid_rain
import os


class MainEngine(object):

    def __init__(self):
        ## get option parameters from an external option file
        # set a directory for the resource file
        pathCurrentDir = os.path.dirname(__file__)  # current script directory
        pathRelDir = "resource/options.txt"
        pathAbsDir = os.path.join(pathCurrentDir, pathRelDir)
        optionFile = open(pathAbsDir, encoding="utf-8")

        # lists for difficulty parameters from the property
        self.optionDiffCount = []
        self.optionDiffTime = []
        self.optionWidgetCoordinate = []

        # find the option parameters and bind to lists
        # these will bind the important parameter only as integer by using slicing
        for optionLine in optionFile.readlines():
            if "DiffCountEasy:" in optionLine:
                self.optionDiffCount.append(int(optionLine[15:-1]))
            elif "DiffCountNorm:" in optionLine:
                self.optionDiffCount.append(int(optionLine[15:-1]))
            elif "DiffCountHard:" in optionLine:
                self.optionDiffCount.append(int(optionLine[15:-1]))
            elif "DiffTimeEasy:" in optionLine:
                self.optionDiffTime.append(int(optionLine[14:-1]))
            elif "DiffTimeNorm:" in optionLine:
                self.optionDiffTime.append(int(optionLine[14:-1]))
            elif "DiffTimeHard:" in optionLine:
                self.optionDiffTime.append(int(optionLine[14:-1]))
            elif "UILabelScoreX:" in optionLine:    # index 0
                self.optionWidgetCoordinate.append(int(optionLine[15:-1]))
            elif "UILabelScoreY:" in optionLine:    # index 1
                self.optionWidgetCoordinate.append(int(optionLine[15:-1]))
            elif "UILabelLifeX:" in optionLine:     # index 2
                self.optionWidgetCoordinate.append(int(optionLine[14:-1]))
            elif "UILabelLifeY:" in optionLine:     # index 3
                self.optionWidgetCoordinate.append(int(optionLine[14:-1]))
            elif "UILabelLineTopX:" in optionLine:  # index 4
                self.optionWidgetCoordinate.append(int(optionLine[17:-1]))
            elif "UILabelLineTopY:" in optionLine:  # index 5
                self.optionWidgetCoordinate.append(int(optionLine[17:-1]))
            elif "UILabelLineBotX:" in optionLine:  # index 6
                self.optionWidgetCoordinate.append(int(optionLine[17:-1]))
            elif "UILabelLineBotY:" in optionLine:  # index 7
                self.optionWidgetCoordinate.append(int(optionLine[17:-1]))
            elif "UIinputTxtBoxX:" in optionLine:   # index 8
                self.optionWidgetCoordinate.append(int(optionLine[16:-1]))
            elif "UIinputTxtBoxY:" in optionLine:   # index 9
                self.optionWidgetCoordinate.append(int(optionLine[16:-1]))


        # initialize tkinter window parameters
        self.root = Tk()
        self.root.title("Acid Rain")
        self.root.geometry("640x480")
        self.root.resizable(0, 0)

        # initialize some engine variables
        self.radioVar = IntVar() # for difficulty option feature
        self.diffCount = self.optionDiffCount[0]    # default: easy
        self.diffTime = self.optionDiffTime[0]      # default: easy
        self.statusGame = False
        self.statusScore = 0
        self.statusLife = 10

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
        self.labelScore = Label(self.root, text=("Score: " + str(self.statusScore)))
        self.labelLife = Label(self.root, text=("Life: " + str(self.statusLife)))
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
        if self.radioVar.get() == 1:
            self.diffCount = self.optionDiffCount[0]
            self.diffTime = self.optionDiffTime[0]

        elif self.radioVar.get() == 2:
            self.diffCount = self.optionDiffCount[1]
            self.diffTime = self.optionDiffTime[1]

        elif self.radioVar.get() == 3:
            self.diffCount = self.optionDiffCount[2]
            self.diffTime = self.optionDiffTime[2]


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
        self.labelScore.place(x=self.optionWidgetCoordinate[0], y=self.optionWidgetCoordinate[1])
        self.labelLife.place(x=self.optionWidgetCoordinate[2], y=self.optionWidgetCoordinate[3])
        self.labelLineTop.place(x=self.optionWidgetCoordinate[4], y=self.optionWidgetCoordinate[5])
        self.labelLineBot.place(x=self.optionWidgetCoordinate[6], y=self.optionWidgetCoordinate[7])
        self.inputEntry.place(x=self.optionWidgetCoordinate[8], y=self.optionWidgetCoordinate[9])
        


    def inputResponse(self, event):

        if self.statusGame == True:
            acid_rain.game.inputResponse(self.inputEntry.get())

            # clear the text box
            self.inputEntry.delete(0, END)


        else:
            pass


    def inGame(self):
        pass


test3 = MainEngine()