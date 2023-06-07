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

def determineRange(scores):
    minScore = min(scores)
    maxScore = max(scores)

    intervalSize = (maxScore - minScore) / 30
    # cipR 10


    ranges = [(minScore + i * intervalSize, minScore + (i + 1) * intervalSize) for i in range(5)]

    intervalCounts = [0] * 5

    for score in scores:
        for i, (lower, upper) in enumerate(ranges):
            if lower <= score < upper:
                intervalCounts[i] += 1
                break

    maxCount = max(intervalCounts)

    mostCommonRange = [ranges[i] for i, count in enumerate(intervalCounts) if count == maxCount]

    commonScores = []

    for i in mostCommonRange:
        commonScores.append(i[0])
        commonScores.append(i[1])

    return commonScores

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
        result = (i[0] / i[1] * 1000)

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
antibioticResList = []
animalSampledList = [] # animals_sampled
herdSizeList = [] # herd_size
organicList = [] # organic
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
colostrumList = [] # give_col
calvingGroupList = [] # calving_group
calfHousingTypeList = [] # calhousing_type
calfHousingOlderList = [] # calhousing_older
othergrazeList = [] # othergraze
bvdList = [] # bvdvacc
ibrList = [] # ibrvacc
leptoList = [] # leptovacc
salmList = [] # salmvacc
lungList = [] # lungvacc
clostList = [] # clostvacc
treatFootList = [] # treatfoot
abCalveList = [] # abcalve
nsaidCalveList = [] # nsaidcalve
calveCleanList = [] # calveclean
milkGrazeList = [] # milkgraze
limeList = [] # lime
predipList = [] # predip
acfList = [] # acf
cleanClusterList = [] # cleancluster
dryTroughList = [] # drytrough
premisesList = [] # premises
showsList = [] # shows
marketList = [] # market
hostFarmWalkList = [] # hostfarmwalk
starlingList = [] # starling
deerList = [] # deer
badgerList = [] # badger
rookList = [] # rook
pigeonList = [] # pigeon
foxList = [] # fox
pheasantList = [] # pheasant
ratList = [] # rat
shootList = [] # shoot
huntList = [] # hunt
outSourceList = [] # outsource
feedLorryList = [] # feedlorry
aiExtersList = [] # aiexternal
machineryList = [] # machinery
housedOutdoorList = [] # s_housed_outdoor
cefqList = [] # cefq_dct
cephList = [] # ceph_dct
framList = [] # fram_dct
cloxList = [] # clox_dct
calvingNowList = [] # s_calving_now
waterList = [] # water
preWeanedHeiferList = [] # preweaned_heifer

