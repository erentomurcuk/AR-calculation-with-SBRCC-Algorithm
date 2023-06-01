# Second calculation method of scoring

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
clinicalMastitisList = [] # whichclinresp #First

antibioticInteger = input("Choose an antibiotic\n1) cipR\n2) tetR\n3) cephR\n4) strepR\n5) amoxR\nInput:")
antibiotic = switch(int(antibioticInteger))

with open('dairy_farms_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip the header row #
    headerRow = next(reader)
    
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
        clinicalMastitisValue = row[headerRow.index("whichclinresp")] #Second

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
        clinicalMastitisList.append(''.join(e for e in clinicalMastitisValue if e.isalnum())) #Third

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
    "Clinical Mastitis": clinicalMastitisList, # Fourth
    "Scores": []
}

binaryNames = [0, 1]
herdSizeNames = [1, 2, 3]
weanNames = [1, 2, 3]
animalNames = ["a", "d", "pw", "h"]
clinicalMastitisNames = ["Amphenicol", "Macrolide", "Penicillimoxycillin", "Tetracycline", "Otherdontknow"] # Fifth

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
clinicalMastitisScores = getScores(clinicalMastitisList, antibioticResList, clinicalMastitisNames) # Sixth

for i in range(len(antibioticResList)):
    microDatabase["Scores"].append(organicScores[microDatabase["Organic"][i]])
    microDatabase["Scores"][i] += herdSizeScores[microDatabase["Herd Size"][i]]
    microDatabase["Scores"][i] += poultryScores[microDatabase["Poultry"][i]]
    microDatabase["Scores"][i] += wasteMilkScores[microDatabase["Waste Milk"][i]]
    microDatabase["Scores"][i] += weanScores[microDatabase["Wean"][i]]
    microDatabase["Scores"][i] += animalSampleScores[microDatabase["Animal Sampled"][i]]
    microDatabase["Scores"][i] += ctxMScores[microDatabase["CTX-M"][i]]
    microDatabase["Scores"][i] += weanedHeiferScores[microDatabase["Weaned Heifer"][i]]
    microDatabase["Scores"][i] += adultScores[microDatabase["Adult"][i]]
    microDatabase["Scores"][i] += dryScores[microDatabase["Dry"][i]]
    microDatabase["Scores"][i] += footPathScores[microDatabase["Foot Path"][i]]
    microDatabase["Scores"][i] += ampCScores[microDatabase["Amp-C"][i]]
    microDatabase["Scores"][i] += heiferWasteScores[microDatabase["Heifer Waste"][i]]
    microDatabase["Scores"][i] += clinicalMastitisScores[microDatabase["Clinical Mastitis"][i]] # Seventh
    
sortedScores = sorted(microDatabase["Scores"])
quarterSubset = sortedScores[:int(len(sortedScores) / 5)]

# TODO: Fix point creation system, cannot pass 65.23

# TODO: Pre-set threshold
threshold = sum(quarterSubset) / len(quarterSubset)
#threshold = 200
print("Threshold: ", threshold)

# TODO: Do not forget to re-enable this part!
#showGraph(microDatabase["Scores"], antibioticResList, "Score", "Amoxycillin Resistance", "Amoxycillin Resistance vs Score")


####################### TEST SET #######################
# Don't forget that the test set is below. This is just a comment for visualisation. No meaning.
####################### TEST SET #######################

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
clinicalMastitisList = [] # Eighth

with open('testSet.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip the header row
    headerRow = next(reader)
    
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
        clinicalMastitisValue = row[headerRow.index("whichclinresp")] # Ninth

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
        clinicalMastitisList.append(clinicalMastitisValue) # Tenth

result = {
    "Amoxycillin Resistance": antibioticResList,
    "Score": [], 
    "Findings": []
}

confidence = 0
score = 0

for i in range(len(antibioticResList)):

    # Get scores for each characteristic
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
            clinicalMastitisScores[clinicalMastitisList[i]] # Eleventh
    
    result["Score"].append(score)

    # Compare score to threshold
    result["Findings"].append(True if score >= threshold else False)

    # Compare findings to actual result
    if result["Findings"][i] == antibioticResList[i]:
        confidence += 1
    

print(tabulate(result, headers="keys", tablefmt="github"))
print(f"Confidence: {confidence / len(antibioticResList) * 100}%")