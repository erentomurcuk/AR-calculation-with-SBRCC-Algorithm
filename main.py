# Primary project source code file for the capstone project code 1010393 of Bahçeşehir University
# This project is coded only for the data set available here: https://catalogue.ceh.ac.uk/id/c9bc537a-d1c5-43a0-b146-42c25d4e8160
# Baytemur, Furkan Doğancan (github: Kaaleyah) & Tomurcuk, Ahmet Eren (github: erentomurcuk)

# All rights reserved, 2023

    # ♫ Victim of your certainty ♫
    # ♫ And therefore, your doubt's not an option ♫
    #                                TOOL - 7empest

# To a bright future for both of us. It awaits us into a new world. To graduation! Skål! 🥂

import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

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
    
    for value in charList:
        if value not in zippedList:
            zippedList.append(value)

    #TODO: Include the ones that are not resistant

    sortedCharCounter = dict(sorted(Counter(zippedList).items(), key=lambda item: item[0]))
    sortedResCounter = dict(sorted(Counter(charList).items(), key=lambda item: item[0]))

    for i in zip(sortedCharCounter.values(), sortedResCounter.values(), charNames):
        result = (i[0] / i[1] * 100)

        #print(f"{i[2]}: {result}")
        scores[i[2]] = result

    return scores

def switch(aInt):
    if aInt == 1:
        return "cipR"
    elif aInt == 2:
        return "tetR"
    elif aInt == 3:
        return "cephR"
    elif aInt == 4:
        return "strepR"
    elif aInt == 5:
        return "amoxR"
    else:
        exit()

##### MAIN #####

#) list name # name in .csv file
# STEP 1: Create the lists for the specific columns
animalSampledList = [] # animals_sampled
herdSizeList = [] # herd_size
organicList = [] # organic
antibioticResList = [] # amoxR
poultryList = [] # poultry
wasteMilkList = [] # anything_waste
weanList = [] # wean
ctxMList = [] # ctx_m
weanedHeiferList = [] # weaned_heifer
adultList = [] # adult
dryList = [] # dry
footPathList = [] # footpath
ampCList = [] # amp_c
heiferWasteList = [] # heifers_waste
clinicalMastitisList = [] # whichclinresp
equineList = [] # equine
totalCattleList = [] # total_cattle

antibioticInteger = input("Choose an antibiotic\n1) cipR\n2) tetR\n3) cephR\n4) strepR\n5) amoxR\nInput:")
antibiotic = switch(int(antibioticInteger))

