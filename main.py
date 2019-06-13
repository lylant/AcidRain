from tkinter import Tk, Label, Button, Radiobutton, IntVar
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
        self.diffCount = 80


    def gameInitialize(self):
        ## Difficulty Selection
        diffLabel = Label(self.root, text="Select the difficulty.")

        # difficulty select options with radiobuttons
        # function difficultySelection will be called if the player hit the diffBtn
        radioBtn1 = Radiobutton(text="Easy", variable=self.radioVar, value=1)
        radioBtn2 = Radiobutton(text="Normal", variable=self.radioVar, value=2)
        radioBtn3 = Radiobutton(text="Hard", variable=self.radioVar, value=3)
        diffBtn = Button(self.root, text="Select", command=self.difficultySelection, width=5, height=1)

        # packing up and show all widgets
        diffLabel.pack()
        radioBtn1.pack()
        radioBtn2.pack()
        radioBtn3.pack()
        diffBtn.pack()

        # execute the game
        self.root.mainloop()

    
    def difficultySelection(self):
        ## get option parameters from an external option file
        # set a directory for the resource file
        pathCurrentDir = os.path.dirname(__file__)  # current script directory
        pathRelDir = "resource/options.txt"
        pathAbsDir = os.path.join(pathCurrentDir, pathRelDir)
        optionFile = open(pathAbsDir, encoding="utf-8")

        optionDifficulty = [] # a list for difficulty parameters got from the option file

        # find the difficulty count parameters and bind to optionDifficulty
        # these will bind the important parameter only as integer by using slicing
        for optionLine in optionFile.readlines():
            if "DiffCountEasy" in optionLine:
                optionDifficulty.append(int(optionLine[14:-1]))
            elif "DiffCountNorm" in optionLine:
                optionDifficulty.append(int(optionLine[14:-1]))
            elif "DiffCountHard" in optionLine:
                optionDifficulty.append(int(optionLine[14:-1]))        


        if self.radioVar.get() == 1:
            self.diffCount = optionDifficulty[0]

        elif self.radioVar.get() == 2:
            self.diffCount = optionDifficulty[1]

        elif self.radioVar.get() == 3:
            self.diffCount = optionDifficulty[2]

        
        print(self.diffCount)
        self.gameStart()


    def gameStart(self):
        pass


test3 = MainEngine()
test3.gameInitialize()