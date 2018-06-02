##Controle de Qualidade=group
##Verificar quantidade de inconsistencias=name
##Input=vector
##Fields=Field Input
##Frequency=output table

from PyQt4 import QtCore
from qgis import core as QgsCore
from qgis.utils import iface
from processing.tools.vector import TableWriter
from collections import defaultdict
from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException

layer = processing.getObject(Input)
inputFields = layer.pendingFields()
fieldIdxs = []
fields = Fields.split(',')
for f in fields:
    idx = inputFields.indexFromName(f)
    if idx == -1:
        raise GeoAlgorithmExecutionException('Field not found:' + f)
    fieldIdxs.append(idx)
writer = TableWriter(Frequency, None, fields + ['FREQ'])

counts = {}
feats = processing.features(layer)
nFeats = len(feats)
counts = defaultdict(int)
for i, feat in enumerate(feats):
    progress.setPercentage(int(100 * i / nFeats))
    attrs = feat.attributes()
    clazz = tuple([attrs[i] for i in fieldIdxs])
    counts[clazz] += 1

for c in counts:
    writer.addRecord(list(c) + [counts[c]])


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
	
local = Frequency
#local='D:/Users/alx/.qgis2/processing/scripts/Frequency.csv'

import csv

with open(local) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    Fields = []
    FREQ = []
    linha = 1
    next(readCSV)
    for row in readCSV:
        temp_1 = row[0][0:30]
        temp_2 = float(row[1])
        Fields.append(temp_1)
        FREQ.append(temp_2)   

print(Fields)
print(FREQ)
objects = Fields
y_pos = np.arange(len(objects))
performance = FREQ	
 
plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, objects)
plt.ylabel('Frequencia')
plt.title('Grafico de frequencia')
 
plt.show()	