def fetchColumns(fileName):
    with open(fileName, 'r') as f:
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
            colostrumValue = row[headerRow.index("give_col")]
            calvingGroupValue = row[headerRow.index("calving_group")]
            calfHousingTypeValue = row[headerRow.index("calhousing_type")]
            calfHousingOlderValue = row[headerRow.index("calhousing_older")]
            othergrazeValue = row[headerRow.index("othergraze")]
            bvdValue = row[headerRow.index("bvdvacc")]
            ibrValue = row[headerRow.index("ibrvacc")]
            leptoValue = row[headerRow.index("leptovacc")]
            salmValue = row[headerRow.index("salmvacc")]
            lungValue = row[headerRow.index("lungvacc")]
            clostValue = row[headerRow.index("clostvacc")]
            treatFootValue = row[headerRow.index("treatfoot")]
            abCalveValue = row[headerRow.index("abcalve")]
            nsaidCalveValue = row[headerRow.index("nsaidcalve")]
            calveCleanValue = row[headerRow.index("calveclean")]
            milkGrazeValue = row[headerRow.index("milkgraze")]
            limeValue = row[headerRow.index("lime")]
            predipValue = row[headerRow.index("predip")]
            acfValue = row[headerRow.index("acf")]
            cleanClusterValue = row[headerRow.index("cleancluster")]
            dryTroughValue = row[headerRow.index("drytrough")]
            premisesValue = row[headerRow.index("premises")]
            showsValue = row[headerRow.index("shows")]
            marketValue = row[headerRow.index("market")]
            hostFarmWalkValue = row[headerRow.index("hostfarmwalk")]
            starlingValue = row[headerRow.index("starling")]
            deerValue = row[headerRow.index("deer")]
            badgerValue = row[headerRow.index("badger")]
            rookValue = row[headerRow.index("rook")]
            pigeonValue = row[headerRow.index("pigeon")]
            foxValue = row[headerRow.index("fox")]
            pheasantValue = row[headerRow.index("pheasant")]
            ratValue = row[headerRow.index("rat")]
            shootValue = row[headerRow.index("shoot")]
            huntValue = row[headerRow.index("hunt")]
            outSourceValue = row[headerRow.index("outsource")]
            feedLorryValue = row[headerRow.index("feedlorry")]
            aiExtersValue = row[headerRow.index("aiexternal")]
            machineryValue = row[headerRow.index("machinery")]
            housedOutdoorValue = row[headerRow.index("s_housed_outdoor")]
            cefqValue = row[headerRow.index("cefq_dct")]
            cephValue = row[headerRow.index("ceph_dct")]
            framValue = row[headerRow.index("fram_dct")]
            cloxValue = row[headerRow.index("clox_dct")]
            calvingNowValue = row[headerRow.index("s_calving_now")]
            waterValue = row[headerRow.index("water")]
            preWeanedHeiferValue = row[headerRow.index("preweaned_heifer")]

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
            colostrumList.append(int(colostrumValue))
            calvingGroupList.append(int(calvingGroupValue))
            calfHousingTypeList.append(int(calfHousingTypeValue))
            calfHousingOlderList.append(int(calfHousingOlderValue))
            othergrazeList.append(0 if othergrazeValue == 'N' else 1)
            bvdList.append(0 if bvdValue == 'N' else 1)
            ibrList.append(0 if ibrValue == 'N' else 1)
            leptoList.append(0 if leptoValue == 'N' else 1)
            salmList.append(0 if salmValue == 'N' else 1)
            lungList.append(0 if lungValue == 'N' else 1)
            clostList.append(0 if clostValue == 'N' else 1)
            treatFootList.append(int(treatFootValue))
            abCalveList.append(int(abCalveValue))
            nsaidCalveList.append(int(nsaidCalveValue))
            calveCleanList.append(int(calveCleanValue))
            milkGrazeList.append(int(milkGrazeValue))
            limeList.append(int(limeValue))
            predipList.append(int(predipValue))
            acfList.append(int(acfValue))
            cleanClusterList.append(int(cleanClusterValue))
            dryTroughList.append(int(dryTroughValue))
            premisesList.append(int(premisesValue))
            showsList.append(int(showsValue))
            marketList.append(int(marketValue))
            hostFarmWalkList.append(int(hostFarmWalkValue))
            starlingList.append(int(starlingValue))
            deerList.append(int(deerValue))
            badgerList.append(int(badgerValue))
            rookList.append(int(rookValue))
            pigeonList.append(int(pigeonValue))
            foxList.append(int(foxValue))
            pheasantList.append(int(pheasantValue))
            ratList.append(int(ratValue))
            shootList.append(int(shootValue))
            huntList.append(int(huntValue))
            outSourceList.append(int(outSourceValue))
            feedLorryList.append(int(feedLorryValue))
            aiExtersList.append(int(aiExtersValue))
            machineryList.append(int(machineryValue))
            housedOutdoorList.append(housedOutdoorValue)
            cefqList.append(int(cefqValue))
            cephList.append(int(cephValue))
            framList.append(int(framValue))
            cloxList.append(int(cloxValue))
            calvingNowList.append(int(calvingNowValue))
            waterList.append(int(waterValue))
            preWeanedHeiferList.append(int(preWeanedHeiferValue))


antibioticInteger = input("Choose an antibiotic\n1) cipR\n2) tetR\n3) cephR\n4) strepR\n5) amoxR\nInput:")
antibiotic = switch(int(antibioticInteger))

