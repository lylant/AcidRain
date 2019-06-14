import random, os
from random import randint


class GameEngine(object):

    def __init__(self):
        # initialize some engine variables and generate wordList
        self.blockNameList = []
        self.wordList = []
        self.wordListGenerate()


    def wordListGenerate(self):
        # set a directory for the resource file
        pathCurrentDir = os.path.dirname(__file__)  # current script directory
        pathRelDir = "../resource/words.txt"
        pathAbsDir = os.path.join(pathCurrentDir, pathRelDir)

        listFile = open(pathAbsDir, encoding="utf-8")
        self.wordList = []

        # read line by line with readlines(), 'word' temporarily save the string
        # then saved string is appended in the list 'wordList'
        for word in listFile.readlines():
            self.wordList.append(word.strip())
                # .strip() will remove any character with passed argument
                # nothing is passed so whitespace will removed (default)
        
    def inputResponse(self, inputWord):
        print(inputWord)


class wordBlock(object):
    
    def __init__(self):
        # initialize parameters
        self.name = ''
        self.alive = False
        self.coordinate = [0, 0]
    

    def blockCreate(self, GameEngine):
        # pass random name for this block and remove it from the word list
        self.name = (GameEngine.wordList).pop(random.randrange(len(GameEngine.wordList)))

        # put this block in play
        self.coordinate[0] = randint(0, 9)
        self.alive = True

        # add this block to blockNameList
        (GameEngine.blockNameList).append(self.name)


    def blockRemove(self, GameEngine):
        # remove from blockNameList and revive it in wordList
        (GameEngine.wordList).append(self.name)
        (GameEngine.blockNameList).remove(self.name)

        # reinitialize parameters
        self.coordinate = [0, 0]
        self.alive = False
        self.name = ''


game = GameEngine()