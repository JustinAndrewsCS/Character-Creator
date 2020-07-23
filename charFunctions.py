import pygame
import mysql.connector
import random

"""
Character Creator Application
CS317 Final Project
By Justin Andrews, Matthieu Privat

File Description:
This file contains the functions that are called by the main file of the project.
These functions are used to create the display to the user.
These functions also execute the sql commands to create the game functionality.

Function Declarations:
    createCharButton(screen)
    viewCharButton(screen)
    deleteCharButton(screen)
    updateCharButton(screen)
    gameTitleText(screen)
    printChar(charInfo)
    viewChar()
    createChar()
    checkCharID(charID)
    printBasicInfo(charInfo)
    getBasicInfo()
    deleteChar()
    updateChar()
"""


# connect to database with ip address, username, password, the database, and the authorization method of the password
db = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="characters",
    auth_plugin='mysql_native_password'
)

# create cursor that is used to execute sql statements
mycursor = db.cursor()

# -----------------------------------------------


def createCharButton(screen):
    """
    This function creates the text box/button to create a new character.

    :param screen: the screen to display the text box to
    :return: no return, this function is purely visual
    """

    # format the text font and font size
    textFormat = pygame.font.SysFont("arial", size=32)

    # create the text
    text = textFormat.render("Click here to Create a New Character", True, (0, 0, 0))

    # display the text
    screen.blit(text, (80, 100))


# -----------------------------------------------


def viewCharButton(screen):
    """
    This function creates the text box/button to view characters in the database.

    :param screen: the screen to display the text box to
    :return: no return, this function is purely visual
    """

    # format the text font and font size
    textFormat = pygame.font.SysFont("arial", size=32)

    # create the text
    text = textFormat.render("Click here to View All Characters", True, (0, 0, 0))

    # display the text
    screen.blit(text, (100, 250))


# -----------------------------------------------


def deleteCharButton(screen):
    """
    This function creates the text box/button to delete a character.

    :param screen: the screen to display the text box to
    :return: no return, this function is purely visual
    """

    # format the text font and font size
    textFormat = pygame.font.SysFont("arial", size=32)

    # create the text
    text = textFormat.render("Click here to Delete A Character", True, (0, 0, 0))

    # display the text
    screen.blit(text, (105, 400))


# -----------------------------------------------


def updateCharButton(screen):
    """
    This function creates the text box/button to update a character.

    :param screen: the screen to display the text box to
    :return: no return, this function is purely visual
    """

    # format the text font and font size
    textFormat = pygame.font.SysFont("arial", size=32)

    # create the text
    text = textFormat.render("Click here to Update a Character's Stats", True, (0, 0, 0))

    # display the text
    screen.blit(text, (65, 550))


# -----------------------------------------------


def gameTitleText(screen):
    """
    This function displays the game title text on the screen.

    :param screen: the screen to display the text box to
    :return: no return, this function is purely visual
    """

    # format the text font, bold, and font size
    textFormat = pygame.font.SysFont("arial", bold=True, size=40)

    # create the text
    text = textFormat.render("Character Creator Interface", True, (0, 0, 0))

    # display the text
    screen.blit(text, (85, 700))


# -----------------------------------------------


def printChar(charInfo):
    """
    This function if called by viewChar and prints out all character information for the given character.

    :param charInfo: the information related to a character
    :return: this function has no returns but prints out the information
    """

    # print all character info for the specified character
    print("Character's Name: ", charInfo[2])
    print("Class:            ", charInfo[1])
    print("Sex:              ", charInfo[3])
    print("Strength:         ", charInfo[4])
    print("Dexterity:        ", charInfo[5])
    print("Constitution:     ", charInfo[6])
    print("Intelligence:     ", charInfo[7])
    print("Wisdom:           ", charInfo[8])
    print("Charisma:         ", charInfo[9])
    print("Treat Injury:     ", charInfo[10])
    print("Computer Use:     ", charInfo[11])
    print("Demolitions:      ", charInfo[12])
    print("Stealth:          ", charInfo[13])
    print("Awareness:        ", charInfo[14])
    print("Persuasion:       ", charInfo[15])
    print("Repair:           ", charInfo[16])
    print("Security:         ", charInfo[17])
    print("gameID:           ", charInfo[18])
    print("charID:           ", charInfo[0])

    # print for spacing
    print()


# -----------------------------------------------


def viewChar():
    """
    This function iterates through all characters in the database and prints their information using
    the printChar(charInfo) function.

    :return: this function has no return but prints out the character info through the printChar(charInfo) function
    """

    # execute a select all entries from characters command on the database
    mycursor.execute("SELECT * FROM characters")

    # fetch the results of that command
    result = mycursor.fetchall()

    print("\nPrinting list of characters:")

    # for each of the results returned, i is a list of the character information
    for i in result:

        # print the character info for the current character
        printChar(i)

    print("End of list of characters\n")


