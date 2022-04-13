from kanren import run, var, eq, Relation, facts
a = var()
b=var()

Abuelos = Relation()
facts(Abuelos, ("Esperanza","Karina"),("Esperanza","Sergio"),
	("Esperanza","Einar"),("Esperanza","Elena"),
	("Jose","Karina"),("Jose","Sergio"),
	("Jose","Einar"),("Jose","Elena"))
print("\nRelacion Abuelos")
print(Abuelos.facts)

Tios = Relation()
facts(Tios, ("Blady","Karina"),("Blady","Sergio"),("Blady","Elena"),
	("Nilsa","Karina"),("Nilsa","Sergio"),("Nilsa","Einar"),
	("Daysi","Einar"),("Daysi","Elena"),
	("Victor","Einar"),("Victor","Elena"))
print("\nRelacion Tios")
print(Tios.facts)

Padres = Relation()
facts(Padres, ("Esperanza","Nilsa"),("Esperanza","Blady"),("Esperanza","Daysi"),
	("Jose","Nilsa"),("Jose","Blady"),("Jose","Daysi"),
	("Daysi","Karina"),("Daysi","Sergio"),
	("Victor","Karina"),("Victor","Sergio"),
	("Blady","Einar"),("Nilsa","Elena"))
print("\nRelacion Padres")
print(Padres.facts)

Primos = Relation()
facts(Primos, ("Karina","Elena"),("Karina","Einar"),
	("Sergio","Elena"),("Sergio","Einar"),
	("Einar","Elena"))
print("\nRelacion Primos")
print(Primos.facts)


Hijos = Relation()
facts(Hijos, ("Nilsa","Esperanza"),("Blady","Esperanza"),("Daysi","Esperanza"),
	("Nilsa","Jose"),("Blady","Jose"),("Daysi","Jose"),
	("Sergio","Daysi"),("Karina","Daysi"),
	("Sergio","Victor"),("Karina","Victor"),
	("Einar","Blady"),("Elena","Nilsa"),)
print("\nRelacion Hijos")
print(Hijos.facts)

print("\n\n\n---------------Preguntas---------------\n\n\n")

t=10
	
while(t!=0):
	print("Que relacion desea consultar?")
	print("1.-   Abuelos")
	print("2.-   Tios")
	print("3.-   Padres")
	print("4.-   Hijos")
	print("5.-   Primos")
	print("0.-   Salir")
	t=int(input())
	if t==1:
		print("\t1.- buscar los nielos de X")
		print("\t2.- buscar los abuelos de X")
		t1=int(input("\t"))
		print("\tIntro X:")
		x=input("\t")
		if(t1==1):
			print("\t",run(10,a,Abuelos(x,a)))
		if(t1==2):
			print("\t",run(10,a,Abuelos(a,x)))
	if t==2:
		print("\t1.- buscar los Sobrinos de X")
		print("\t2.- buscar los Tios de X")
		t1=int(input("\t"))
		print("\tIntro X:")
		x=input("\t")
		if(t1==1):
			print("\t",run(10,a,Tios(x,a)))
		if(t1==2):
			print("\t",run(10,a,Tios(a,x)))
	if t==3:
		print("\t1.- buscar los Hijos de X")
		print("\t2.- buscar los Padres de X")
		t1=int(input("\t"))
		print("\tIntro X:")
		x=input("\t")
		if(t1==1):
			print("\t",run(10,a,Padres(x,a)))
		if(t1==2):
			print("\t",run(10,a,Padres(a,x)))
	if t==4:
		print("\t1.- buscar los Padres de X")
		print("\t2.- buscar los Hijos de X")
		t1=int(input("\t"))
		print("\tIntro X:")
		x=input("\t")
		if(t1==1):
			print("\t",run(10,a,Hijos(x,a)))
		if(t1==2):
			print("\t",run(10,a,Hijos(a,x)))
	if t==5:
		print("\t1.- buscar los Primos de X")
		t1=int(input("\t"))
		print("\tIntro X:")
		x=input("\t")
		if(t1==1):
			print("\t",run(10,a,Primos(x,a)),"\t",run(10,a,Primos(a,x)))

print("\n\n-----------------------FIN-----------------------")
