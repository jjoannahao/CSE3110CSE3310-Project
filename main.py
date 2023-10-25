"""
title: Search and Sort Superheros
author: Joanna Hao
date: 2023-10-12
"""


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


def sortIDs(allData):
    """
    sort all superhero data lexicographically by superhero ID using iterative selection sort
    :param allData: unsorted list - string
    :return: None
    """
    for i in range(len(allData) - 1):  # stop at 2nd last val  # i = idx of value to be sorted/placed
        MIN_IDX = i
        for j in range(i + 1, len(allData)):  # all elems in unsorted section
            if allData[j][0] < allData[MIN_IDX][0]:
                MIN_IDX = j
        if allData[MIN_IDX][0] < allData[i][0]:
            allData[i], allData[MIN_IDX] = allData[MIN_IDX], allData[i]


def searchID(ID):
    """
    search for index of superhero info based on ID using ITERATIVE binary search
    :param ID: str
    :return: int
    """
    global allSuperheroData
    START_IDX = 0
    END_IDX = len(allSuperheroData) - 1

    while (START_IDX <= END_IDX):  # normal stopping point for binary search
        MIDPOINT_IDX = (START_IDX + END_IDX) // 2
        if allSuperheroData[MIDPOINT_IDX][0] == ID:
            return MIDPOINT_IDX
        elif allSuperheroData[MIDPOINT_IDX][0] < ID:
            START_IDX = MIDPOINT_IDX + 1
        else:
            END_IDX = MIDPOINT_IDX - 1
    return -1


def sortNames(allData):
    """
    sort data lexicographically by superhero names
    :param allData: unsorted list - string
    :return: None
    """
    for i in range(len(allData) - 1):  # stop at 2nd last val  # i = idx of value to be sorted/placed
        MIN_IDX = i
        for j in range(i + 1, len(allData)):  # all elems in unsorted section
            if allData[j][1] < allData[MIN_IDX][1]:
                MIN_IDX = j
        if allData[MIN_IDX][1] < allData[i][1]:
            allData[i], allData[MIN_IDX] = allData[MIN_IDX], allData[i]


def searchName(NAME):
    """
    search for index of superhero info based on ID using ITERATIVE binary search
    :param NAME: str
    :return: int
    """
    global allSuperheroData
    START_IDX = 0
    END_IDX = len(allSuperheroData) - 1

    while (START_IDX <= END_IDX):  # normal stopping point for binary search
        MIDPOINT_IDX = (START_IDX + END_IDX) // 2
        if allSuperheroData[MIDPOINT_IDX][1].lower().strip() == NAME.lower().strip():
            return MIDPOINT_IDX
        elif allSuperheroData[MIDPOINT_IDX][1].lower().strip() < NAME.lower().strip():
            START_IDX = MIDPOINT_IDX + 1
        else:
            END_IDX = MIDPOINT_IDX - 1
    return -1


def retrieveSuperheroInfo(index):
    """
    retrieve relevant superhero details using index corresponding to superhero ID
    :param index: int
    :return: list - str
    """
    global allSuperheroData
    return allSuperheroData[index]


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
        return superheroID
    else:
        print("Entry is invalid!\n")
        return menu()


def getSuperheroName():
    """
    get superhero name to search from user
    :return:
    """
    superheroName = input("What is the Superhero Name? ")
    if checkName(superheroName):
        return superheroName.strip()
    else:
        print("Entry invalid!")
        return getSuperheroName()


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
    # print(headers)
    allSuperheroIDs, allLowercaseSuperheroNames = compileSuperheros(allSuperheroData)
    playAgain = True

    while playAgain:
        # --- input --- #
        choice = menu()
        if choice == 1:
            superheroID = getSuperheroID()
        else:
            superheroName = getSuperheroName()

        # --- processing --- #
        cleanRawData(allSuperheroData)

        if choice == 1:  # user searching by hero ID
            sortIDs(allSuperheroData)
            SUPERHERO_IDX = searchID(superheroID)
        else:  # user searching by hero name
            sortNames(allSuperheroData)
            SUPERHERO_IDX = searchName(superheroName)

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
