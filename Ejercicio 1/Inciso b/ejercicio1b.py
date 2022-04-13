import pandas as pd
import numpy as np
datos=pd.read_csv("fertility_Diagnosis2.txt",sep=",")
print(datos)

print("---------Perceptil 50---------")
print(np.percentile(datos,50,axis=0))
print("---------Cuartil 1 por Columna---------")
print(np.quantile(datos,0.25,axis=0))