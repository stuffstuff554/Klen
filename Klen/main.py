# Version

Klen_Version = "Alpha 0.0"

# Imports starting modules

import os

import sys

# Warns the user of PyGame requirement

os.system("msg * Please enter the prompt in the console.")

while True:
    print("Do you have PyGame? Y/N")
    print()
    Awnser = input(">")
    if Awnser == "Y":
        print("Ok!")
        break
    elif Awnser == "N":
        print("Attempting installment.")
        os.system("pip install pygame")
        print("Check logs for sucsess.")
        print("Hit enter to close the application. (Requires restart of application)")
        input(">")
        sys.exit()
    else:
        print("incorrect awnser")

# PyGame

import pygame

class KlenClass:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption("Klen ", Klen_Version)
    def KlenGame(self):
        print("Main init started")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

# Run Game

if __name__ == "__main__":
    GameClassInit = KlenClass()
    GameClassInit.KlenGame()