with open('dairy_farms_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip the header row #
    headerRow = next(reader)
    
    # STEP 2: Get the data from the .csv file
    for row in reader:
        herdSize = row[headerRow.index("herd_size")]
        antibioticValue = row[headerRow.index(antibiotic)]
        organicValue = row[headerRow.index("organic")]
        poultryValues = row[headerRow.index("poultry")]
        wasteMilkValue = row[headerRow.index("anything_waste")]
        weanValue = row[headerRow.index("wean")]
        animalSampleValue = row[headerRow.index("animals_sampled")]
        ctxMValue = row[headerRow.index("ctx_m")]
        weanedHeiferValue = row[headerRow.index("weaned_heifer")]
        adultValue = row[headerRow.index("adult")]
        dryValue = row[headerRow.index("dry")]
        footPathValue = row[headerRow.index("footpath")]
        ampCValue = row[headerRow.index("amp_c")]
        heiferWasteValue = row[headerRow.index("heifers_waste")]
        clinicalMastitisValue = row[headerRow.index("whichclinresp")]
        equineValue = row[headerRow.index("equine")]
        totalCattleValue = row[headerRow.index("total_cattle")]

        # STEP 3: Append the data to the lists
        herdSizeList.append(int(herdSize))
        organicList.append(int(organicValue))
        antibioticResList.append(True if antibioticValue == '1' else False)
        poultryList.append(int(poultryValues))
        wasteMilkList.append(int(wasteMilkValue))
        weanList.append(int(weanValue))
        animalSampledList.append(animalSampleValue)
        ctxMList.append(int(ctxMValue))
        weanedHeiferList.append(int(weanedHeiferValue))
        adultList.append(int(adultValue))
        dryList.append(int(dryValue))
        footPathList.append(int(footPathValue))
        ampCList.append(int(ampCValue))
        heiferWasteList.append(int(heiferWasteValue))
        clinicalMastitisList.append(''.join(e for e in clinicalMastitisValue if e.isalnum()))
        equineList.append(int(equineValue))
        totalCattleList.append(int(totalCattleValue))

# STEP 4: Add the list into the microDatabase
microDatabase = {
    "Amoxycillin Resistance": antibioticResList,
    "Herd Size": herdSizeList,
    "Organic": organicList,
    "Poultry": poultryList,
    "Waste Milk": wasteMilkList,
    "Wean": weanList,
    "Animal Sampled": animalSampledList,
    "CTX-M": ctxMList,
    "Weaned Heifer": weanedHeiferList,
    "Adult": adultList,
    "Dry": dryList,
    "Foot Path": footPathList,
    "Amp-C": ampCList,
    "Heifer Waste": heiferWasteList,
    "Clinical Mastitis": clinicalMastitisList,
    "Equine": equineList,
    "Total Cattle": totalCattleList,

    "Scores": []
}

# Code below is for setting up the types of the data on the column. If required, new ones should be added.
# STEP 5: Add the type of the data if it does not exist here
binaryNames = [0, 1]
herdSizeNames = [1, 2, 3]
weanNames = [1, 2, 3]
animalNames = ["a", "d", "pw", "h"]
clinicalMastitisNames = ["Amphenicol", "Macrolide", "Penicillimoxycillin", "Tetracycline", "Otherdontknow"]
totalCattleNames = [1, 2, 3]

# STEP 6: Get the scores for each column (xList, antibioticResList, xNames)
organicScores = getScores(organicList, antibioticResList, binaryNames)
herdSizeScores = getScores(herdSizeList, antibioticResList, herdSizeNames)
poultryScores = getScores(poultryList, antibioticResList, binaryNames)
wasteMilkScores = getScores(wasteMilkList, antibioticResList, binaryNames)
weanScores = getScores(weanList, antibioticResList, weanNames)
animalSampleScores = getScores(animalSampledList, antibioticResList, animalNames)
ctxMScores = getScores(ctxMList, antibioticResList, binaryNames)
weanedHeiferScores = getScores(weanedHeiferList, antibioticResList, binaryNames)
adultScores = getScores(adultList, antibioticResList, binaryNames)
dryScores = getScores(dryList, antibioticResList, binaryNames)
footPathScores = getScores(footPathList, antibioticResList, binaryNames)
ampCScores = getScores(ampCList, antibioticResList, binaryNames)
heiferWasteScores = getScores(heiferWasteList, antibioticResList, binaryNames)
clinicalMastitisScores = getScores(clinicalMastitisList, antibioticResList, clinicalMastitisNames)
equineScores = getScores(equineList, antibioticResList, binaryNames)
totalCattleScores = getScores(totalCattleList, antibioticResList, totalCattleNames)

# STEP 7: Add the scores to the microDatabase
for i in range(len(antibioticResList)):
    microDatabase["Scores"].append(organicScores[microDatabase["Organic"][i]])
    microDatabase["Scores"][i] + herdSizeScores[microDatabase["Herd Size"][i]] + \
        poultryScores[microDatabase["Poultry"][i]] + \
        wasteMilkScores[microDatabase["Waste Milk"][i]] + \
        weanScores[microDatabase["Wean"][i]] + \
        animalSampleScores[microDatabase["Animal Sampled"][i]] + \
        ctxMScores[microDatabase["CTX-M"][i]] + \
        weanedHeiferScores[microDatabase["Weaned Heifer"][i]] + \
        adultScores[microDatabase["Adult"][i]] + \
        dryScores[microDatabase["Dry"][i]] + \
        footPathScores[microDatabase["Foot Path"][i]] + \
        ampCScores[microDatabase["Amp-C"][i]] + \
        heiferWasteScores[microDatabase["Heifer Waste"][i]] + \
        clinicalMastitisScores[microDatabase["Clinical Mastitis"][i]] + \
        equineScores[microDatabase["Equine"][i]] + \
        totalCattleScores[microDatabase["Total Cattle"][i]]
    
sortedScores = sorted(microDatabase["Scores"])
quarterSubset = sortedScores[:int(len(sortedScores) / 5)]

# TODO: Pre-set threshold
threshold = sum(quarterSubset) / len(quarterSubset)
#threshold = 200
print("Threshold: ", threshold)

# TODO: Do not forget to re-enable this part!
#showGraph(microDatabase["Scores"], antibioticResList, "Score", "Amoxycillin Resistance", "Amoxycillin Resistance vs Score")


####################### TEST SET #######################
# Don't forget that the test set is below. This is just a comment for visualisation. No meaning.
####################### TEST SET #######################

# STEP 8: Create the list for the test set
herdSizeList = []
organicList = []
antibioticResList = []
poultryList = []
wasteMilkList = []
weanList = []
animalSampledList = []
ctxMList = []
weanedHeiferList = []
adultList = []
dryList = []
footPathList = []
ampCList = []
heiferWasteList = []
clinicalMastitisList = []
equineList = []
totalCattleList = []

with open('testSet.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip the header row
    headerRow = next(reader)
    
    # STEP 9: Set the column names for the value lists
    for row in reader:
        herdSize = row[headerRow.index("herd_size")]
        antibioticValue = row[headerRow.index(antibiotic)]
        organicValue = row[headerRow.index("organic")]
        poultryValues = row[headerRow.index("poultry")]
        wasteMilkValue = row[headerRow.index("anything_waste")]
        weanValue = row[headerRow.index("wean")]
        animalSampleValue = row[headerRow.index("animals_sampled")]
        ctxMValue = row[headerRow.index("ctx_m")]
        weanedHeiferValue = row[headerRow.index("weaned_heifer")]
        adultValue = row[headerRow.index("adult")]
        dryValue = row[headerRow.index("dry")]
        footPathValue = row[headerRow.index("footpath")]
        ampCValue = row[headerRow.index("amp_c")]
        heiferWasteValue = row[headerRow.index("heifers_waste")]
        clinicalMastitisValue = row[headerRow.index("whichclinresp")]
        equineValue = row[headerRow.index("equine")]
        totalCattleValue = row[headerRow.index("total_cattle")]

        # STEP 10: Append the values to the lists
        herdSizeList.append(int(herdSize))
        organicList.append(int(organicValue))
        antibioticResList.append(True if antibioticValue == '1' else False)
        poultryList.append(int(poultryValues))
        wasteMilkList.append(int(wasteMilkValue))
        weanList.append(int(weanValue))
        animalSampledList.append(animalSampleValue)
        ctxMList.append(int(ctxMValue))
        weanedHeiferList.append(int(weanedHeiferValue))
        adultList.append(int(adultValue))
        dryList.append(int(dryValue))
        footPathList.append(int(footPathValue))
        ampCList.append(int(ampCValue))
        heiferWasteList.append(int(heiferWasteValue))
        clinicalMastitisList.append(clinicalMastitisValue)
        equineList.append(int(equineValue))
        totalCattleList.append(int(totalCattleValue))

result = {
    "Amoxycillin Resistance": antibioticResList,
    "Score": [], 
    "Findings": []
}

confidence = 0
score = 0

for i in range(len(antibioticResList)):

    # Get scores for each characteristic
    # STEP 11: Add the scores for each characteristic
    score += organicScores[organicList[i]] + \
            herdSizeScores[herdSizeList[i]] + \
            poultryScores[poultryList[i]] + \
            wasteMilkScores[wasteMilkList[i]] + \
            weanScores[weanList[i]] + \
            animalSampleScores[animalSampledList[i]] + \
            ctxMScores[ctxMList[i]] + \
            weanedHeiferScores[weanedHeiferList[i]] + \
            adultScores[adultList[i]] + \
            dryScores[dryList[i]] + \
            footPathScores[footPathList[i]] + \
            ampCScores[ampCList[i]] + \
            heiferWasteScores[heiferWasteList[i]] + \
            clinicalMastitisScores[clinicalMastitisList[i]] + \
            equineScores[equineList[i]] + \
            totalCattleScores[totalCattleList[i]]
    
    result["Score"].append(score)

    # Compare score to threshold
    result["Findings"].append(True if score >= threshold else False)

    # Compare findings to actual result
    if result["Findings"][i] == antibioticResList[i]:
        confidence += 1
    
print(tabulate(result, headers="keys", tablefmt="github"))
print(f"Confidence: {confidence / len(antibioticResList) * 100}%")