import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

herdSizeList = []
organicList = []
amoxResList = []

def showGraph(xValues, yValues, xLabel, yLabel, title):
    plt.bar(xValues, yValues, width=0.3)

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)

    plt.show()

with open('dairy_farms_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip the header row
    headerRow = next(reader)
    
    for row in reader:
        herdSize = row[headerRow.index("herd_size")]
        amoxValue = row[headerRow.index("amoxR")]
        organicValue = row[headerRow.index("organic")]

        herdSizeList.append(int(herdSize))
        organicList.append(int(organicValue))
        amoxResList.append(True if amoxValue == '1' else False)

herdSizeResistance = [value for value, condition in zip(herdSizeList, amoxResList) if condition]
organicResistance = [value for value, condition in zip(organicList, amoxResList) if condition]

herdSizeCounter = Counter(herdSizeResistance)
sortedHerdSizeCounter = dict(sorted(herdSizeCounter.items(), key=lambda item: item[0]))

organicCounter = Counter(organicResistance)
sortedOrganicCounter = dict(sorted(organicCounter.items(), key=lambda item: item[0]))

organicValues = list(sortedOrganicCounter.values())
print("Organic Values")
for i in organicValues:
    print(i / sum(organicValues) * 100)

herdValues = list(sortedHerdSizeCounter.values())
print("Herd Size Values")
for i in herdValues:
    print(i / sum(herdValues) * 100)

twoList = herdValues + organicValues
print("Two List Values")
for i in twoList:
    print(i / sum(twoList) * 100)

showGraph(list(sortedHerdSizeCounter.keys()), list(sortedHerdSizeCounter.values()), "Herd Size", "Frequency of Amox Resistance", "Herd Size vs. Amox Resistance")
showGraph(list(sortedOrganicCounter.keys()), list(sortedOrganicCounter.values()), "Organic", "Frequency of Amox Resistance", "Organic vs. Amox Resistance")