# Fetch from training data #
fetchColumns("trainSet.csv")

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
    "Colostrum": colostrumList,
    "Calving Group": calvingGroupList,
    "Calf Housing Type": calfHousingTypeList,
    "Calf Housing Older": calfHousingOlderList,
    "Other Grazing": othergrazeList,
    "BVD Vaccination": bvdList,
    "IBR Vaccination": ibrList,
    "Lepto Vaccination": leptoList,
    "Salmonella Vaccination": salmList,
    "Lungworm Vaccination": lungList,
    "Clostridial Vaccination": clostList,
    "Treat Foot": treatFootList,
    "Antibiotics at Calving": abCalveList,
    "NSAID at Calving": nsaidCalveList,
    "Calving Area Clean": calveCleanList,
    "Milking Cow Graze": milkGrazeList,
    "Lime": limeList,
    "Predip": predipList,
    "Automatic Cluster Flush": acfList,
    "Clean Cluster": cleanClusterList,
    "Dry Cow Trough": dryTroughList,
    "Premises": premisesList,
    "Shows": showsList,
    "Market": marketList,
    "Host Farm Walk": hostFarmWalkList,
    "Starling": starlingList,
    "Deer": deerList,
    "Badger": badgerList,
    "Rook": rookList,
    "Pigeon": pigeonList,
    "Fox": foxList,
    "Pheasant": pheasantList,
    "Rat": ratList,
    "Shoot": shootList,
    "Hunt": huntList,
    "Out Source": outSourceList,
    "Feed Lorry": feedLorryList,
    "AI External": aiExtersList,
    "Machinery": machineryList,
    "Housed Outdoor": housedOutdoorList,
    "Cefquinome": cefqList,
    "Cephalonium": cephList,
    "Framycetin": framList,
    "Cloxacillin": cloxList,
    "Calving Now": calvingNowList,
    "Water": waterList,
    "Pre-Weaned Heifer": preWeanedHeiferList,
    "Scores": []
}

