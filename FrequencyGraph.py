"""
/***************************************************************************
Name                 : Frequency graph 
Description          : Generates a frequency graphy ( QGIS 2.14 or above )
Date                 : March, 2019.
copyright            : (C) 2019 by Alex Santos
email                : alex.santos@ibge.gov.br

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 
"""

##Controle de Qualidade=group
##3 - Grafico de frequencias = name
##Input=vector
##Fields=Field Input
##Tabela_frequencia=output table

from PyQt4 import QtCore
from PyQt4.QtGui import QMessageBox
from qgis import core as QgsCore
from processing.tools.vector import VectorWriter
from qgis.utils import iface
from processing.tools.vector import TableWriter
from collections import defaultdict
from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException
from qgis.gui import QgsMessageBar

layer = processing.getObject(Input)
Output = Tabela_frequencia

inputFields = layer.pendingFields()
fieldIdxs = []
fields = Fields.split(',')
for f in fields:
    idx = inputFields.indexFromName(f)
    if idx == -1:
        raise GeoAlgorithmExecutionException('Field not found:' + f)
    fieldIdxs.append(idx)
writer = TableWriter(Output, None, fields + ['FREQ'])

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
	
local = Output
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

progress.setInfo('Alex Santos')
QMessageBox.about(None, "Grafico de frequencias", "Grafico gerado com sucesso")
        
