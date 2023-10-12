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
    sort all superhero data lexicographically by superhero ID using
    :param allData: 2D list (string)
    :return:
    """
    for i in range(1, len(allData)):  # start at 2nd elem --> front is sorted
        IDX_VALUE = allData[i]
        SORTED_IDX = i - 1  # end of sorted values
        while SORTED_IDX >= 0 and IDX_VALUE < allData[SORTED_IDX]:  # while not at front of list and current value <
            allData[SORTED_IDX + 1] = allData[SORTED_IDX]
            SORTED_IDX -= 1
        allData[SORTED_IDX + 1] = IDX_VALUE


rawArr, headers = getRawData('comicBookCharData_mixed.csv')
# rawArr is a 2D arrays holding all the Superhero data
# headers is a variable that holds the List of all the column headers.

print(headers)
print(rawArr[0])  # 708 characters, 11 characteristics associated w/ each
cleanRawData(rawArr)
# print(rawArr[2])  # checking cleaning

