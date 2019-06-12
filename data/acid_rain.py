import random, os
from random import randint


class GameEngine(object):

    def __init__(self):
        # initialize some engine variables
        self.blockNameList = []
        self.wordList = []

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
        

    def wordBlockCreate(self):
        pass
            

    def wordBlockRemove(self, word):
        pass


class wordBlock(object):
    
    def __init__(self):
        self.name = ''
        self.alive = False
        self.coordinate = [0, 0]
    
    def blockCreate(self, GameEngine):
        # pass random name for this block and remove it from the word list
        wordList = GameEngine.wordList  # bind a word list from the object of GameEngine
        self.name = wordList.pop(random.randrange(len(wordList)))

        # put this block in play
        self.coordinate[0] = randint(0, 9)
        self.alive = True

        # add this block to blockNameList
        (GameEngine.blockNameList).append(self.name)




test = GameEngine()
test.wordListGenerate()
test2 = wordBlock()
test2.blockCreate(test)
print(test2.coordinate)
print(test2.name)
print(test.blockNameList)