binaryNames = [0, 1]
ordinalNames = [1, 2]
categoryNames = [1, 2, 3]
weanNames = [1, 2, 3]
animalNames = ["a", "d", "pw", "h"]
clinicalMastitisNames = ["Amphenicol", "Macrolide", "Penicillimoxycillin", "Tetracycline", "Otherdontknow"] # Fifth
firstMastitisNames = ["Cobactan", "MastiplanLC", "OrbeninLA", "UbroYellow", "Ubrolexin", "amoxyclav", "tdmultiject"]
houseNames = ["outdoor", "housed"]


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
colostrumScores = getScores(colostrumList, antibioticResList, binaryNames)
calvingGroupScores = getScores(calvingGroupList, antibioticResList, binaryNames)
calfHousingTypeScores = getScores(calfHousingTypeList, antibioticResList, categoryNames)
calfHousingOlderScores = getScores(calfHousingOlderList, antibioticResList, binaryNames)
othergrazeScores = getScores(othergrazeList, antibioticResList, binaryNames)
bvdScores = getScores(bvdList, antibioticResList, binaryNames)
ibrScores = getScores(ibrList, antibioticResList, binaryNames)
leptoScores = getScores(leptoList, antibioticResList, binaryNames)
salmScores = getScores(salmList, antibioticResList, binaryNames)
lungScores = getScores(lungList, antibioticResList, binaryNames)
clostScores = getScores(clostList, antibioticResList, binaryNames)
treatFootScores = getScores(treatFootList, antibioticResList, binaryNames)
abCalveScores = getScores(abCalveList, antibioticResList, binaryNames)
nsaidCalveScores = getScores(nsaidCalveList, antibioticResList, binaryNames)
calveCleanScores = getScores(calveCleanList, antibioticResList, ordinalNames)
milkGrazeScores = getScores(milkGrazeList, antibioticResList, binaryNames)
limeScores = getScores(limeList, antibioticResList, binaryNames)
predipScores = getScores(predipList, antibioticResList, binaryNames)
acfScores = getScores(acfList, antibioticResList, binaryNames)
cleanClusterScores = getScores(cleanClusterList, antibioticResList, ordinalNames)
dryTroughScores = getScores(dryTroughList, antibioticResList, ordinalNames)
premisesScores = getScores(premisesList, antibioticResList, ordinalNames)
showsScores = getScores(showsList, antibioticResList, binaryNames)
marketScores = getScores(marketList, antibioticResList, binaryNames)
hostFarmWalkScores = getScores(hostFarmWalkList, antibioticResList, binaryNames)
starlingScores = getScores(starlingList, antibioticResList, ordinalNames)
deerScores = getScores(deerList, antibioticResList, ordinalNames)
badgerScores = getScores(badgerList, antibioticResList, ordinalNames)
rookScores = getScores(rookList, antibioticResList, ordinalNames)
pigeonScores = getScores(pigeonList, antibioticResList, ordinalNames)
foxScores = getScores(foxList, antibioticResList, ordinalNames)
pheasantScores = getScores(pheasantList, antibioticResList, ordinalNames)
ratScores = getScores(ratList, antibioticResList, ordinalNames)
shootScores = getScores(shootList, antibioticResList, ordinalNames)
huntScores = getScores(huntList, antibioticResList, ordinalNames)
outSourceScores = getScores(outSourceList, antibioticResList, binaryNames)
feedLorryScores = getScores(feedLorryList, antibioticResList, binaryNames)
aiExtersScores = getScores(aiExtersList, antibioticResList, binaryNames)
machineryScores = getScores(machineryList, antibioticResList, binaryNames)
housedOutdoorScores = getScores(housedOutdoorList, antibioticResList, houseNames)
cefqScores = getScores(cefqList, antibioticResList, binaryNames)
cephScores = getScores(cephList, antibioticResList, binaryNames)
framScores = getScores(framList, antibioticResList, binaryNames)
cloxScores = getScores(cloxList, antibioticResList, binaryNames)
calvingNowScores = getScores(calvingNowList, antibioticResList, binaryNames)
waterScores = getScores(waterList, antibioticResList, binaryNames)
preWeanedHeiferScores = getScores(preWeanedHeiferList, antibioticResList, binaryNames)

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
    microDatabase["Scores"][i] += colostrumScores[microDatabase["Colostrum"][i]]
    microDatabase["Scores"][i] += calvingGroupScores[microDatabase["Calving Group"][i]]
    microDatabase["Scores"][i] += calfHousingTypeScores[microDatabase["Calf Housing Type"][i]]
    microDatabase["Scores"][i] += calfHousingOlderScores[microDatabase["Calf Housing Older"][i]]
    microDatabase["Scores"][i] += othergrazeScores[microDatabase["Other Grazing"][i]]
    microDatabase["Scores"][i] += bvdScores[microDatabase["BVD Vaccination"][i]]
    microDatabase["Scores"][i] += ibrScores[microDatabase["IBR Vaccination"][i]]
    microDatabase["Scores"][i] += leptoScores[microDatabase["Lepto Vaccination"][i]]
    microDatabase["Scores"][i] += salmScores[microDatabase["Salmonella Vaccination"][i]]
    microDatabase["Scores"][i] += lungScores[microDatabase["Lungworm Vaccination"][i]]
    microDatabase["Scores"][i] += clostScores[microDatabase["Clostridial Vaccination"][i]]
    microDatabase["Scores"][i] += treatFootScores[microDatabase["Treat Foot"][i]]
    microDatabase["Scores"][i] += abCalveScores[microDatabase["Antibiotics at Calving"][i]]
    microDatabase["Scores"][i] += nsaidCalveScores[microDatabase["NSAID at Calving"][i]]
    microDatabase["Scores"][i] += calveCleanScores[microDatabase["Calving Area Clean"][i]]
    microDatabase["Scores"][i] += milkGrazeScores[microDatabase["Milking Cow Graze"][i]]
    microDatabase["Scores"][i] += limeScores[microDatabase["Lime"][i]]
    microDatabase["Scores"][i] += predipScores[microDatabase["Predip"][i]]
    microDatabase["Scores"][i] += acfScores[microDatabase["Automatic Cluster Flush"][i]]
    microDatabase["Scores"][i] += cleanClusterScores[microDatabase["Clean Cluster"][i]]
    microDatabase["Scores"][i] += dryTroughScores[microDatabase["Dry Cow Trough"][i]]
    microDatabase["Scores"][i] += premisesScores[microDatabase["Premises"][i]]
    microDatabase["Scores"][i] += showsScores[microDatabase["Shows"][i]]
    microDatabase["Scores"][i] += marketScores[microDatabase["Market"][i]]
    microDatabase["Scores"][i] += hostFarmWalkScores[microDatabase["Host Farm Walk"][i]]
    microDatabase["Scores"][i] += starlingScores[microDatabase["Starling"][i]]
    microDatabase["Scores"][i] += deerScores[microDatabase["Deer"][i]]
    microDatabase["Scores"][i] += badgerScores[microDatabase["Badger"][i]]
    microDatabase["Scores"][i] += rookScores[microDatabase["Rook"][i]]
    microDatabase["Scores"][i] += pigeonScores[microDatabase["Pigeon"][i]]
    microDatabase["Scores"][i] += foxScores[microDatabase["Fox"][i]]
    microDatabase["Scores"][i] += pheasantScores[microDatabase["Pheasant"][i]]
    microDatabase["Scores"][i] += ratScores[microDatabase["Rat"][i]]
    microDatabase["Scores"][i] += shootScores[microDatabase["Shoot"][i]]
    microDatabase["Scores"][i] += huntScores[microDatabase["Hunt"][i]]
    microDatabase["Scores"][i] += outSourceScores[microDatabase["Out Source"][i]]
    microDatabase["Scores"][i] += feedLorryScores[microDatabase["Feed Lorry"][i]]
    microDatabase["Scores"][i] += aiExtersScores[microDatabase["AI External"][i]]
    microDatabase["Scores"][i] += machineryScores[microDatabase["Machinery"][i]]
    microDatabase["Scores"][i] += housedOutdoorScores[microDatabase["Housed Outdoor"][i]]
    microDatabase["Scores"][i] += cefqScores[microDatabase["Cefquinome"][i]]
    microDatabase["Scores"][i] += cephScores[microDatabase["Cephalonium"][i]]
    microDatabase["Scores"][i] += framScores[microDatabase["Framycetin"][i]]
    microDatabase["Scores"][i] += cloxScores[microDatabase["Cloxacillin"][i]]
    microDatabase["Scores"][i] += calvingNowScores[microDatabase["Calving Now"][i]]
    microDatabase["Scores"][i] += waterScores[microDatabase["Water"][i]]
    microDatabase["Scores"][i] += preWeanedHeiferScores[microDatabase["Pre-Weaned Heifer"][i]]