# -----------------------------------------------


def createChar():
    """
    This function creates a new character to be inserted into the database and prompts the user to enter the
    required information about the character.

    :return: there is no return, only print statements and a sql insert into the database upon successful creation
    """

    # generate a random character id to act as the key, int value between 1000 and 9999
    charID = int(random.randint(1000, 9999))

    # check that the generated key is not already in use, if so assign a new character id
    charID = checkCharID(charID)

    # input character's name, class, and sex
    name = input("Enter the character's name (no more than 30 characters): ")
    charClass = input("Enter the character's class (no more than 12 characters): ")
    sex = input("Enter the character's sex (no more than 10 characters: ")

    # if input is not an int then the program will give an error
    print("\nAll skill values must be an INTEGER!")

    # input the character's skills, must be int values
    strength = int(input("Enter the character's strength: "))
    dexterity = int(input("Enter the character's dexterity: "))
    constitution = int(input("Enter the character's constitution: "))
    intelligence = int(input("Enter the character's intelligence: "))
    wisdom = int(input("Enter the character's wisdom: "))
    charisma = int(input("Enter the character's charisma: "))
    treatInjury = int(input("Enter the character's treat injury skill: "))
    computerUse = int(input("Enter the character's computer use skill: "))
    demolitions = int(input("Enter the character's demolitions skill: "))
    stealth = int(input("Enter the character's stealth: "))
    awareness = int(input("Enter the character's awareness: "))
    persuade = int(input("Enter the character's persuasion skill: "))
    repair = int(input("Enter the character's repair skill: "))
    security = int(input("Enter the character's security skill: "))

    # game id equals 0, only 1 game
    gameID = 1000

    # if name, class, and sex are valid string lengths
    if len(name) <= 30 and len(charClass) <= 12 and len(sex) <= 10:

        # the sql query to be executed
        query = "INSERT INTO characters (" \
                "charID, " \
                "class, " \
                "charName, " \
                "sex, " \
                "strength, " \
                "dexterity, " \
                "constitution, " \
                "intelligence," \
                "wisdom, " \
                "charisma, " \
                "treatInjury, " \
                "computerUse, " \
                "demolitions, " \
                "stealth, " \
                "awareness, " \
                "persuade, " \
                "repairSkill," \
                "securitySkill, " \
                "gameID) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # the information to be inserted
        char = (charID, charClass, name, sex, strength, dexterity, constitution, intelligence, wisdom, charisma,
                treatInjury, computerUse, demolitions, stealth, awareness, persuade, repair, security, gameID)

        # execute sql command with sql query and character information
        mycursor.execute(query, char)

        # commit the insertion into the database
        db.commit()

        # print number of new rows and print to confirm insertion worked
        print(mycursor.rowcount, "new character created")

    # if the user inputted strings with an invalid length
    else:
        print("Invalid Entries. Character creation canceled.")


# -----------------------------------------------


def checkCharID(charID):
    """
    This function checks if the random generated character ID is unique and does not collide with another ID.
    If it does collide it generates a new ID.

    :param charID: the generated character ID
    :return charID: returns either the original charID or a new one that does not collide
    """

    # select charIDs in use in the database
    mycursor.execute("SELECT charID FROM characters")

    # fetch the results from the sql command
    result = mycursor.fetchall()

    # charID is valid
    valid = True

    # for each entry of the results
    for i in result:

        # if the generated charID is already in use
        if charID == i:

            # then charID is not valid
            valid = False

    # if charID is not valid
    if not valid:

        # generate new charID between 1000 and 9999
        charID = random.randint(1000, 9999)

    # return the charID that should now be valid/confirmed to be valid
    return charID


# -----------------------------------------------


def printBasicInfo(charInfo):
    """
    This function prints basic character info when the delete or update function is called.
    The function prints the name, class, sex, and charID of the characters so that the user can properly enter the
    correct character ID to identify the character they wish to interact with.

    :param charInfo: the character information
    :return: no returns but does print out information about the character
    """

    # print for spacing and cleanness
    print("--------------------")

    # print basic character info to give context when deleting or updating a character
    print("Name: ", charInfo[2])
    print("Class: ", charInfo[1])
    print("Sex: ", charInfo[3])
    print("Character ID: ", charInfo[0])

    # print for spacing and cleanness
    print("--------------------")


# -----------------------------------------------


def getBasicInfo():
    """
    This function selects the basic information about the character to be printed when delete or update is called.

    :return: no returns but does call the function to print out the information
    """

    # execute a select entries from characters command on the database
    mycursor.execute("SELECT charID, class, charName, sex FROM characters")

    # fetch the results of that command
    result = mycursor.fetchall()

    print("\nCharacters:")

    # for each of the results returned, i is a list of the character information
    for i in result:

        # print the character basic character info for the current character
        printBasicInfo(i)


# -----------------------------------------------


