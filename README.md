# Acid Rain

# Introduction

## Project Backgrounds
This project aims to practice building a simple typing game using Python.

* **Acid Rain Storm:** The massive storm is coming your land. Some Hydrochloric acid clouds are brewed in the storm somehow, the storm becomes a catastrophic disaster. This acid rain storm could completely destroy the whole land including your base.
* **Defend the Base:** You are the site administrator of a secret research base. The base stores immense unstable radioactive elements, which can make the region sterile for decades. You must defend the base from the acid rain.
* **Destroy the Rain:** Recently the laboratory researched a new CIWS which allows you to destroy the rain blocks. Each rain block contains a random English word, you can destroy the rain block by typing the word in it.


## Main Tech-Stacks for the Project
* Python


# Installation

## Required Packages
Following packages are required to install the game. Please prepare following packages installed on your machine before the installation. Most recent stable version is recommended. `Tkinter` can be installed using `pip`.

* Python 3
* Tkinter

## Installation
As the product is not using any game framework or engine, the installation process is simple copy and paste.

1. Create a directory for the game.
2. Copy the product into the new directory.

## Game Option
Several options can be updated by manipulating `resource/options.txt`. Available options are including block limits in the screen, block drop speed and position of several user interfaces. List of options are below:

```
DiffCountEasy: __
DiffCountNorm: __
DiffCountHard: __
DiffTimeEasy: ___
DiffTimeNorm: ___
DiffTimeHard: ___
UILabelScoreX: ___
UILabelScoreY: ___
UILabelLifeX: ___
UILabelLifeY: ___
UILabelLineTopX: ___
UILabelLineTopY: ___
UILabelLineBotX: ___
UILabelLineBotY: ___
UIinputTxtBoxX: ___
UIinputTxtBoxY: ___
```

## Word Pool
Words in each dropping rain blocks are randomly selected from the word pool. The word pool is located as `resource/words.txt`. To add word to the pool, you can simply add desired word in the file.