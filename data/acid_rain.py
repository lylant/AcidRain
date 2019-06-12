import random
import os

class GameEngine(object):

    def __init__(self):
        # initialize some engine variables
        pass

    def wordListGenerate(self):
        # set a directory for the resource file
        pathCurrentDir = os.path.dirname(__file__)  # current script directory
        pathRelDir = "../resource/words.txt"
        pathAbsDir = os.path.join(pathCurrentDir, pathRelDir)

        listFile = open(pathAbsDir, encoding="utf-8")
        listGenerated = []

        # read line by line with readlines(), 'word' temporarily save the string
        # then saved string is appended in the list 'wordsList'
        for word in listFile.readlines():
            listGenerated.append(word.strip())
                # .strip() will remove any character with passed argument
                # nothing is passed so whitespace will removed (default)
        
        return listGenerated
        

    def wordBlockCreate(self, count):
        pass

    def wordBlockRemove(self, word):
        pass


test = GameEngine()
test.wordListGenerate()