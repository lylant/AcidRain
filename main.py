from tkinter import Tk
from data import acid_rain


class mainEngine(object):

    def wordsListGenerate(self):
        listFile = open("resource/words.txt", encoding="utf-8")
        listGenerated = []

        # read line by line with readlines(), 'word' temporarily save the string
        # then saved string is appended in the list 'wordsList'
        for word in listFile.readlines():
            listGenerated.append(word.strip())
                # .strip() will remove any character with passed argument
                # nothing is passed so whitespace will removed (default)
        
        return listGenerated


# construct a tkinter window
root = Tk()
root.title("Acid Rain")
root.geometry("640x480")
root.resizable(0,0)