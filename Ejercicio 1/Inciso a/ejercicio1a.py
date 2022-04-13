import pandas as pd
import math
nroFilas=100

def calculaPosicion(arr,percentil):
	i=nroFilas*percentil
	i=i-1
	r=0
	if (i==round(i)):
		r=(arr[round(i)]+arr[round(i)+1])
		r=r/2
	else:
		i=math.ceil(i)
		r=arr[i]
	return r



datos=pd.read_csv("fertility_Diagnosis.txt",sep=",")
titulos=["Temporada   ",
	"Edad        ",
	"Enfermedades",
	"Accidente   ",
	"Intervención",
	"Fiebre      ",
	"Consumo     ",
	"Fumar       ",
	"Sentado     ",
	"class       ",
	"pr            "]
print(datos)
print()

arrX=[
	sorted(datos["Temporada"]),
	sorted(datos["Edad"]),
	sorted(datos["Enfermedades"]),
	sorted(datos["Accidente"]),
	sorted(datos["Intervención"]),
	sorted(datos["Fiebre"]),
	sorted(datos["Consumo"]),
	sorted(datos["Fumar"]),
	sorted(datos["Sentado"]),
	sorted(datos["class"])]

print("---------Perceptil 50---------")
arrPercentil=[]
for x in arrX:
	arrPercentil.append(calculaPosicion(x,0.50))

print(arrPercentil)




print("---------Cuartil primero---------")
arrCuartil=[]
for x in arrX:
	arrCuartil.append(calculaPosicion(x,0.25))

print(arrCuartil)
print()
print("\n\n\n\n\n\n\n\n")
posTitulo=0
for x in arrX:
	print("Percentil: ",titulos[posTitulo],"\t",arrPercentil[posTitulo])
	posTitulo+=1
print()
posTitulo=0
for x in arrX:
	pos=0
	print("Cuartil: ",arrCuartil[posTitulo],end="\t\t")
	print(titulos[posTitulo],end="\t")
	posTitulo+=1
	while (pos<=math.floor(nroFilas/4)):
		print(x[pos],end=" ")
		pos=pos+1
	print()