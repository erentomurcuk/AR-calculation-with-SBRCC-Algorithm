import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

eColiList = []
amoxResList = []

with open('dairy_farms_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Skip the header row
    headerRow = next(reader)
    
    for row in reader:
        eColiValue = row[headerRow.index("plain_undiluted")]
        amoxValue = row[headerRow.index("amoxR")]

        eColiList.append(int(eColiValue))
        amoxResList.append(True if amoxValue == '1' else False)

# Hurdaci geliyah gksdngks aliyom

uniqueEColiValues = [value for value, condition in zip(eColiList, amoxResList) if condition]

eColiCounter = Counter(uniqueEColiValues)
sortedEColiCounter = dict(sorted(eColiCounter.items(), key=lambda item: item[0]))

for key, value in sortedEColiCounter.items():
    print(f"{key}: {value}")

xValues = list(sortedEColiCounter.keys())
yValues = list(sortedEColiCounter.values())

print(sum(yValues))
print(sum(xValues))

newValue = np.interp(2800, xValues, yValues)
print(newValue)

plt.plot(xValues, yValues, marker='o')

plt.xlabel("E. Coli Count")
plt.ylabel("Frequency of Amox Resistance")

plt.show()