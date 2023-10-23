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


def retrieveSuperheroInfo(index):
    """
    retrieve relevant superhero details using index corresponding to superhero ID
    :param index: int
    :return: list - str
    """
    global allSuperheroData
    return allSuperheroData[index]


def menu() -> str:
    """
    print start message and get superhero ID to retrieve
    :return: string
    """
    print("Welcome to the Superhero Search and Sort!")
    superheroID = input("What is the Superhero ID? ")
    superheroID = reformatID(superheroID)  # reformat some IDs
    if checkID(superheroID):
        return superheroID
    else:
        print("Entry is invalid!\n")
        return menu()


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


def compileIDs(allData):
    """
    combine all superhero IDs into 1 list
    :param allData: 2D list - strings
    :return: list - string
    """
    heroIDs = []
    for i in range(len(allData)):
        heroIDs.append(allData[i][0])
    return heroIDs


if __name__ == "__main__":
    # ----- MAIN PROGRAM CODE ----- #
    allSuperheroData, headers = getRawData('comicBookCharData_mixed.csv')
    print(headers)
    allSuperheroIDs = compileIDs(allSuperheroData)
    playAgain = True

    while playAgain:
        # --- input --- #
        superheroID = menu()

        # --- processing --- #
        cleanRawData(allSuperheroData)
        sortIDs(allSuperheroData)
        SUPERHERO_IDX = searchID(superheroID)
        if SUPERHERO_IDX == -1:
            continue
        else:
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
