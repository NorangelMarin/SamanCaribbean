def puertoTour(name, dni, tour, people):
    cuposA = []
    suma = 0
    hora = "7 A.M."
    precio = 30*people
    limite = 4
    cupototal = 10
    for i in cuposA:
        suma += cuposA[i]
        i+=1
        cupototal = suma - cupototal
    if cupototal == 0:
        for i in cuposA:
            cuposA.pop(cuposA[i])
    for i in cuposA:
        suma += cuposA[i]
        i+=1
        cupototal = suma - cupototal 
    if people == 3:
        precio = 60 + (30-30*0.1)
    elif people == 4:
        precio = 60 + (30-30*0.1) + (30-30*0.1)
    if people > limite:
        return "La cantidad de personas supera el limite permitido."
    elif people <= limite and people <= cupototal:
        confirmar_compra = input(f"\nHa seleccionado el tour {tour}, el monto total será de {precio}$. ¿Desea continuar con su compra?(Si o No): ").upper()
        if confirmar_compra == "SI":
            return f"Su tour empieza a las {hora} y el monto de su compra es {precio}$, diviertanse!" #Resumen de compra (Hora y monto con descuento)
            cuposA.append(people)
        elif confirmar_compra == "NO":
            return "Gracias por su tiempo :)."
def degustacionTour(name, dni, tour, people):
    cuposB = []
    suma = 0
    hora = "12 P.M."
    precio = 100*people
    limite = 2
    cupototal = 100
    for i in cuposB:
        suma += cuposB[i]
        i+=1
        cupototal = suma - cupototal
    if cupototal == 0:
        for i in cuposB:
            cuposB.pop(cuposB[i])
    for i in cuposB:
        suma += cuposB[i]
        i+=1
        cupototal = suma - cupototal 
    if people > limite:
        return "La cantidad de personas supera el limite permitido."
    elif people <= limite and people <= cupototal:
        confirmar_compra = input(f"\nHa seleccionado el tour {tour}, el monto total será de {precio}$. ¿Desea continuar con su compra?(Si o No): ").upper()
        if confirmar_compra == "SI":
            return f"Su tour empieza a las {hora} y el monto de su compra es {precio}$, diviertanse!" #Resumen de compra (Hora y monto con descuento)
            cuposB.append(people)
        elif confirmar_compra == "NO":
            return "Gracias por su tiempo :)."
def trotarTour(name, dni, tour, people):
    suma = 0
    hora = "6 A.M."
    precio = 0*people
    confirmar_compra = input(f"\nHa seleccionado el tour {tour}, el monto total será de {precio}$. ¿Desea continuar con su compra?(Si o No): ").upper()
    if confirmar_compra == "SI":
        return f"Su tour empieza a las {hora} y el monto de su compra es {precio}$, diviertanse!" #Resumen de compra (Hora y monto con descuento)
    elif confirmar_compra == "NO":
        return "Gracias por su tiempo :)."
def visitaTour(name, dni, tour, people):
    cuposD = []
    suma = 0
    hora = "10 A.M."
    precio = 40*people
    limite = 4
    cupototal = 15
    for i in cuposD:
        suma += cuposD[i]
        i+=1
        cupototal = suma - cupototal
    if cupototal == 0:
        for i in cuposD:
            cuposD.pop(cuposD[i])
    for i in cuposD:
        suma += cuposD[i]
        i+=1
        cupototal = suma - cupototal 
    if people == 3:
        precio = 80 + (40-40*0.1)
    elif people == 4:
        precio = 80 + (40-40*0.1) + (40-40*0.1)
    if people > limite:
        return "La cantidad de personas supera el limite permitido."
    elif people <= limite and people <= cupototal:
        confirmar_compra = input(f"\nHa seleccionado el tour {tour}, el monto total será de {precio}$. ¿Desea continuar con su compra?(Si o No): ").upper()
        if confirmar_compra == "SI":
            return f"Su tour empieza a las {hora} y el monto de su compra es {precio}$, diviertanse!" #Resumen de compra (Hora y monto con descuento)
            cuposD.append(people)
        elif confirmar_compra == "NO":
            return "Gracias por su tiempo :)."