sortedScores = sorted(microDatabase["Scores"])
quarterSubset = sortedScores[:int(len(sortedScores) / 10)]

# TODO: Fix point creation system, cannot pass 65.23

# TODO: Pre-set threshold
threshold = sum(quarterSubset) / len(quarterSubset)
#threshold = 3000

commonRanges = determineRange(sortedScores)

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
colostrumList = []
calvingGroupList = []
calfHousingTypeList = []
calfHousingOlderList = []
othergrazeList = []
bvdList = []
ibrList = []
leptoList = []
salmList = []
lungList = []
clostList = []
treatFootList = []
abCalveList = []
nsaidCalveList = []
calveCleanList = []
milkGrazeList = []
limeList = []
predipList = []
acfList = []
cleanClusterList = []
dryTroughList = []
premisesList = []
showsList = []
marketList = []
hostFarmWalkList = []
starlingList = []
deerList = []
badgerList = []
rookList = []
pigeonList = []
foxList = []
pheasantList = []
ratList = []
shootList = []
huntList = []
outSourceList = []
feedLorryList = []
aiExtersList = []
machineryList = []
housedOutdoorList = []
cefqList = []
cephList = []
framList = []
cloxList = []
calvingNowList = []
waterList = []
preWeanedHeiferList = []

# Fetch for test set
fetchColumns("testSet.csv")