def deleteChar():
    """
    This function deletes the selected character from the database.
    If an invalid character ID is entered nothing will be deleted.

    :return: no return but does delete a character entry from the database
    """

    # print short list of characters to show basic info and character IDs
    getBasicInfo()

    # Prompt
    print("\nTime to delete a character >:D")

    # Create variable of Character ID we want to remove
    toDelete = int(
        input("Please enter the ID number of the character you wish to erase (this operation can't be undone!): "))

    # Create MySQL command line
    sql = "DELETE FROM Characters WHERE charID = %s"

    # Execute MySQL command using the CharID we defined
    mycursor.execute(sql, (toDelete,))
    db.commit()

    # Confirm how many things we removed
    print(mycursor.rowcount, "character record deleted")


# -----------------------------------------------


def updateChar():
    """
    This function updates the skills and attributes of the selected character.
    If an invalid character ID is inputted then nothing will be updated.

    :return: no returns but does update attributes related to the selected character in the database
    """

    # get basic information about the characters and print it
    getBasicInfo()

    # Prompt the user
    print("\nSo you have levelled up? You must have some new skills and attributes!")
    print("Let's update your character's abilities, to reflect your new level...")
    toUpdate = int(input("What character do you wish to update? Enter their character ID: "))

    # Update all of the character's skills upon levelling up
    strUpdate = int(input("Enter the character's new strength: "))
    dexUpdate = int(input("Enter the character's new dexterity: "))
    conUpdate = int(input("Enter the character's new constitution: "))
    intUpdate = int(input("Enter the character's new intelligence: "))
    wisUpdate = int(input("Enter the character's new wisdom: "))
    chaUpdate = int(input("Enter the character's new charisma: "))
    treatInjuryUpdate = int(input("Enter the character's new treat injury skill: "))
    computerUseUpdate = int(input("Enter the character's new computer use skill: "))
    demolitionsUpdate = int(input("Enter the character's new demolitions skill: "))
    stealthUpdate = int(input("Enter the character's new stealth: "))
    awarenessUpdate = int(input("Enter the character's new awareness: "))
    persuadeUpdate = int(input("Enter the character's new persuasion skill: "))
    repairUpdate = int(input("Enter the character's new repair skill: "))
    securityUpdate = int(input("Enter the character's new security skill: "))

    # Create MySQL Commands
    strSQL = "UPDATE Characters SET strength = %s WHERE charID = %s"
    dexSQL = "UPDATE Characters SET dexterity = %s WHERE charID = %s"
    conSQL = "UPDATE Characters SET constitution = %s WHERE charID = %s"
    intSQL = "UPDATE Characters SET intelligence = %s WHERE charID = %s"
    wisSQL = "UPDATE Characters SET wisdom = %s WHERE charID = %s"
    chaSQL = "UPDATE Characters SET charisma = %s WHERE charID = %s"
    treatInjurySQL = "UPDATE Characters SET treatInjury = %s WHERE charID = %s"
    computerUseSQL = "UPDATE Characters SET ComputerUse = %s WHERE charID = %s"
    demolitionsSQL = "UPDATE Characters SET demolitions = %s WHERE charID = %s"
    stealthSQL = "UPDATE Characters SET stealth = %s WHERE charID = %s"
    awarenessSQL = "UPDATE Characters SET awareness = %s WHERE charID = %s"
    persuadeSQL = "UPDATE Characters SET persuade = %s WHERE charID = %s"
    repairSQL = "UPDATE Characters SET repairSkill = %s WHERE charID = %s"
    securitySQL = "UPDATE Characters SET securitySkill = %s WHERE charID = %s"

    # Execute MySQL Commands
    mycursor.execute(strSQL, (strUpdate, toUpdate))
    mycursor.execute(dexSQL, (dexUpdate, toUpdate))
    mycursor.execute(conSQL, (conUpdate, toUpdate))
    mycursor.execute(intSQL, (intUpdate, toUpdate))
    mycursor.execute(wisSQL, (wisUpdate, toUpdate))
    mycursor.execute(chaSQL, (chaUpdate, toUpdate))
    mycursor.execute(treatInjurySQL, (treatInjuryUpdate, toUpdate))
    mycursor.execute(computerUseSQL, (computerUseUpdate, toUpdate))
    mycursor.execute(demolitionsSQL, (demolitionsUpdate, toUpdate))
    mycursor.execute(stealthSQL, (stealthUpdate, toUpdate))
    mycursor.execute(awarenessSQL, (awarenessUpdate, toUpdate))
    mycursor.execute(persuadeSQL, (persuadeUpdate, toUpdate))
    mycursor.execute(repairSQL, (repairUpdate, toUpdate))
    mycursor.execute(securitySQL, (securityUpdate, toUpdate))

    # commit the changes to the database
    db.commit()

    # confirm that a record was updated
    print(mycursor.rowcount, "character record updated")
