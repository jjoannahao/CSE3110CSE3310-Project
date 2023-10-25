"""
title: Search and Sort Superheros
author: Joanna Hao
date: 2023-10-12
"""


### INPUT FUNCTIONS ###
def menu() -> int:
    """
    print start message and get superhero ID to retrieve
    :return: int
    """
    print("Welcome to the Superhero Search and Sort!")
    choice = input("""
Please choose how you would like to search superheros:
1. Superhero ID
2. Superhero Name
> """)
    if choice.isdigit() and 1 <= int(choice) <= 2:
        return int(choice)
    else:
        print("Please enter a number between 1 and 2!")
        return menu()


def getSuperheroID():
    """
    Get superhero ID to search from user
    :return:
    """
    superheroID = input("What is the Superhero ID? ")
    superheroID = reformatID(superheroID)  # reformat some IDs
    if checkID(superheroID):
        return superheroID.strip()
    else:
        print("Entry is invalid!\n")
        return getSuperheroID()


def getSuperheroName():
    """
    get superhero name to search from user
    :return:
    """
    superheroName = input("What is the Superhero Name? ")
    if checkName(superheroName.lower().strip()):
        return superheroName.strip()
    else:
        print("Entry invalid!")
        return getSuperheroName()


def rerun():
    """
    determine if user wants to continue running the program
    :return: bool
    """
    CHOICE = input("""
Would you like to continue playing? Press 'Y' to continue or anything else to exit.
> """)
    if CHOICE.upper().strip() in ('Y', "YES"):
        return True
    else:
        return False


### PROCESSING FUNCTIONS
def getRawData(fileName):
    import csv
    tempLi = []
    fil = open(fileName)
    text = csv.reader(fil)
    for line in text:
        tempLi.append(line)
    var = tempLi.pop(0)
    return tempLi, var


def cleanRawData(allData):
    """
    clean raw data by filling in empty boxes
    :param allData: 2D list (string)
    :return: 2D list (string)
    """
    for i in range(len(allData)):
        for j in range(len(allData[i])):
            if allData[i][j] == "":
                allData[i][j] = "Not available"


def sortIDs(LIST, FIRST_IDX, LAST_IDX):
    """
    use quicksort to sort IDs lexicographically
    :param LIST: 2D list - strings
    :param FIRST_IDX: int
    :param LAST_IDX: int
    :return: None
    """
    if FIRST_IDX < LAST_IDX:
        PIVOT_VALUE = LIST[FIRST_IDX][0]  # select 1st num as pivot

        LEFT_IDX = FIRST_IDX + 1
        RIGHT_IDX = LAST_IDX

        DONE = False
        while not DONE:
            while LEFT_IDX <= RIGHT_IDX and LIST[LEFT_IDX][0] <= PIVOT_VALUE:  # left hand bigger? hands crossed?
                LEFT_IDX += 1
            while RIGHT_IDX >= LEFT_IDX and LIST[RIGHT_IDX][0] >= PIVOT_VALUE:
                RIGHT_IDX -= 1

            if RIGHT_IDX < LEFT_IDX:  # if hands cross
                DONE = True  # found pivot spot
            else:
                LIST[LEFT_IDX], LIST[RIGHT_IDX] = LIST[RIGHT_IDX], LIST[LEFT_IDX]

        LIST[FIRST_IDX], LIST[RIGHT_IDX] = LIST[RIGHT_IDX], LIST[FIRST_IDX]

        sortIDs(LIST, FIRST_IDX, RIGHT_IDX - 1)  # sort left section
        sortIDs(LIST, RIGHT_IDX + 1, LAST_IDX)  # sort right section


def searchID(INDEX, VALUE):
    """
    searches for a value w/in a LIST using recursive linear search
    :param INDEX: int
    :param VALUE: string
    :return: int
    """
    global allSuperheroData
    if allSuperheroData[INDEX][0] == VALUE:
        print(f"{allSuperheroData[INDEX][0]} and {VALUE} compared")
        return INDEX
    elif INDEX > len(allSuperheroData) - 1:
        return -1
    else:
        return searchID(INDEX + 1, VALUE)


def sortNames(LIST, FIRST_IDX, LAST_IDX):
    """
    use quicksort to sort IDs lexicographically
    :param LIST: 2D list - strings
    :param FIRST_IDX: int
    :param LAST_IDX: int
    :return: None
    """
    if FIRST_IDX < LAST_IDX:
        PIVOT_VALUE = LIST[FIRST_IDX][1]  # select 1st num as pivot

        LEFT_IDX = FIRST_IDX + 1
        RIGHT_IDX = LAST_IDX

        DONE = False
        while not DONE:
            while LEFT_IDX <= RIGHT_IDX and LIST[LEFT_IDX][1] <= PIVOT_VALUE:  # left hand bigger? hands crossed?
                LEFT_IDX += 1
            while RIGHT_IDX >= LEFT_IDX and LIST[RIGHT_IDX][1] >= PIVOT_VALUE:
                RIGHT_IDX -= 1

            if RIGHT_IDX < LEFT_IDX:  # if hands cross
                DONE = True  # found pivot spot
            else:
                LIST[LEFT_IDX], LIST[RIGHT_IDX] = LIST[RIGHT_IDX], LIST[LEFT_IDX]

        LIST[FIRST_IDX], LIST[RIGHT_IDX] = LIST[RIGHT_IDX], LIST[FIRST_IDX]

        sortIDs(LIST, FIRST_IDX, RIGHT_IDX - 1)  # sort left section
        sortIDs(LIST, RIGHT_IDX + 1, LAST_IDX)  # sort right section