result = {
    "Amoxycillin Resistance": antibioticResList,
    "Score": [], 
    "Findings": []
}

confidence = 0

for i in range(len(antibioticResList)):
    score = 0

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
            clinicalMastitisScores[clinicalMastitisList[i]] + \
            firstMastitisScores[firstMastitisList[i]] + \
            equineScores[equineList[i]] + \
            totalCattleScores[totalCattleList[i]] + \
            yieldScores[yieldList[i]] + \
            pneumVaccScores[pneumVaccList[i]] + \
            diarrVaccScores[diarrVaccList[i]] + \
            antiCoccScores[antiCoccList[i]] + \
            halocurScores[halocurList[i]] + \
            nsaidScores[nsaidList[i]] + \
            throughCleanScores[throughCleanList[i]] + \
            timeDamScores[timeDamList[i]] + \
            umSprayScores[umSprayList[i]] + \
            patternScores[patternList[i]] + \
            colostrumScores[colostrumList[i]] + \
            calvingGroupScores[calvingGroupList[i]] + \
            calfHousingTypeScores[calfHousingTypeList[i]] + \
            calfHousingOlderScores[calfHousingOlderList[i]] + \
            othergrazeScores[othergrazeList[i]] + \
            bvdScores[bvdList[i]] + \
            ibrScores[ibrList[i]] + \
            leptoScores[leptoList[i]] + \
            salmScores[salmList[i]] + \
            lungScores[lungList[i]] + \
            clostScores[clostList[i]] + \
            treatFootScores[treatFootList[i]] + \
            abCalveScores[abCalveList[i]] + \
            nsaidCalveScores[nsaidCalveList[i]] + \
            calveCleanScores[calveCleanList[i]] + \
            milkGrazeScores[milkGrazeList[i]] + \
            limeScores[limeList[i]] + \
            predipScores[predipList[i]] + \
            acfScores[acfList[i]] + \
            cleanClusterScores[cleanClusterList[i]] + \
            dryTroughScores[dryTroughList[i]] + \
            premisesScores[premisesList[i]] + \
            showsScores[showsList[i]] + \
            marketScores[marketList[i]] + \
            hostFarmWalkScores[hostFarmWalkList[i]] + \
            starlingScores[starlingList[i]] + \
            deerScores[deerList[i]] + \
            badgerScores[badgerList[i]] + \
            rookScores[rookList[i]] + \
            pigeonScores[pigeonList[i]] + \
            foxScores[foxList[i]] + \
            pheasantScores[pheasantList[i]] + \
            ratScores[ratList[i]] + \
            shootScores[shootList[i]] + \
            huntScores[huntList[i]] + \
            outSourceScores[outSourceList[i]] + \
            feedLorryScores[feedLorryList[i]] + \
            aiExtersScores[aiExtersList[i]] + \
            machineryScores[machineryList[i]] + \
            housedOutdoorScores[housedOutdoorList[i]] + \
            cefqScores[cefqList[i]] + \
            cephScores[cephList[i]] + \
            framScores[framList[i]] + \
            cloxScores[cloxList[i]] + \
            calvingNowScores[calvingNowList[i]] + \
            waterScores[waterList[i]] + \
            preWeanedHeiferScores[preWeanedHeiferList[i]]
     
    result["Score"].append(score)

    if score > float(antibioticInteger) * 6666:
        result["Findings"].append(True if score >= threshold else False)
    else:
        result["Findings"].append(True if commonRanges[0] <= score < commonRanges[1] else False)

    # Compare score to threshold

    # Compare findings to actual result
    if result["Findings"][i] == antibioticResList[i]:
        confidence += 1
    

print(tabulate(result, headers="keys", tablefmt="github"))
print(f"Confidence: {confidence / len(antibioticResList) * 100}%")
print(f"Threshold: {threshold}")