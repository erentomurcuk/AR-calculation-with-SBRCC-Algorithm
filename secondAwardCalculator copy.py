# Second calculation method of scoring

import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

#) list name # name in .csv file
herdSizeList = [] # herd_size
organicList = [] # organic
amoxResList = [] # amoxR
poultryList = [] # poultry
wasteMilkList = [] # anything_waste
weanList = [] # wean

def showGraph(xValues, yValues, xLabel, yLabel, title):
    plt.bar(xValues, yValues)

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)

    plt.xlim(0)
    plt.show()

def showAxis(numbers):
    x = range(len(numbers))

    plt.plot(x, numbers, marker='o', linestyle='-', color='blue')

    plt.xlabel('Index')
    plt.ylabel('Numbers')
    plt.title('List of Numbers')

    plt.xticks(x, x)  # Show x-axis ticks as the index values
    plt.ylim(0)  # Set x-axis limits

    plt.show()

def getScores(charList, resistantList, charNames):
    scores = {}
    zippedList = [value for value, condition in zip(charList, resistantList) if condition]

    sortedCharCounter = dict(sorted(Counter(zippedList).items(), key=lambda item: item[0]))
    sortedResCounter = dict(sorted(Counter(charList).items(), key=lambda item: item[0]))

    for i in zip(sortedCharCounter.values(), sortedResCounter.values(), charNames):
        result = i[0] / i[1] * 100

        print(f"{i[2]}: {result}")
        scores[i[2]] = result

    return scores


with open('dairy_farms_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip the header row
    headerRow = next(reader)
    
    for row in reader:
        herdSize = row[headerRow.index("herd_size")]
        amoxValue = row[headerRow.index("amoxR")]
        organicValue = row[headerRow.index("organic")]
        poultryValues = row[headerRow.index("poultry")]
        wasteMilkValue = row[headerRow.index("anything_waste")]
        weanValue = row[headerRow.index("wean")]

        herdSizeList.append(int(herdSize))
        organicList.append(int(organicValue))
        amoxResList.append(True if amoxValue == '1' else False)
        poultryList.append(int(poultryValues))
        wasteMilkList.append(int(wasteMilkValue))
        weanList.append(int(weanValue))

microDatabase = {
    "Amoxycillin Resistance": amoxResList,
    "Herd Size": herdSizeList,
    "Organic": organicList,
    "Poultry": poultryList,
    "Waste Milk": wasteMilkList,
    "Wean": weanList,
    "Scores": []
}

organicNames = [0, 1]
herdSizeNames = [1, 2, 3]
poultryNames = [0, 1]
wasteMilkNames = [0, 1]
weanNames = [1, 2, 3]

organicScores = getScores(organicList, amoxResList, organicNames)
print()
herdSizeScores = getScores(herdSizeList, amoxResList, herdSizeNames)
print()
poultryScores = getScores(poultryList, amoxResList, poultryNames)
wasteMilkScores = getScores(wasteMilkList, amoxResList, wasteMilkNames)
weanScores = getScores(weanList, amoxResList, weanNames)

for i in range(len(amoxResList)):
    microDatabase["Scores"].append(organicScores[microDatabase["Organic"][i]])
    microDatabase["Scores"][i] += herdSizeScores[microDatabase["Herd Size"][i]]
    microDatabase["Scores"][i] += poultryScores[microDatabase["Poultry"][i]]
    microDatabase["Scores"][i] += wasteMilkScores[microDatabase["Waste Milk"][i]]
    microDatabase["Scores"][i] += weanScores[microDatabase["Wean"][i]]
    
sortedScores = sorted(microDatabase["Scores"])
quarterSubset = sortedScores[:int(len(sortedScores) / 10)]

# TODO: Fix point creation system, cannot pass 65.23

# TODO: Pre-set threshold
# threshold = sum(quarterSubset) / len(quarterSubset)
threshold = 200
print("Threshold: ", threshold)

# TODO: Do not forget to re-enable this part!
#showGraph(microDatabase["Scores"], amoxResList, "Score", "Amoxycillin Resistance", "Amoxycillin Resistance vs Score")


####################### TEST SET #######################
# TODO: Don't forget that the test set is below. This is just a comment for visualisation. No meaning.
####################### TEST SET #######################

herdSizeList = []
organicList = []
amoxResList = []
poultryList = []
wasteMilkList = []
weanList = []

with open('testSet.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip the header row
    headerRow = next(reader)
    
    for row in reader:
        herdSize = row[headerRow.index("herd_size")]
        amoxValue = row[headerRow.index("amoxR")]
        organicValue = row[headerRow.index("organic")]
        poultryValues = row[headerRow.index("poultry")]
        wasteMilkValue = row[headerRow.index("anything_waste")]
        weanValue = row[headerRow.index("wean")]

        herdSizeList.append(int(herdSize))
        organicList.append(int(organicValue))
        amoxResList.append(True if amoxValue == '1' else False)
        poultryList.append(int(poultryValues))
        wasteMilkList.append(int(wasteMilkValue))
        weanList.append(int(weanValue))

result = {
    "Amoxycillin Resistance": amoxResList,
    "Score": [], 
    "Findings": []
}

# mal confidence zaaaaa xd
confidence = 0

for i in range(len(amoxResList)):
    # Get scores for each characteristic
    score = organicScores[organicList[i]] + herdSizeScores[herdSizeList[i]] + poultryScores[poultryList[i]] + wasteMilkScores[wasteMilkList[i]] + weanScores[weanList[i]]
    result["Score"].append(score)

    # Compare score to threshold
    result["Findings"].append(True if score >= threshold else False)

    # Compare findings to actual result
    if result["Findings"][i] == amoxResList[i]:
        confidence += 1
    

print(tabulate(result, headers="keys", tablefmt="github"))
print(confidence / len(amoxResList) * 100)