# Primary project source code file for the capstone project code 1010393 of Bahçeşehir University
# Currently this project is coded only for the data set available here: https://catalogue.ceh.ac.uk/id/c9bc537a-d1c5-43a0-b146-42c25d4e8160
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
firstMastitisList = [] #firstmastitis
equineList = [] # equine
totalCattleList = [] # total_cattle
yieldList = [] # yield
pneumVaccList = [] # pneum_vacc
diarrVaccList = [] # diarrvacc
antiCoccList = [] # anticocc
halocurList = [] # halocur
nsaidList = [] # nsaiddiarr
throughCleanList = [] # trough_clean
timeDamList = [] # time_dam
umSprayList = [] # um_spray
patternList = [] # pattern

antibioticInteger = input("Choose an antibiotic\n1) cipR\n2) tetR\n3) cephR\n4) strepR\n5) amoxR\nInput:")
antibiotic = switch(int(antibioticInteger))

with open('trainSet.csv', 'r') as f:
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
        firstMastitisValue = row[headerRow.index("firstmastitis")]
        equineValue = row[headerRow.index("equine")]
        totalCattleValue = row[headerRow.index("total_cattle")]
        yieldValue = row[headerRow.index("yield")]
        pneumVaccValue = row[headerRow.index("pneum_vacc")]
        diarrVaccValue = row[headerRow.index("diarrvacc")]
        antiCoccValue = row[headerRow.index("anticocc")]
        halocurValue = row[headerRow.index("halocur")]
        nsaidValue = row[headerRow.index("nsaiddiarr")]
        throughCleanValue = row[headerRow.index("trough_clean")]
        timeDamValue = row[headerRow.index("time_dam")]
        umSprayValue = row[headerRow.index("um_spray")]
        patternValue = row[headerRow.index("pattern")]

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
        firstMastitisList.append(''.join(e for e in firstMastitisValue if e.isalnum()))
        equineList.append(int(equineValue))
        totalCattleList.append(int(totalCattleValue))
        yieldList.append(int(yieldValue))
        pneumVaccList.append(int(pneumVaccValue))
        diarrVaccList.append(0 if diarrVaccValue == 'N' else 1)
        antiCoccList.append(int(antiCoccValue))
        halocurList.append(int(halocurValue))
        nsaidList.append(int(nsaidValue))
        throughCleanList.append(int(throughCleanValue))
        timeDamList.append(int(timeDamValue))
        umSprayList.append(int(umSprayValue))
        patternList.append(int(patternValue))

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
    "First Mastitis": firstMastitisList,
    "Equine": equineList,
    "Total Cattle": totalCattleList,
    "Yield": yieldList,
    "Pneum Vacc": pneumVaccList,
    "Diarr Vacc": diarrVaccList,
    "Anti Cocc": antiCoccList,
    "Halocur": halocurList,
    "NSAID": nsaidList,
    "Trough Clean": throughCleanList,
    "Time Dam": timeDamList,
    "Umbilicus Spray": umSprayList,
    "Calving Pattern": patternList,
    "Scores": []
}

binaryNames = [0, 1]
ordinalNames = [1, 2]
categoryNames = [1, 2, 3]
weanNames = [1, 2, 3]
animalNames = ["a", "d", "pw", "h"]
clinicalMastitisNames = ["Amphenicol", "Macrolide", "Penicillimoxycillin", "Tetracycline", "Otherdontknow"] # Fifth
firstMastitisNames = ["Cobactan", "MastiplanLC", "OrbeninLA", "UbroYellow", "Ubrolexin", "amoxyclav", "tdmultiject"]


organicScores = getScores(organicList, antibioticResList, binaryNames)
herdSizeScores = getScores(herdSizeList, antibioticResList, categoryNames)
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
firstMastitisScores = getScores(firstMastitisList, antibioticResList, firstMastitisNames)
equineScores = getScores(equineList, antibioticResList, binaryNames)
totalCattleScores = getScores(totalCattleList, antibioticResList, categoryNames)
yieldScores = getScores(yieldList, antibioticResList, categoryNames)
pneumVaccScores = getScores(pneumVaccList, antibioticResList, binaryNames)
diarrVaccScores = getScores(diarrVaccList, antibioticResList, binaryNames)
antiCoccScores = getScores(antiCoccList, antibioticResList, binaryNames)
halocurScores = getScores(halocurList, antibioticResList, binaryNames)
nsaidScores = getScores(nsaidList, antibioticResList, binaryNames)
throughCleanScores = getScores(throughCleanList, antibioticResList, ordinalNames)
timeDamScores = getScores(timeDamList, antibioticResList, ordinalNames)
umSprayScores = getScores(umSprayList, antibioticResList, binaryNames)
patternScores = getScores(patternList, antibioticResList, ordinalNames)

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
    microDatabase["Scores"][i] += firstMastitisScores[microDatabase["First Mastitis"][i]]
    microDatabase["Scores"][i] += equineScores[microDatabase["Equine"][i]]
    microDatabase["Scores"][i] += totalCattleScores[microDatabase["Total Cattle"][i]]
    microDatabase["Scores"][i] += yieldScores[microDatabase["Yield"][i]]
    microDatabase["Scores"][i] += pneumVaccScores[microDatabase["Pneum Vacc"][i]]
    microDatabase["Scores"][i] += diarrVaccScores[microDatabase["Diarr Vacc"][i]]
    microDatabase["Scores"][i] += antiCoccScores[microDatabase["Anti Cocc"][i]]
    microDatabase["Scores"][i] += halocurScores[microDatabase["Halocur"][i]]
    microDatabase["Scores"][i] += nsaidScores[microDatabase["NSAID"][i]]
    microDatabase["Scores"][i] += throughCleanScores[microDatabase["Trough Clean"][i]]
    microDatabase["Scores"][i] += timeDamScores[microDatabase["Time Dam"][i]]
    microDatabase["Scores"][i] += umSprayScores[microDatabase["Umbilicus Spray"][i]]
    microDatabase["Scores"][i] += patternScores[microDatabase["Calving Pattern"][i]]
    
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
firstMastitisList = []
equineList = []
totalCattleList = []
yieldList = []
pneumVaccList = []
diarrVaccList = []
antiCoccList = []
halocurList = []
nsaidList = []
throughCleanList = []
timeDamList = []
umSprayList = []
patternList = []

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