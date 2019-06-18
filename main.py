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
        self.statusLife = 20
        self.wordCreateLimit = 2

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
        self.labelBlockList = [Label(self.root, text='') for i in range(self.optionDiffCount[2])]

        # inputResponse will be called if the player hit <Return> key
        self.root.bind('<Return>', self.inputResponse)
        self.root.bind('<7>', self.inputResponseTest)

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
        if self.radioVar.get() == 1:    # Easy
            self.diffCount = self.optionDiffCount[0]
            self.diffTime = self.optionDiffTime[0]

        elif self.radioVar.get() == 2:  # Normal
            self.diffCount = self.optionDiffCount[1]
            self.diffTime = self.optionDiffTime[1]

        elif self.radioVar.get() == 3:  # Hard
            self.diffCount = self.optionDiffCount[2]
            self.diffTime = self.optionDiffTime[2]

        self.gameStart()    # difficulty selection is finished
        print("diffCount:", self.diffCount)
        print("diffTime:", self.diffTime)


    def gameStart(self):
        # remove all widgets for difficulty selection
        self.radioBtn1.destroy()
        self.radioBtn2.destroy()
        self.radioBtn3.destroy()
        self.diffBtn.destroy()
        self.diffLabel.destroy()

        # initialize the game
        self.statusGame = True
        self.labelScore.place(x=self.optionWidgetCoordinate[0], y=self.optionWidgetCoordinate[1])
        self.labelLife.place(x=self.optionWidgetCoordinate[2], y=self.optionWidgetCoordinate[3])
        self.labelLineTop.place(x=self.optionWidgetCoordinate[4], y=self.optionWidgetCoordinate[5])
        self.labelLineBot.place(x=self.optionWidgetCoordinate[6], y=self.optionWidgetCoordinate[7])
        self.inputEntry.place(x=self.optionWidgetCoordinate[8], y=self.optionWidgetCoordinate[9])
        


    def inputResponse(self, event):

        if self.statusGame == True:

            matchFound = acid_rain.gameEngine.inputResponse(self.diffCount, self.inputEntry.get()) # check the word
            self.inputEntry.delete(0, END)  # clear the text box

            if matchFound == True:
                self.statusScore += 1

                # find current dead block object and configure the widgets to renew the field
                for i in range(self.diffCount):
                    if acid_rain.gameEngine.wordBlockList[i].alive == True:
                        pass
                    else:
                        self.labelBlockList[i].configure(text=acid_rain.gameEngine.wordBlockList[i].name)
                        self.labelScore.configure(text=("Score: " + str(self.statusScore)))

            else:
                pass

        else:
            pass    # game is not started yet


    def inputResponseTest(self, event):

            self.loopFunction(self.diffCount)



    def inGame(self):
        pass


    def loopFunction(self, diffCount):
        ## deploy a new word block if we have not enough word blocks on the field
        # prevent the burst as using wordCreateLimit variable
        if len(acid_rain.gameEngine.blockNameList) < diffCount and self.wordCreateLimit == 2:

            self.wordCreateLimit = 0    # set the limit variable

            # find a dead block object and call the blockCreate function
            for i in range(diffCount):

                if acid_rain.gameEngine.wordBlockList[i].alive == True:
                    pass

                else:
                    acid_rain.gameEngine.wordBlockList[i].blockCreate(acid_rain.gameEngine) # calling the blockCreate function
                    self.labelBlockList[i].configure(text=acid_rain.gameEngine.wordBlockList[i].name)   # pass the name of the new block to widget
                    break   # if we find one, escape the loop
        

        # after two loop, we allow to deploy a new block
        if self.wordCreateLimit != 2:
            self.wordCreateLimit += 1
        

        ## active block moves
        for i in range(diffCount):

            if acid_rain.gameEngine.wordBlockList[i].alive == True:

                # if the player missed this block, call blockRemove function and subtract life
                if acid_rain.gameEngine.wordBlockList[i].coordinate[1] == 20:
                    acid_rain.gameEngine.wordBlockList[i].blockRemove(acid_rain.gameEngine)
                    self.labelBlockList[i].configure(text=acid_rain.gameEngine.wordBlockList[i].name)
                    self.statusLife -= 1

                else:
                    acid_rain.gameEngine.wordBlockList[i].coordinate[1] += 1    # adjust y-coordinate
                    self.labelBlockList[i].place(x=10 + acid_rain.gameEngine.wordBlockList[i].coordinate[0]*60,
                                                y=30 + acid_rain.gameEngine.wordBlockList[i].coordinate[1]*19)

            else:
                pass

        
        ## configure score and life
        self.labelScore.configure(text=("Score: " + str(self.statusScore)))
        self.labelLife.configure(text=("Life: " + str(self.statusLife)))


mainEngine = MainEngine()