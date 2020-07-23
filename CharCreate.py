import pygame
import charFunctions

"""
Character Creator Application
CS317 Final Project
By Justin Andrews, Matthieu Privat

File Description:
This is the main file that is executed to run the Character Creator Application.
This file initiates pygame, creates the GUI, and handles functionality of the application by calling
functions from charFunctions.py.
"""


# -----------------------------------------------

# initialize pygame
pygame.init()

# print for spacing
print()

# create screen and set screen size
screen = pygame.display.set_mode((600, 900))

# title the pygame window
pygame.display.set_caption("Character Creator Interface")

# -----------------------------------------------

# LOOP TO RUN APPLICATION

# while running is true the game runs
running = True

print("\nApplication is running\n")

# while application is not quit
while running:

    # set screen background color
    screen.fill((128, 128, 128))

    # CREATE BUTTONS
    # add the create character button/textbox to the screen
    charFunctions.createCharButton(screen)

    # add the view characters button/textbox to the screen
    charFunctions.viewCharButton(screen)

    # add the delete character button/textbox to the screen
    charFunctions.deleteCharButton(screen)

    # add the update character button/textbox to the screen
    charFunctions.updateCharButton(screen)

    # add the game title to the screen
    charFunctions.gameTitleText(screen)
    # END CREATE BUTTONS

    # catch event
    for event in pygame.event.get():

        # if event is user exiting the application
        if event.type == pygame.QUIT:
            # end the application
            print("Application is closing...")
            running = False
        # END IF USER QUITS

        # if user clicks the screen
        if event.type == pygame.MOUSEBUTTONDOWN:

            # get location of click
            xPos, yPos = pygame.mouse.get_pos()

            # if the user clicks on the view character text box
            if 92 < xPos < 493 and 250 < yPos < 286:
                # print out all characters in the database
                charFunctions.viewChar()

            # END IF USER CLICKS TO VIEW CHARACTERS

            # if user clicks on the create character text box
            if 71 < xPos < 527 and 98 < yPos < 135:
                # start create character process through prints and inputs
                charFunctions.createChar()

            # END IF USER CLICKS TO CREATE NEW CHARACTER

            # if user clicks on the delete character text box
            if 98 < xPos < 491 and 402 < yPos < 439:
                # delete character from the database
                charFunctions.deleteChar()

            # END IF USER CLICKS TO DELETE CHARACTER

            # if user clicks on the update character text box
            if 58 < xPos < 547 and 547 < yPos < 594:
                # update character from the database
                charFunctions.updateChar()

            # END IF USER CLICKS TO UPDATE CHARACTER

        # END IF USER CLICKS

    # update the screen every tick
    pygame.display.update()