def searchName(INDEX, VALUE):
    """
    use recursive linear search to find superhero info by hero name
    :param INDEX: int
    :param VALUE: str
    :return: int
    """
    global allSuperheroData
    if allSuperheroData[INDEX][1].lower().strip() == VALUE.lower().strip():
        return INDEX
    elif INDEX > len(allSuperheroData) - 1:
        return -1
    else:
        return searchName(INDEX + 1, VALUE)


def retrieveSuperheroInfo(index):
    """
    retrieve relevant superhero details using index corresponding to superhero ID
    :param index: int
    :return: list - str
    """
    global allSuperheroData
    return allSuperheroData[index]


def checkID(ID):
    """
    check validity of superhero ID inputted
    :param ID: string
    :return: bool
    """
    global allSuperheroIDs
    valid = True
    if ID not in allSuperheroIDs:  # check ID existence in data
        valid = False
    return valid


def checkName(NAME):
    """
    check validity of superhero name from user
    :param NAME: str
    :return: bool
    """
    global allLowercaseSuperheroNames
    valid = True
    if NAME not in allLowercaseSuperheroNames:  # check name existence in all data
        valid = False
    return valid


def reformatID(ID):
    """
    make input ID format consistent w/ data format
    :param ID: string
    :return: string
    """
    ID_numbers = ID[1:]
    if ID_numbers.isdigit() and int(ID_numbers) < 1000:
        if len(ID_numbers) < 3:
            ID_numbers = list(ID_numbers)
            for i in range(3 - len(ID_numbers)):
                ID_numbers.insert(0, "0")
            ID_numbers = "".join(ID_numbers)
    newID = ID[0].upper() + ID_numbers
    # print(f"    new ID: {newID}") # checking purposes
    return newID  # either 3 numbers (OK) or more than 4 numbers --> won't exist


def compileSuperheros(allData):
    """
    combine all superhero IDs into a list and names into another list
    :param allData: 2D list - strings
    :return: x2 lists - string
    """
    heroIDs = []
    heroNames = []
    for i in range(len(allData)):
        heroIDs.append(allData[i][0])
        heroNames.append(allData[i][1].lower().strip())
    return heroIDs, heroNames


if __name__ == "__main__":
    # ----- MAIN PROGRAM CODE ----- #
    allSuperheroData, headers = getRawData('comicBookCharData_mixed.csv')
    allSuperheroIDs, allLowercaseSuperheroNames = compileSuperheros(allSuperheroData)
    PLAY_AGAIN = True
    FIRST_RUN = True

    while PLAY_AGAIN:
        if not FIRST_RUN:
            # --- input --- #
            PLAY_AGAIN = rerun()
        FIRST_RUN = False
        CHOICE = menu()
        if CHOICE == 1:
            SUPERHERO_ID = getSuperheroID()
        else:
            SUPERHERO_NAME = getSuperheroName()
        # --- processing --- #
        cleanRawData(allSuperheroData)
        if CHOICE == 1:
            sortIDs(allSuperheroData, 0, len(allSuperheroIDs) - 1)
            SUPERHERO_IDX = searchID(0, SUPERHERO_ID)
        else:
            sortNames(allSuperheroData, 0, len(allSuperheroIDs) - 1)
            SUPERHERO_IDX = searchName(0, SUPERHERO_NAME)

        if SUPERHERO_IDX == -1:  # if superhero doesn't exist
            continue
        else:  # if superhero found
            SUPERHERO_INFO = retrieveSuperheroInfo(SUPERHERO_IDX)

            # --- output --- #
            print(f"""
Superhero ID: {SUPERHERO_INFO[0]}
Name: {SUPERHERO_INFO[1]}
ID: {SUPERHERO_INFO[2]}
Align: {SUPERHERO_INFO[3]}
Eye: {SUPERHERO_INFO[4]}
Hair: {SUPERHERO_INFO[5]}
Alive: {SUPERHERO_INFO[6]}
Appearances: {SUPERHERO_INFO[7]}
First-Appearance: {SUPERHERO_INFO[8]}
Year: {SUPERHERO_INFO[9]}
Brand: {SUPERHERO_INFO[10]}
            """)
